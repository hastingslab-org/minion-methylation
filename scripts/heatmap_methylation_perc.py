#!/usr/bin/env python3

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

WL_data = []
WL_pos = []

show_only = [36,37,73,74,97,98,174,240,241,267,268,311,333,355,384,391,416,430,459,460,481,499,519,520,535,555,565,579,613,679,688,718,786,787,889,890,932,933]

# read in files
for counter in range(1,7):
    wl = []
    wl_pos = []
    file = open("./data/WL_" + str(counter) + "_pos_per.txt", "r")
    for x in file:
        entry = x.strip().split()
        perc = float(entry[1])/100
        if (int(entry[0])+1) in show_only:
            wl.append(perc)
            wl_pos.append(int(entry[0])+1)
    WL_data.append(wl)
    WL_pos.append(wl_pos)
    file.close()

data_np = np.array([WL_data[3],WL_data[0],WL_data[2],WL_data[1],WL_data[4],WL_data[5]])

data = np.random.randint(low=1,
                         high=100,
                         size=(10, 10))


sns.heatmap(data_np, xticklabels=WL_pos[0],yticklabels=["WL_4","WL_1","WL_3","WL_2","WL_5","WL_6"],cmap=sns.cubehelix_palette(as_cmap=True))
# sns.color_palette("flare", as_cmap=True)
plt.title( "2-D Heat Map" )
plt.show()
