#!/usr/bin/env python3

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

WL_data = []
WL_pos = []

# show_only = [36,37,73,74,97,98,174,240,241,267,268,311,333,355,384,391,416,430,459,460,481,499,519,520,535,555,565,579,613,679,688,718,786,787,889,890,932,933]

# read in files
for counter in range(1,7):
    wl = []
    wl_pos = []
    to_sort = []
    file = open("../data_raw/WL_" + str(counter) + "_pos_per.txt", "r")
    for x in file:
        entry = x.strip().split()
        perc = float(entry[2])
        # if (int(entry[0])+1) in show_only:
        to_sort.append([int(entry[1]), perc])
    # sort data    
    to_sort.sort()
    for i in to_sort:
        wl.append(i[1])
        wl_pos.append(i[0])
    WL_data.append(wl)
    WL_pos.append(wl_pos)
    file.close()

new_data, WL_data1,WL_data2,WL_data3,WL_data4,WL_data5,WL_data6,position = [],[],[],[],[],[],[],[]

# show only those where WL_1 or WL_4 is >= 1
for i in range(0,len(WL_data[0])):
    if WL_data[0][i] >= 1 or WL_data[3][i] >= 1:
        WL_data1.append(WL_data[0][i])
        WL_data2.append(WL_data[1][i])
        WL_data3.append(WL_data[2][i])
        WL_data4.append(WL_data[3][i])
        WL_data5.append(WL_data[4][i])
        WL_data6.append(WL_data[5][i])
        position.append(WL_pos[0][i])

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

fig = plt.figure(figsize=(20, 10))
sns.heatmap(data_np, xticklabels=position,yticklabels=["WL_4","WL_1","WL_3","WL_2","WL_5","WL_6"],cmap=sns.color_palette("OrRd", as_cmap=True))
plt.title( "2-D Heat Map" )
plt.savefig("../results/Figure_4_v8.png")
