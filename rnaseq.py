import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
import matplotlib.pyplot as plt

# # read in data
# counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col=0)

# # read in metadata
# metadata = pd.read_csv("gtex_metadata.txt", index_col=0)

# counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# counts_df_normed = np.log2(counts_df_normed + 1)

# full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

# allgenes = pd.DataFrame(columns=['Gene', 'Slope', 'P-value'])

# for column_name in counts_df_normed.columns:
#     model = smf.ols(formula=f'Q("{column_name}") ~ SEX', data=full_design_df)
#     results = model.fit()
#     slope = results.params['SEX']
#     pval = results.pvalues['SEX']
#     allgenes.loc[len(allgenes), :] = [column_name, slope, pval]

# allgenes.to_csv("allgenes.csv")

# genes = pd.read_csv("allgenes.csv", index_col=0)

# fdr = multitest.fdrcorrection(genes.loc[:, "P-value"], alpha=0.10, method='indep', is_sorted=False)

# genes['fdr'] = fdr[0]

# trues = genes.loc[genes.loc[:, 'fdr'], :]

# trues.to_csv("diff_expressed_10%_FDR.csv")

from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

# dds = DeseqDataSet(
#     counts=counts_df,
#     metadata=metadata,
#     design_factors="SEX",
#     n_cpus=4,
# )

# dds.deseq2()
# stat_res = DeseqStats(dds)
# stat_res.summary()
# results = stat_res.results_df

# results.to_csv("pydeseq2_results.csv")

pyde = pd.read_csv("pydeseq2_results.csv", index_col=0)

pyde_filtered = pyde.loc[pyde.loc[:, 'padj'] > 0.1, :]

#jaccard = (len(trues) / (len(pyde_filtered)))* 100
#print(jaccard)


plt.scatter(pyde.loc[:, "log2FoldChange"], (-(np.log10(pyde.loc[:, "pvalue"]))), c='b')
plt.scatter(pyde.loc[(pyde.loc[:, 'log2FoldChange'].abs() > 1) & (pyde.loc[:, 'padj'] < 0.1), "log2FoldChange"], 
	-(np.log10(pyde.loc[(pyde.loc[:, 'log2FoldChange'].abs() > 1) & (pyde.loc[:, 'padj'] < 0.1), "pvalue"])), c='r')

plt.show()
