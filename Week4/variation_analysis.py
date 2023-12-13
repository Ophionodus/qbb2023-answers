#!/usr/bin/env python

import matplotlib.pyplot as plt




for line in open(annotatedvariants.vcf):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')

    # grab what you need from `fields`