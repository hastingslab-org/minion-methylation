#!/usr/bin/env python3

import numpy as np
import pandas as pd
import seaborn as sns
from Bio import SeqIO

import matplotlib.pyplot as plt

ref_genome = '../data_raw/reference_genome/genome_weina.fa'

# read in files
WL_data = []
for counter in [1,4]:
    data = []
    file = open("../data_raw/WL_" + str(counter) + "_pos_per.txt", "r")
    for x in file:
        entry = x.strip().split()
        perc = float(entry[3])
        orientation = entry[2]
        data.append([int(entry[1]), perc, orientation])
    WL_data.append(data)

fasta_sequences = SeqIO.parse(open(ref_genome),'fasta')
for seq in fasta_sequences:
    ref_seq = seq.seq

number_of_Cs = ref_seq.count("C")
number_of_Gs = ref_seq.count("G")

for data in WL_data:
    counter = 0
    total_plus = 0
    total_minus = 0
    for entry in data:
        if entry[2] == '+':
            if ref_seq[entry[0] - 1] == 'C':
                total_plus += entry[1]
        else:
            if ref_seq[entry[0] - 1] == 'G':
                total_minus += entry[1]

    print('plus:', total_plus/number_of_Cs)      
    print('minus: ', total_minus/number_of_Gs) 

    print(number_of_Cs)
    print(number_of_Gs)
