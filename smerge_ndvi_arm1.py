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

dates = ['20160401','20160421','20160505','20160524','20160715','20160729','20160812','20160826','20160909','20160923','20161007','20161021','20170401','20170415',
         '20170429','20170513','20170527','20170610','20170624','20170708','20170722','20170805','20170819','20170902','20170916','20170930','20171014','20171028',
         '20180401','20180415','20180429','20180513','20180527','20180610','20180624','20180708','20180722','20180805','20180819','20180902','20180916','20180930',
         '20181014','20181028','20190401','20190415','20190429']
doys =['NDVI_2016_122','NDVI__2016_142','NDVI_2016_156','NDVI__2016_175','NDVI__2016_227','NDVI__2016_241','NDVI__2016_255','NDVI__2016_269','NDVI__2016_283',
       'NDVI__2016_297','NDVI__2016_311','NDVI__2016_325','NDVI__2017_121','NDVI__2017_135','NDVI__2017_149','NDVI__2017_163','NDVI__2017_177','NDVI__2017_191',
       'NDVI__2017_205','NDVI__2017_219','NDVI_2017_233','NDVI__2017_247','NDVI__2017_261','NDVI__2017_275','NDVI__2017_289','NDVI__2017_303','NDVI__2017_317',
       'NDVI__2017_331','NDVI__2018_121','NDVI__2018_135','NDVI__2018_149','NDVI__2018_163','NDVI__2018_177','NDVI__2018_191','NDVI__2018_205','NDVI__2018_219',
       'NDVI__2018_233','NDVI__2018_247','NDVI__2018_261','NDVI__2018_275','NDVI__2018_289','NDVI__2018_303','NDVI__2018_317','NDVI__2018_331','NDVI__2019_121',
       'NDVI__2019_135','NDVI__2019_149']
# date = ["4/1/2016","4/21/2016","5/5/2016","5/24/2016","7/15/2016","7/29/2016","8/12/2016","8/26/2016","9/9/2016","9/23/2016","10/7/2016","10/21/2016",
#         "4/1/2017","4/15/2017","4/29/2017","5/13/2017","5/27/2017","6/10/2017","6/24/2017","7/8/2017","7/22/2017","8/5/2017","8/19/2017","9/2/2017",
#         "9/16/2017","9/30/2017","10/14/2017","10/28/2017","4/1/2018","4/15/2018","4/29/2018","5/13/2018","5/27/2018","6/10/2018","6/24/2018","7/8/2018",
#         "7/22/2018","8/5/2018","8/19/2018","9/2/2018","9/16/2018","9/30/2018","10/14/2018","10/28/2018","4/1/2019","4/15/2019","4/29/2019"] #era1
oi = [1]
for o in oi:
    input_dir = "/mnt/d/ARM/Era1/gis/"
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
        #print(k)
        if "1_1_" in k:
            era = "1_1"
        if "1_2_" in k:
            era = "1_2"
        ndvi_list = main.columns
        for g in ndvi_list:
            num = 1
            #print(g)
            for d in doys:
                if d in g:
                    out = main[[g,'PageName']]
                    out.columns = ['MEAN','PageName']
                    #print(d)
                    out.to_csv("/mnt/d/ARM/Era1/Era"+era+"/ALL_Data"+"/NDVI_"+era+'-'+d+"-1400.csv", index=False)
                num = num + 1
    for k in smerge_fourteen:
        main = pd.read_csv(k).dropna(axis=1, how='all')
        if "1_1_" in k:
            era = "1_1"
        if "1_2_" in k:
            era = "1_2"
        smerge_list = main.columns
        for g in smerge_list:
            num = 1
            for d in dates:
                if d in g:
                    out = main[[g,'PageName']]
                    out.columns = ['MEAN', 'PageName']
                    #print(d)
                    out.to_csv("/mnt/d/ARM/Era1/Era"+era+"/ALL_Data"+"/Smerge_"+era+'-'+d+"-1400.csv", index=False)
                num = num + 1