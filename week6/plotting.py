#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = open("plink.eigenvec")
pc1 = []
pc2 = []
for line in file:
	split = line.split(' ')
	pc1.append(split[2])
	pc2.append(split[3])
plt.scatter(pc1, pc2)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
# plt.show()
plt.close()


freqDF = pd.read_csv('genotype.frq', header=0, delim_whitespace=True)


# fig, ax = plt.subplots()
# ax.hist(freqDF.loc[:, 'MAF'], bins=100)
# ax.set_xlabel("MAF")
# ax.set_ylabel("Number of Variants")
# fig.savefig('Allele_Frequencies.png')

Phen1 = pd.read_csv("CB1908_IC50_gwas_results.assoc.linear", header=0, delim_whitespace=True)
Phen1_filtered = Phen1.loc[Phen1.loc[:, 'TEST']=='ADD', :]
pvalues = (Phen1_filtered.loc[:, 'P'])
cbpval = pvalues
pvalues = -np.log10(pvalues)


Phen2 = pd.read_csv("GS451_IC50_gwas_results.assoc.linear", header=0, delim_whitespace=True)
Phen2_filtered = Phen2.loc[Phen2.loc[:, 'TEST']=='ADD', :]
pvalues2 = (Phen2_filtered.loc[:, 'P'])
gspval = pvalues2
pvalues2 = -np.log10(pvalues2)

pvalueshigh = []
pvalues2high = []
pvalueslow = []
pvalues2low = []

for val in pvalues:
	if val<(5):
		pvalueslow.append(val)
	else:
		pvalueshigh.append(val)

for val in pvalues2:
	if val<(5):
		pvalues2low.append(val)
	else:
		pvalues2high.append(val)

# fig, ax = plt.subplots(2,1)
# ax[0].plot(pvalueshigh, 'ro')
# ax[1].plot(pvalues2high, 'ro')
# ax[0].plot(pvalueslow, 'bo')
# ax[1].plot(pvalues2low, 'bo')
# ax[0].title.set_text('CB1908')
# ax[1].title.set_text('GS451')
# plt.xlabel("SNP")
# plt.ylabel("-log10(pvalue)")
# fig.savefig('Manhattan_plot.png')

small = (np.min(cbpval))
# print(Phen1.loc[Phen1['P'] == small])

genotypes = pd.read_csv("genotypes.vcf", header=27, delim_whitespace=True)
bestsnp = genotypes.loc[genotypes.loc[:, 'ID']=='rs10876043', :]
beet = bestsnp.loc[:, '1001_1001':'1176_1176']
bestsnplist = beet.values.flatten().tolist()

phenotypes = pd.read_csv("CB1908_IC50.txt", header=0, delim_whitespace=True)
phenz = phenotypes.loc[:, 'CB1908_IC50']
phenlist = phenz.values.flatten().tolist()
b = 0
n = 0
gt1 = []
gt2 = []
gt3 = []
t = 0
# for phen in phenlist:
# 	if phen == 'nan':
# 		phenlist.remove(phen)
# 		bestsnplist.remove(bestsnplist[t])
# 		t=t+1
for genotype in bestsnplist:
	if genotype == '0/0':
		gt1.append(phenlist[n])
	elif genotype == '0/1':	
		gt2.append(phenlist[n])
	elif genotype == '1/1':
		gt3.append(phenlist[n])
	elif genotype == './.':
		b=b+1
	n = n+1

data = [gt1, gt2, gt3]

for i in range(len(data)):
	data[i] = [x for x in data[i] if str(x) != 'nan']

#print(data[0])
#print(data[1])
#print(data[2])
plt.boxplot(data)
plt.xlabel('Genotype; 1=A/A   2=A/G   3=G/G')
plt.ylabel('IC50')
plt.show()


