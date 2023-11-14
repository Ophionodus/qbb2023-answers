#!/bin/bash

#bwa index sacCer3.fa 

# for sample in {A01_09.fastq A01_11.fastq A01_23.fastq A01_24.fastq A01_27.fastq A01_31.fastq A01_35.fastq A01_39.fastq A01_62.fastq A01_63.fastq
# do
# 	echo "Aligning sample:" ${sample}
# 	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" sacCer3.fa ${sample} > ${sample}.sam
# 	samtools sort ${sample}.sam > ${sample}.bam
# 	samtools index ${sample}.bam
# done

#freebayes -f sacCer3.fa --genotype-qualities -p 1 -L filenames.txt >variants.vcf

#vcffilter -f "QUAL > 99" variants.vcf >filteredvariants.vcf

#vcfallelicprimitives -k -g filteredvariants.vcf >primitivevariants.vcf



#snpEff ann R64-1-1.105 primitivevariants.vcf >annotatedvariants.vcf

head -100 annotatedvariants.vcf >first100ofannotatedvariants.vcf