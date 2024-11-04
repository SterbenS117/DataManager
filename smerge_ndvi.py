import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from natsort import natsorted
import os
import string

dates = ["20030401", "20030415", "20030429", "20030513", "20030527", "20030610","20030624","20030731","20030814","20030828","20030910","20031023",
             "20040401","20040415","20040430","20040514","20040528","20040617", "20040701","20040715","20040729","20040812","20040826","20040909",
             "20040923","20041007","20041021","20050401","20050415","20050429", "20050513","20050527","20050610","20050628","20050713","20050727",
             "20050822","20050905","20050920","20051004","20051018","20060401","20060415","20060707","20060806","20060826","20060909","20060923",
             "20061007","20061021","20070620","20070813"]

oi = [1]
for o in oi:
    input_dir = "/mnt/d/ARM/Era3/gis/"
    four = []
    seven = []
    ten = []
    fourteen = []
    for f in os.listdir(input_dir):
        print(f)
        if f.endswith("400.csv"):
            four.append(f)
        if f.endswith("700.csv"):
            seven.append(f)
        if f.endswith("1000.csv"):
            ten.append(f)
        if f.endswith("1400.csv"):
            fourteen.append(f)
    four = natsorted(four)
    seven = natsorted(seven)
    fourteen = natsorted(fourteen)
    ten = natsorted(ten)
    ndvi_fourteen = []
    smerge_fourteen = []
    for h in fourteen:
        if h.startswith('NDVI'):
            ndvi_fourteen.append(os.path.join(input_dir, h))
        if h.startswith('ARM'):
            smerge_fourteen.append(os.path.join(input_dir, h))
    for k in ndvi_fourteen:

        main = pd.read_csv(k).dropna(axis=1, how='all')
        print(main)
        if "3_1_" in k:
            era = "3_1"
        if "3_2_" in k:
            era = "3_2"
        if "3_3_" in k:
            era = "3_3"
        if "3_4_" in k:
            era = "3_4"
        ndvi_list = main.columns
        for g in ndvi_list:
            num = 1
            for d in dates:
                if d in g:
                    out = main[[g,'PageName']]
                    out.columns = ['MEAN','PageName']
                    out.to_csv("/mnt/d/ARM/Era3/Era"+era+"/ALL_Data"+"/NDVI_"+era+'-'+str(num)+"-1400.csv", index=False)
                num = num + 1
    for k in smerge_fourteen:
        main = pd.read_csv(k).dropna(axis=1, how='all')
        if "3_1_" in k:
            era = "3_1"
        if "3_2_" in k:
            era = "3_2"
        if "3_3_" in k:
            era = "3_3"
        if "3_4_" in k:
            era = "3_4"
        smerge_list = main.columns
        for g in smerge_list:
            num = 1
            for d in dates:
                if d in g:
                    out = main[[g,'PageName']]
                    out.columns = ['MEAN', 'PageName']
                    out.to_csv("/mnt/d/ARM/Era3/Era"+era+"/ALL_Data"+"/Smerge_"+era+'-'+str(num)+"-1400.csv", index=False)
                num = num + 1