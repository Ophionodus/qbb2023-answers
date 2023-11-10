#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file1 = open("ONT.cpg.chr2.bedgraph")

file2 = open("bisulfite.cpg.chr2.bedgraph")

colnames = ['chromosome', 'start', 'end', 'percent_methylated', 'read_coverage']

ont = pd.read_csv('ONT.cpg.chr2.bedgraph', header=None, names=colnames, delim_whitespace=True)

bis = pd.read_csv('bisulfite.cpg.chr2.bedgraph', header=None, names=colnames, delim_whitespace=True)

ont_combined = set((ont['chromosome'] + '_' + ont['start'].astype(str)).tolist())

bis_combined = set((bis['chromosome'] + '_' + bis['start'].astype(str)).tolist())

intersection = ont_combined.intersection(bis_combined)

ont_only = [ element for element in ont_combined if element not in bis_combined] 
bis_only = [ element for element in bis_combined if element not in ont_combined] 

# print("Shared sites:", len(intersection))

# print("ONT only:", len(ont_only))

# print("Bisulfite only:", len(bis_only))

# print("Jaccard Index:", (len(intersection))/(len(ont_combined|bis_combined)))

fig, ax = plt.subplots(4, 1)
ax[0].hist(ont.loc[:, 'read_coverage'], bins=max(ont.loc[:, 'read_coverage']), label="ONT Coverage", alpha=0.5)
ax[0].hist(bis.loc[:, 'read_coverage'], bins=max(bis.loc[:, 'read_coverage']), label="Bisulfite Coverage", alpha=0.5)
ax[0].legend()
ax[0].set_xlim([0, 100])


ont.index = ont['chromosome'] + '_' + ont['start'].astype(str)
bis.index = bis['chromosome'] + '_' + bis['start'].astype(str)
intersection_list = list(intersection)

ont_filtered = ont.loc[intersection_list, :]
bis_filtered = bis.loc[intersection_list, :]


ont_hist = np.histogram2d(ont_filtered.loc[:, 'percent_methylated'], bis_filtered.loc[:, 'percent_methylated'], range=((0, 100), (0, 100)), bins=100)[0]
ont_hist = np.log10(ont_hist + 1)
ax[1].imshow(ont_hist)
ax[1].set_xlabel('ONT')
ax[1].set_ylabel('Bisulfite')
ax[1].set_title('Pearson Correlation Coefficient: 0.010')


ont_methylation = ont.loc[:, 'percent_methylated'].values
bis_methylation = bis.loc[:, 'percent_methylated'].values


ont_methylation = np.pad(ont_methylation, (0, bis_methylation.shape[0] - ont_methylation.shape[0]), mode='constant', constant_values=0)

pearson = np.corrcoef(ont_methylation, bis_methylation)[0, 1]
# print(pearson)





tumor_ont = pd.read_csv('tumor.ONT.chr2.bedgraph', header=None, names=colnames, delim_whitespace=True)

normal_ont = pd.read_csv('normal.ONT.chr2.bedgraph', header=None, names=colnames, delim_whitespace=True)

tumor_bis = pd.read_csv('tumor.bisulfite.chr2.bedgraph', header=None, names=colnames, delim_whitespace=True)

normal_bis = pd.read_csv('normal.bisulfite.chr2.bedgraph', header=None, names=colnames, delim_whitespace=True)


tumor_ont_combined = set((tumor_ont['chromosome'] + '_' + tumor_ont['start'].astype(str)).tolist())

normal_ont_combined = set((normal_ont['chromosome'] + '_' + normal_ont['start'].astype(str)).tolist())

tumor_bis_combined = set((tumor_bis['chromosome'] + '_' + tumor_bis['start'].astype(str)).tolist())

normal_bis_combined = set((normal_bis['chromosome'] + '_' + normal_bis['start'].astype(str)).tolist())

common_ont = tumor_ont_combined.intersection(normal_ont_combined)

common_bis = tumor_bis_combined.intersection(normal_bis_combined)

tumor_ont.index = tumor_ont['chromosome'] + '_' + tumor_ont['start'].astype(str)
tumor_bis.index = tumor_bis['chromosome'] + '_' + tumor_bis['start'].astype(str)
normal_ont.index = normal_ont['chromosome'] + '_' + normal_ont['start'].astype(str)
normal_bis.index = normal_bis['chromosome'] + '_' + normal_bis['start'].astype(str)
ont_list = []
bis_list = []
for location in common_ont:
	ont_list.append((tumor_ont.loc[location, 'percent_methylated']) - (normal_ont.loc[location, 'percent_methylated']))
for location in common_bis:
	bis_list.append((tumor_bis.loc[location, 'percent_methylated']) - (normal_bis.loc[location, 'percent_methylated']))

ax[2].violinplot(ont_list)
ax[2].set_ylabel("Change in Percent Methylation from Normal to Tumor(ONT)")
ax[3].violinplot(bis_list)
ax[3].set_ylabel("Change in Percent Methylation from Normal to Tumor(Bisulfite)")



fig.savefig('methylation_comparison.png', bbox_inches='tight', dpi=300)