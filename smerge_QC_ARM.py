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

qc_dir = '/mnt/d/AriMoss/smerge_QC'

four = []
seven = []
ten = []
fourteen = []
input_dir = '/mnt/e/Smerge_QC_main/Smerge_QC_Tables/ARM_1'
for f in os.listdir(input_dir):
    if f.endswith('.csv') and 'ARM_1_2' in f:
        if ("__400" in f):
            four.append(f)
        if ("__700" in f):
            seven.append(f)
        if ("__1000" in f):
            ten.append(f)
        if ("__1400" in f):
            fourteen.append(f)
int_percent = 0.0
i = 0
m = 0.0
for data_n in four:
    data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
    i = i + 1
    # print(data_n)
    # print(data.dtypes)
    # inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
    n = data.loc[data['MEAN'] < 1.0, ['MEAN']].shape[0]
    m = m + float(data.shape[0])
    int_percent = n + int_percent
    print(data_n + ":   " + str(n / data.shape[0]))
total_percent = (int_percent / m) * 100
print('400m percent interpolated is ' + str(total_percent))

int_percent = 0.0
i = 0
m = 0.0
for data_n in seven:
    data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
    i = i + 1
    # print(data_n)
    # print(data.dtypes)
    # inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
    n = data.loc[data['MEAN'] < 1.0, ['MEAN']].shape[0]
    m = m + float(data.shape[0])
    int_percent = n + int_percent
    print(data_n + ":   " + str(n / data.shape[0]))
total_percent = (int_percent / m) * 100
print('700m percent interpolated is ' + str(total_percent))

int_percent = 0.0
i = 0
m = 0.0
for data_n in ten:
    data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
    i = i + 1
    # print(data_n)
    # print(data.dtypes)
    # inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
    n = data.loc[data['MEAN'] < 1.0, ['MEAN']].shape[0]
    m = m + float(data.shape[0])
    int_percent = n + int_percent
    print(data_n + ":   " + str(n / data.shape[0]))
total_percent = (int_percent / m) * 100
print('1000m percent interpolated is ' + str(total_percent))

int_percent = 0.0
i = 0
m = 0.0
for data_n in fourteen:
    data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
    i = i + 1
    # print(data_n)
    # print(data.dtypes)
    # inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
    n = data.loc[data['MEAN'] < 1.0, ['MEAN']].shape[0]
    m = m + float(data.shape[0])
    int_percent = n + int_percent
    print(data_n + ":   " + str(n / data.shape[0]))
total_percent = (int_percent / m) * 100
print('1400m percent interpolated is ' + str(total_percent))