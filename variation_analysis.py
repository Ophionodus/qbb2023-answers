#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = open("annotatedvariants.vcf")
depthss = []
qualities = []
frequencies = []
effect_types = []
for line in file:
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')

    splitfields = (fields[7].split(';'))
    splitfields_2 = (fields[9].split(':'))
    quality = splitfields_2[1]
    if quality !=".":
    	quality = float(quality)
    	qualities.append(quality)


    depths = splitfields[7]	


    depths = depths.replace('DP=', '')
    depths = depths.split(',')[0]
    depths = int(depths)
    depthss.append(depths)

    frequency = splitfields[3]
    frequency = frequency.replace('AF=', '')
    frequency = frequency.split(',')[0]
    frequency = float(frequency)
    frequencies.append(frequency)

    effect = splitfields[41]
    spliteffect = effect.split("|")
    effect_type = spliteffect[2]
    effect_types.append(effect_type)
count = pd.Series(effect_types).value_counts()

print(count.index)
print(count.values)

fig, ax = plt.subplots(2, 2)

ax[0,0].hist(np.log10(depthss), bins=100, label="log10(depth)")
ax[0,0].set(xlabel='log10(depth)', ylabel='frequency')

ax[0,1].hist((qualities), bins=100)
ax[0,1].set(xlabel='quality', ylabel='frequency')

ax[1,0].hist((frequencies), bins=10)
ax[1,0].set(xlabel='allele frequency', ylabel='frequency')

ax[1,1].bar(count.index, count.values)
ax[1,1].set(xlabel='effect type', ylabel='frequency')



plt.tight_layout()
plt.show()