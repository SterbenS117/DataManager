import os
#os.environ["MODIN_ENGINE"] = "dask"
import datetime
import pandas as pd
#import modin.pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import re
import string
import warnings
from natsort import natsorted
import sys
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
op = 4
if op == 1:
    data = pd.read_csv('/mnt/d/AriMoss/Grid_200_LAI_ALB.csv')
    col = data.columns
    home = '/mnt/d/AriMoss/200m/'
    for c in col:
        f_data = data[['PageName', c]]
        f_data.columns = ['PageName', 'MEAN']
        f_data.to_csv(home + c.replace('MEAN_','')+'.csv')
        print(f_data)
if op == 2:
    home = '/mnt/d/AriMoss/200m/'
    data = pd.read_csv('/mnt/d/AriMoss/Moisst_13_ALL_200.csv')
    static = data[['PageName','MEAN_Clay_pt','MEAN_Sand_pt', 'MEAN_Silt_pt_1', 'MEAN_Elevation_pt_1','MEAN_Slope_pt', 'MEAN_Aspect_C_pt']]
    static.columns = ['PageName','Clay','Sand','Silt','Elevation','Slope','Aspect']
    static.to_csv(home +'Static_200.csv', index=False)

date = ['20121024','20121027','20121030','20130617','20130716','20130719','20130723','20130927','20140416','20140418','20140424','20140708','20140711','20140715','20141014',
        '20141017','20141021','20150416','20150420','20150807','20150811','20150814']
if op == 3:
    input_dir = "/mnt/d/ARM/Era3/Static_1400/ERA3_4"
    fourteen = []
    seven = []
    ten = []
    for f in os.listdir(input_dir):
        print(f)
        if f.endswith("1400.csv"):
            fourteen.append(f)
    fourteen = natsorted(fourteen)
    seven = natsorted(seven)
    print(seven)
    ten = natsorted(ten)
#########################################################################################################################################
    index = pd.read_csv(os.path.join(input_dir,fourteen[0]), usecols=["PageName"])
    static_1400m = pd.DataFrame(index=index["PageName"])
    for f in fourteen:
        temp = pd.read_csv(os.path.join(input_dir,f)).set_index("PageName")
        static_1400m[f.split("_", 1)[0]] = temp['MEAN']
        print(f.split("_", 1)[0])
        static_1400m.to_csv(input_dir+"/ARM_Static_1400m.csv")
if op == 4:
    static_home = '/mnt/d/AriMOSS/200m/'
    input_dir = '/mnt/d/AriMOSS/200m/'
    two = []
    for f in os.listdir(input_dir):
        if f.endswith(".csv"):
            print(f)
            two.append(f)
    two = natsorted(two)
    alb_two = []
    lai_two = []
    lst_two = []
    ndvi_two = []
    smerge_two = []
    air_two = []
    for w in two:
        if w.startswith("ALB"):
            alb_two.append(os.path.join(input_dir, w))
        if w.startswith("LAI"):
            lai_two.append(os.path.join(input_dir, w))
        if w.startswith("Prism"):
            lst_two.append(os.path.join(input_dir, w))
        if w.startswith("NDVI"):
            ndvi_two.append(os.path.join(input_dir, w))
        if w.startswith("SMERGE"):
            smerge_two.append(os.path.join(input_dir, w))
        if w.startswith("Air"):
            print(w)
            air_two.append(os.path.join(input_dir, w))

    f_data = pd.DataFrame(
        columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope', 'Elevation',
                 'Aspect'])
    # r = 110000
    r = 106150  # 400m 16941
    static = pd.read_csv(static_home + "Static_200.csv")
    for k in range(1, 23):
        # print(lai_whole)
        current = pd.DataFrame(index=static["PageName"],
                               columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt',
                                        'Slope', 'Elevation', 'Aspect'])
        index = static["PageName"]
        current['SMERGE'] = pd.read_csv(smerge_two[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        # lst_temp = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).dropna()
        # print(static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept','PageName']].set_index("PageName"))
        print(lst_two[k - 1])
        current['Temp'] = pd.read_csv(lst_two[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["LAI"] = pd.read_csv(lai_two[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current['Temp'] = pd.read_csv(lst_two[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["Albedo"] = pd.read_csv(alb_two[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["NDVI"] = pd.read_csv(ndvi_two[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current['Air'] = pd.read_csv(air_two[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current[['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Aspect']] = static[
            ['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Aspect', 'PageName']].set_index("PageName")
        current['PageName'] = current.index
        current.index = range(current.shape[0])
        current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
        f_data = pd.concat([f_data, current])
        if k == 22:
            f_data.to_csv('Air_200m_dataV1.csv')
            op = 5
if op == 5:
    data = pd.read_csv('Air_200m_dataV1.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Aspect'] > 0)]
    data1 = data1[ ~(data1[["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Aspect"]] < 0).any(axis=1)]
    data1 = data1.dropna()
    data1.to_csv('Air_200m_dataV1_p.csv', index=False)
    df_train, df_test = train_test_split(data1, test_size=0.30, random_state=42)
    df_train.to_csv('Air_200m_dataV1_train.csv', index=False)
    df_test.to_csv('Air_200m_dataV1_test.csv', index=False)
