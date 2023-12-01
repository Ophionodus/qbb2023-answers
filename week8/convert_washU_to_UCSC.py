#!/usr/bin/env python
import sys
import numpy as np
import pandas as pd

baitmap = sys.argv[1]
washu = sys.argv[2]

baitmap = pd.read_csv(baitmap, header=None, delim_whitespace=True)
washu = pd.read_csv(washu, header=None, sep='\s|,', engine='python')

baitmap['fragment_pos'] = 'chr' + baitmap.iloc[:,0].astype(str) + ',' + baitmap.iloc[:, 1].astype(str) + ',' + baitmap.iloc[:, 2].astype(str)
baitmap.index = baitmap['fragment_pos']
# print(baitmap)

# print(washu)

# for index, washu_row in washu.iterrows():
#     washu_chromosome = washu_row[0].replace('chr', '')
#     left_start = washu_row[1]
#     right_start = washu_row[4]

    
#     for index_baitmap, baitmap_row in baitmap.iterrows():
#         baitmap_chromosome = baitmap_row[0]
#         baitmap_start = baitmap_row[1]


#         if left_start == baitmap_start and int(baitmap_chromosome) == int(washu_chromosome):
#             washu.loc[index, 'Bait Fragment'] = "left"
#             washu.loc[index, 'Gene'] = baitmap_row[4]
#         if right_start == baitmap_start and int(baitmap_chromosome) == int(washu_chromosome):
#             washu.loc[index, 'Bait Fragment'] = "right"
#             washu.loc[index, 'Gene'] = baitmap_row[4]

# print(washu)

# # columns = ('chrom', 'chromStart', 'chromEnd', 'name', 'score', 'value', 'ex', 'color', 'sourceChrom', 'sourceStart', 'sourceEnd', 'sourceName', 'sourceStrand', 'targetChrom', 'targetStart', 'targetEnd', 'targetName', 'targetStrand')
ucsc = open("ucsc.bed", 'w')
ucsc.write("track type=interact name=\"pCHIC\" description=\"Chromatin interactions\" useScore=on maxHeightPixels=200:100:50 visibility=full" + "\n")

for index, washu_row in washu.iterrows():
	strength = int((washu_row[6])/(np.max(washu.loc[:, 6])) * 1000)
	value = washu_row[6]
	chrom = washu_row[0]
	chromStart = min(washu_row[1], washu_row[4])
	chromEnd = max(washu_row[2], washu_row[5])

	washu_string1 = str(washu_row[0]) + ',' + str(washu_row[1]) + ',' + str(washu_row[2])
	washu_string2 = str(washu_row[3]) + ',' + str(washu_row[4]) + ',' + str(washu_row[5])

	if washu_string1 in baitmap.index:
		s_chrom = washu_row[0]
		s_start = washu_row[1]
		s_end = washu_row[2]
		s_gene = baitmap.loc[washu_string1, 4]
		s_strand = '+'
		t_chrom = washu_row[3]
		t_start = washu_row[4]
		t_end = washu_row[5]
		if washu_string2 in baitmap.index:
			t_gene = baitmap.loc[washu_string2, 4]
			t_strand = '+'
		else:
			t_gene = '.'
			t_strand = '-'
	else:
		s_chrom = washu_row[3]
		s_start = washu_row[4]
		s_end = washu_row[5]
		s_strand = '+'
		s_gene = baitmap.loc[washu_string2, 4]
		t_chrom = washu_row[0]
		t_start = washu_row[1]
		t_end = washu_row[2]
		t_strand = '-'
		t_gene = '.'
	ucsc.write(str(chrom) + "\t" +  str(chromStart) + "\t" +  str(chromEnd) + "\t" +  '.' + "\t" +  str(strength) + "\t" +  str(value) + "\t" +  '.' + "\t" +  '0' + "\t" +  str(s_chrom) + "\t" +  str(s_start) + "\t" +  str(s_end) + "\t" +  str(s_gene) + "\t" +  str(s_strand) + "\t" +  str(t_chrom) + "\t" +  str(t_start) + "\t" +  str(t_end) + "\t" +  str(t_gene) + "\t" +  str(t_strand) + "\n")
ucsc.close()
ucsc_file = pd.read_csv("ucsc.bed", skiprows=1, header=None, delim_whitespace=True)
# print(ucsc_file)

plusses = ucsc_file.loc[ucsc_file.loc[:, 17]=='+', :]

sorted_plusses = (plusses.sort_values(4, ascending=False))
# print(sorted_plusses.iloc[0:6, :])

minuses = ucsc_file.loc[ucsc_file.loc[:, 17]=='-', :]

sorted_minuses = (minuses.sort_values(4, ascending=False))
print(sorted_minuses.iloc[0:6, :])


