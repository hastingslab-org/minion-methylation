#!/bin/bash

awk -F ' ' '{print $2,$3,$6,$11}' ../data_raw/WL_1/modified_bases.re_aggregated.5mC.bed > ../data_raw/WL_1_pos_per.txt
awk -F ' ' '{print $2,$3,$6,$11}' ../data_raw/WL_2/modified_bases.re_aggregated.5mC.bed > ../data_raw/WL_2_pos_per.txt
awk -F ' ' '{print $2,$3,$6,$11}' ../data_raw/WL_3/modified_bases.re_aggregated.5mC.bed > ../data_raw/WL_3_pos_per.txt
awk -F ' ' '{print $2,$3,$6,$11}' ../data_raw/WL_4/modified_bases.re_aggregated.5mC.bed > ../data_raw/WL_4_pos_per.txt
awk -F ' ' '{print $2,$3,$6,$11}' ../data_raw/WL_5/modified_bases.re_aggregated.5mC.bed > ../data_raw/WL_5_pos_per.txt
awk -F ' ' '{print $2,$3,$6,$11}' ../data_raw/WL_6/modified_bases.re_aggregated.5mC.bed > ../data_raw/WL_6_pos_per.txt

python3 heatmap_methylation_perc.py