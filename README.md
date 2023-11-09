plink --pca --vcf genotypes.vcf 


plink --maf --make-bed --vcf genotypes.vcf 




plink --vcf genotypes.vcf --linear --pheno phenotype.txt --covar pca.eigenvec --allow-no-sex --out phenotype_gwas_results



Near my SNP of interest, I found this gene:


Description: Disco-interacting protein 2 homolog B (DIP2 homolog B).
RefSeq Summary (NM_173602): This gene encodes a member of the disco-interacting protein homolog 2 protein family. The encoded protein contains a binding site for the transcriptional regulator DNA methyltransferase 1 associated protein 1 as well as AMP-binding sites. The presence of these sites suggests that the encoded protein may participate in DNA methylation. This gene is located near a folate-sensitive fragile site, and CGG-repeat expansion in the promoter of this gene which affects transcription has been detected in individuals containing this fragile site on chromosome 12. [provided by RefSeq, Aug 2011]. 


Changes in DNA methylation could affect a wide range of regulatory processes in cells, which could pose as risk factors for lymphocytophenia.