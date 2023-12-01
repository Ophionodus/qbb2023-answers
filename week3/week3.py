#!/usr/bin/env python

from fasta import readFASTA
import numpy as np
import sys
import pandas as pd

fasta = sys.argv[1]
scoring_matrix = sys.argv[2]

filepath = sys.argv[4]

file = open(filepath, "a")
input_sequences = readFASTA(open(fasta))
score = pd.read_csv(scoring_matrix,delim_whitespace=True)
gap_penalty = float(sys.argv[3])

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]



F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
T_matrix = np.empty((len(sequence1)+1, len(sequence2)+1), dtype=str)


for i in range(len(sequence1)+1):
	T_matrix[i,0] = "v"

for j in range(len(sequence2)+1):
	T_matrix[0,j] = "h"





for i in range(len(sequence1)+1):
	F_matrix[i,0] = i*gap_penalty

for j in range(len(sequence2)+1):
	F_matrix[0,j] = j*gap_penalty

for i in range(1, len(sequence1)+1): # loop through rows
	for j in range(1, len(sequence2)+1): # loop through columns
		d = F_matrix[i-1, j-1] + score.loc[sequence1[i-1],sequence2[j-1]]
		h = F_matrix[i,j-1] + gap_penalty
		v = F_matrix[i-1,j] + gap_penalty

		F_matrix[i,j] = max(d,h,v)
		if F_matrix[i,j] == d:
			T_matrix[i,j] = "d"
		elif F_matrix[i,j] == h:
			T_matrix[i,j] = "h"
		elif F_matrix[i,j] == v:
			T_matrix[i,j] = "v"





for i in range(len(sequence1)+1):
	max(F_matrix[i-1,j-1], F_matrix[i,j-1], F_matrix[i-1,j])

alignment_score = F_matrix[i,j]


seq1_output = ""
seq2_output = ""
seq1_gaps = 0
seq2_gaps = 0

while i != 0 or j!=0:

	if T_matrix[i,j] == "d":
		i = i-1
		j = j-1
		seq1_output = seq1_output + sequence1[i]
		seq2_output = seq2_output + sequence2[j]
	elif T_matrix[i,j] == "h":
		j = j-1
		seq1_output = seq1_output + "-"
		seq1_gaps = seq1_gaps + 1
		seq2_output = seq2_output + sequence2[j]
	elif T_matrix[i,j] == "v":
		i = i-1
		seq1_output = seq1_output + sequence1[i]
		seq2_output = seq2_output + "-"
		seq2_gaps = seq2_gaps + 1
file.write("Sequence 1:")
file.write(seq1_output)
file.write("Sequence 2:")
file.write(seq2_output)
file.write("Sequence 1 Gaps:")
file.write(str(seq1_gaps))
file.write("Sequence 2 Gaps:")
file.write(str(seq2_gaps))
file.write("Alignment Score:")
file.write(str(alignment_score))
file.close()
