#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt
from scanpy import pp
from scanpy import tl
from scanpy import pl


# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 


pp.neighbors(adata, n_neighbors=10, n_pcs=40)


tl.leiden(adata)

tl.umap(adata, maxiter=900)

# pl.scatter(adata, color='leiden', title='UMAP of PBMcs', basis='umap', save='scatter.png')

tl.tsne(adata)

# pl.scatter(adata, color='leiden', title='t-SNE of PBMcs', basis='tsne', save='scatter.png')


wilcoxon_adata = sc.tl.rank_genes_groups(adata, method='wilcoxon', groupby='leiden', use_raw=True, copy=True)

logreg_adata = sc.tl.rank_genes_groups(adata, method='logreg', groupby='leiden', use_raw=True, copy=True, max_iter=100000000000)

sc.pl.rank_genes_groups(wilcoxon_adata, n_genes=25, title='Top 25 Wilcoxon Genes', sharey=False, show=False, use_raw=True, save='wilcoxon.png')
sc.pl.rank_genes_groups(logreg_adata, n_genes=25, title='Top 25 Logistic Regression Genes', sharey=False, show=False, use_raw=True, save='logreg.png')

leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne

adata.write('filtered_clustered_data.h5')

adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy

# fig, axs = plt.subplots(1, 4, figsize=(18, 5), gridspec_kw={'width_ratios': [1, 1, 1, 0.05]})

# # Scatter plot for LYZ gene
# sc.pl.scatter(adata, color='LYZ', title='LYZ Gene UMAP', basis='umap', ax=axs[0], show=False, color_map='viridis')

# # Scatter plot for LDHB gene
# sc.pl.scatter(adata, color='LDHB', title='LDHB Gene UMAP', basis='umap', ax=axs[1], show=False, color_map='viridis')

# # Scatter plot for CD79A gene
# sc.pl.scatter(adata, color='CD79A', title='CD79A Gene UMAP', basis='umap', ax=axs[2], show=False, color_map='viridis')

# # Create a color bar
# cbar = plt.colorbar(axs[2].collections[0], cax=axs[3], orientation='vertical', label='Expression')

# # Adjust layout
# plt.tight_layout()

# plt.show()


adata.rename_categories('leiden', ['LDHB', 'LYZ', 'CD79A', '3', '4', '5', '6', '7'])
sc.pl.scatter(adata, color='leiden', title='Overall UMAP', basis='umap', color_map='viridis')
plt.show()