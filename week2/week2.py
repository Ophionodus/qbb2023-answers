#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# =======================
#       exercise 1
# =======================

def simulate_coverage(coverage, genome_len, read_len, figname):

	coverage_arr = np.zeros(genome_len)

	num_reads = int(coverage * genome_len / read_len)

	low = 0

	high = genome_len - read_len

	start_positions = np.random.randint(low=0, high=high+1, size=num_reads)   #high is exclusive

	for start in start_positions:
		coverage_arr[start: start+read_len] += 1

	x = np.arange(0, max(coverage_arr)+1)
	sim_0cov = genome_len - np.count_nonzero(coverage_arr)
	sim_0cov_pct = 100* sim_0cov / genome_len

	print(f'In the simulation, there are {sim_0cov} bases with 0 coverage.')
	print(f'This is {sim_0cov_pct}% of the genome.')

	# Get Poisson Distribution
	y_poisson = stats.poisson.pmf(x, mu = coverage ) * genome_len


	# Get Normal Distribution
	y_normal = stats.norm.pdf(x, loc= coverage, scale=np.sqrt(coverage)) * genome_len


	fig, ax = plt.subplots()
	ax.hist(coverage_arr, bins=x, align='left', label='Simulation')
	ax.plot(x, y_poisson, label='Poisson')
	ax.plot(x, y_normal, label='Normal')
	ax.set_xlabel('Coverage')
	ax.set_ylabel('Frequency (bp)')
	ax.legend()
	fig.tight_layout()
	fig.savefig(figname)
	plt.show()

#simulate_coverage(30, 1_000_000, 100, 'ex1_30x_cov.png')




reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

graph = set()

for read in reads:
	for i in range(len(read) - 3 - 1):
		kmer1 = read[i: i+3]
		kmer2 = read[i+1: i+1+3]
		graph.add(f'{kmer1} -> {kmer2}')

for edge in graph:
	print(edge)



f = open("dotfile.txt", "w")
f.write("digraph {")
for line in graph:
	f.write(line + '\n')
f.write("}")
f.close()


