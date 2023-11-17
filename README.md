Rscript runChicago.R --design-dir /Users/cmdb/qbb2023-answers/week8/raw/Design --en-feat-list /Users/cmdb/qbb2023-answers/week8/raw/Features/featuresGM.txt --export-format washU_text /Users/cmdb/qbb2023-answers/week8/raw/PCHIC_Data/GM_rep1.chinput,/Users/cmdb/qbb2023-answers/week8/raw/PCHIC_Data/GM_rep2.chinput,/Users/cmdb/qbb2023-answers/week8/raw/PCHIC_Data/GM_rep3.chinput GM12878


Step 1.2

These enrichments make sense to me; for the most part, the epigenetic marks typically associated with euchromatin are more highly enriched.

CTCF: insulators could be associated with enrichment, as they prevent the spread of adjacent H3K27me3
H3K4me1: this epigenetic mark is usually activating, so the high enrichment compared to random samples makes sense.
H3K4me3: this mark is also generally activating, so the pattern makes sense.
H3K27ac: acetylation creates euchromatin, and prevents repressive methylation at H3K27. Thus it makes sense that this is highly enriched in overlaps compared to random samples.
H3K27me3: this mark is repressive, so it makes sense that it is not enriched.
H3K9me3: this mark is usually repressive, so the enrichment is somewhat unexpected. However, the magnitude of enrichment is small compared to other interactions.



Top 6 interactions between two promoters:
1645  chr20  44438565  44565593  .  1000  34.77  .   0  chr20  44562442  44565593         PCIF1  +  chr20  44438565  44442365        UBE2C  +
1655  chr20  44438565  44607204  .   986  34.29  .   0  chr20  44596299  44607204  FTLP1;ZNF335  +  chr20  44438565  44442365        UBE2C  +
2819  chr21  26837918  26939577  .   978  34.02  .   0  chr21  26837918  26842640        snoU13  +  chr21  26926437  26939577     MIR155HG  +
1646  chr20  44452862  44565593  .   974  33.89  .   0  chr20  44562442  44565593         PCIF1  +  chr20  44452862  44471524  SNX21;TNNC2  +
475   chr20  17660712  17951709  .   973  33.85  .   0  chr20  17946510  17951709    MGME1;SNX5  +  chr20  17660712  17672229        RRBP1  +
577   chr20  24972345  25043735  .   973  33.84  .   0  chr20  24972345  24985047         APMAP  +  chr20  25036380  25043735        ACSS1  +


Top 6 interactions between a promoter and enhancer:
2842  chr21  26797667  26939577  .  952  33.13  .   0  chr21  26926437  26939577            MIR155HG  +  chr21  26797667  26799364  .  -
2254  chr20  55957140  56074932  .  928  32.29  .   0  chr20  55957140  55973022  RBM38;RP4-800J21.3  +  chr20  56067414  56074932  .  -
2838  chr21  26790966  26939577  .  838  29.17  .   0  chr21  26926437  26939577            MIR155HG  +  chr21  26790966  26793953  .  -
231   chr20   5585992   5628028  .  830  28.88  .   0  chr20   5585992   5601172              GPCPD1  +  chr20   5625693   5628028  .  -
2839  chr21  26793954  26939577  .  754  26.23  .   0  chr21  26926437  26939577            MIR155HG  +  chr21  26793954  26795680  .  -
278   chr20   5515866   5933156  .  750  26.08  .   0  chr20   5929472   5933156          MCM8;TRMT6  +  chr20   5515866   5523933  .  -


RBM38 does make sense to be interacting with enhancers in GM12878, as it is involved in the DNA damage response. This gene is expressed in lymph nodes, so it makes sense that it would be expressed in immune cells such as B cells.
MIR155HG also makes sense - it is an oncogenic microRNA that is expressed at high levels in lymphoma.
