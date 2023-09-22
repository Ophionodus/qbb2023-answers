Step 1.1
1.
1 million X 3 divided by 100 = 
30,000

Step 1.3
1.
49210 bases had 0 coverage, which is 4.921 percent of the genome.
2.
This fits the Poisson distribution better than the normal distribution.

Step 1.4
1.
55 bases had 0 coverage, which is 0.0055 percent of the genome. 
2.
This fits the normal distribution a bit better than 3, but the Poisson is still a better fit.

Step 1.5
1.
Only 14 bases have 0 coverage, which is 0.0014 percent of the genome.
2.
The Poisson distribution and the normal distribution seem to be equally good fits at this coverage.

Step 2.4

I used this code to make a dot graph:
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


Step 2.5

TTGATTCATTGATTCTTAT

Step 2.6 

To accurately reconstruct the sequence of the genome, we would need to know the total length of the genome, and which read comes first. Then we would know whether there are repeats of certain paths through the graph and we could reconstruct it.

Step 3.1 

Prompt: 
Write an essay about why I am interested in genomics, referring to the applications of genomics to the fields of cell biology, molecular biology, developmental biology, and biophysics. Provide references.

Output:
Title: Exploring the Fascinating World of Genomics: A Journey through its Applications in Biology and Biophysics

Introduction

The field of genomics has captured my curiosity and passion, drawing me into its intricate web of scientific marvels and limitless possibilities. Genomics, the study of an organism's complete set of genes and their functions, holds the key to unraveling the mysteries of life at its most fundamental level. My interest in genomics stems from its profound applications in various biological disciplines, such as cell biology, molecular biology, developmental biology, and biophysics. In this essay, I will elucidate the reasons behind my fascination with genomics, shedding light on how it has revolutionized these fields and continues to drive innovation.

Genomics in Cell Biology

Cell biology explores the structure and function of cells, the building blocks of life. Genomics has significantly impacted this field by providing valuable insights into the molecular mechanisms that govern cellular processes. The study of gene expression patterns using techniques like RNA-Seq and single-cell RNA sequencing has allowed researchers to dissect the intricacies of cellular diversity. Understanding how genes are regulated in different cell types and under various conditions has paved the way for targeted therapies in diseases like cancer, where the genomic landscape is often altered.

For instance, the Cancer Genome Atlas (TCGA) project has delved into the genomic alterations in various cancer types, enabling the identification of specific genetic mutations and alterations responsible for cancer initiation and progression (1). The newfound knowledge has opened doors to personalized cancer treatments, exemplifying how genomics is transforming cell biology.

Genomics in Molecular Biology

Molecular biology focuses on the mechanisms underlying the interactions of biomolecules within cells. Genomics has revolutionized this field by providing a comprehensive map of an organism's genes and their functions. It has allowed scientists to identify genes responsible for vital biological processes, disease susceptibility, and the development of new therapeutic targets.

One remarkable application is the CRISPR-Cas9 genome editing system, which relies on genomics to precisely target and modify genes (2). This revolutionary technology has profound implications for the treatment of genetic disorders and the study of gene function, epitomizing how genomics is at the forefront of molecular biology research.

Genomics in Developmental Biology

Developmental biology explores the intricate processes that drive an organism's growth and differentiation from a single cell to a complex multicellular organism. Genomics has played a pivotal role in deciphering the genetic basis of development. By comparing the genomes of different species, researchers can uncover conserved genes and regulatory elements responsible for key developmental pathways.

The Human Genome Project, a monumental genomics endeavor, has provided a comprehensive reference for understanding human development and evolution (3). Additionally, the emerging field of epigenomics, which studies modifications to DNA and histones, has shed light on how epigenetic changes influence development and differentiation (4). Genomics, in conjunction with developmental biology, has thus uncovered the intricate genetic tapestry underlying life's most fundamental processes.

Genomics in Biophysics

Biophysics is an interdisciplinary field that seeks to understand biological processes from a physical perspective. Genomics has contributed significantly to biophysics by providing a wealth of data on the molecular components of living organisms. This data can be used to model and simulate biological systems, allowing researchers to gain insights into the physical principles governing biological processes.

For example, the field of structural genomics has led to the determination of three-dimensional structures of proteins and their interactions, aiding in drug discovery and the development of therapeutics (5). Genomic information also underpins computational models of cellular processes, enabling biophysicists to simulate complex phenomena such as protein folding and cellular signaling (6). Genomics has thus become an indispensable tool in advancing our understanding of the physical aspects of biology.

Conclusion

In conclusion, my fascination with genomics stems from its transformative impact on the fields of cell biology, molecular biology, developmental biology, and biophysics. Genomics has enabled researchers to unravel the genetic underpinnings of life's most fundamental processes, offering insights that have led to groundbreaking discoveries and innovative applications. As the field continues to evolve and expand, it promises to unlock even more secrets of the biological world, making it an exciting and promising area of study.

References:

Weinstein, J. N., Collisson, E. A., et al. (2013). The Cancer Genome Atlas Pan-Cancer analysis project. Nature Genetics, 45(10), 1113-1120.
Doudna, J. A., & Charpentier, E. (2014). The new frontier of genome engineering with CRISPR-Cas9. Science, 346(6213), 1258096.
Lander, E. S., Linton, L. M., et al. (2001). Initial sequencing and analysis of the human genome. Nature, 409(6822), 860-921.
Portela, A., & Esteller, M. (2010). Epigenetic modifications and human disease. Nature Biotechnology, 28(10), 1057-1068.
Montelione, G. T., & Anderson, S. (2002). Structural genomics: keystone for a Human Proteome Project. Nature Structural Biology, 9(12), 973-974.
Lemerle, C., Di Ventura, B., et al. (2005). The temporal expression pattern of a generic network of synthetic transcriptional regulators. PLoS Biology, 3(9), e309.


Step 3.2
This output does make quite a lot of logical sense! Nothing is really out of the ordinary for an essay like this, and the references do exist and support the claims made. 