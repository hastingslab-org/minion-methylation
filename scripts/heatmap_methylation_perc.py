#!/usr/bin/env python3

import numpy as np
import pandas as pd
import seaborn as sns
from Bio import SeqIO

import matplotlib.pyplot as plt

def rc(seq):
    rc_seq = ''
    for i in seq:
        if i == 'A':
            rc_seq += 'T'
        elif i == 'C':
            rc_seq += 'G'
        elif i == 'G':
            rc_seq += 'C'
        elif i == 'T':
            rc_seq += 'A'
        else:
            rc_seq += 'N'
    return rc_seq[::-1]

WL_data = []
WL_pos = []
WL_ori = []
ref_genome = '../data_raw/reference_genome/genome_weina.fa'

# show_only = [36,37,73,74,97,98,174,240,241,267,268,311,333,355,384,391,416,430,459,460,481,499,519,520,535,555,565,579,613,679,688,718,786,787,889,890,932,933]

fasta_sequences = SeqIO.parse(open(ref_genome),'fasta')
for seq in fasta_sequences:
    ref_seq = seq.seq
    # print(seq.id)

# read in files
for counter in range(1,7):
    wl = []
    wl_pos = []
    wl_ori = []
    to_sort = []
    file = open("../data_raw/WL_" + str(counter) + "_pos_per.txt", "r")
    for x in file:
        entry = x.strip().split()
        perc = float(entry[3])
        orientation = entry[2]
        # if (int(entry[0])+1) in show_only:
        to_sort.append([int(entry[1]), perc, orientation])
    # sort data    
    to_sort.sort()
    for i in to_sort:
        wl.append(i[1])
        wl_pos.append(i[0])
        wl_ori.append(i[2])
    WL_data.append(wl)
    WL_pos.append(wl_pos)
    WL_ori.append(wl_ori)
    file.close()

new_data, WL_data1,WL_data2,WL_data3,WL_data4,WL_data5,WL_data6,position = [],[],[],[],[],[],[],[]

# show only those where WL_1 or WL_4 is >= 1
x_labels_more = []
for i in range(0,len(WL_data[0])):
    if WL_data[0][i] >= 1 or WL_data[3][i] >= 1:
        WL_data1.append(WL_data[0][i])
        WL_data2.append(WL_data[1][i])
        WL_data3.append(WL_data[2][i])
        WL_data4.append(WL_data[3][i])
        WL_data5.append(WL_data[4][i])
        WL_data6.append(WL_data[5][i])
        position.append(WL_pos[0][i])
        j = WL_pos[0][i]
        if WL_ori[0][i] == '+':
            label = str(ref_seq[j-6:j-1]) + "$\\bf{" + str(ref_seq[j-1]) +  "}$" + str(ref_seq[j:j+5])
        else:
            label = str(rc(ref_seq[j:j+5])) + "$\\bf{" + str(rc(ref_seq[j-1])) + "}$" + str(rc(ref_seq[j-6:j-1]))
        x_labels_more.append(str(j) + " " + str(WL_ori[0][i]) + " " + label)

# only show those where at least one entry is non-zero
# for i in range(0,len(WL_data[0])):
#     new = [WL_data[0][i],WL_data[1][i],WL_data[2][i],WL_data[3][i],WL_data[4][i],WL_data[5][i]]
#     if not all(j == 0 for j in new):
#         WL_data1.append(WL_data[0][i])
#         WL_data2.append(WL_data[1][i])
#         WL_data3.append(WL_data[2][i])
#         WL_data4.append(WL_data[3][i])
#         WL_data5.append(WL_data[4][i])
#         WL_data6.append(WL_data[5][i])
#         position.append(WL_pos[0][i])

data_np = np.array([WL_data4,WL_data1,WL_data2,WL_data3,WL_data5,WL_data6])


fig = plt.figure(figsize=(12, 10))
plt.rcParams['font.family'] = 'monospace'
sns.heatmap(data_np, xticklabels=x_labels_more,yticklabels=["4","1","3","2","5","6"],cmap=sns.color_palette("OrRd", as_cmap=True))
plt.title( "Methylation percentage" )
plt.tight_layout()
plt.savefig("../results/Figure_4_v10.png")
