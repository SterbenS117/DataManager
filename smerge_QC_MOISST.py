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
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

date = ['10/24/2012','10/27/2012','10/30/2012','06/17/2013','07/16/2013','07/19/2013','07/23/2013','09/27/2013','04/16/2014','04/18/2014','04/24/2014','07/08/2014','07/11/2014',
        '07/15/2014','10/14/2014','10/17/2014','10/21/2014','04/16/2015','04/20/2015','08/07/2015','08/11/2015','08/14/2015']
date_in = [20121024,20121027,20121030,20130617,20130716,20130719,20130723,20130927,20140416,20140418,20140424,20140708,20140711,20140715,20141014,
        20141017,20141021,20150416,20150420,20150807,20150811,20150814]

k = 16

if k == 16:
    four = []
    seven = []
    ten = []
    fourteen = []
    twenty = []
    thirty = []
    input_dir = '/mnt/d/AriMoss'
    for f in os.listdir(input_dir):
        if f.endswith('.csv'):
            if ("_400m_" in f):
                four.append(f)
            if ("_700m_" in f):
                seven.append(f)
            if ("_1000m_" in f):
                ten.append(f)
            if ("_1400m_" in f):
                fourteen.append(f)
            if ("_2000m_" in f):
                twenty.append(f)
            if ("_3000m_" in f):
                thirty.append(f)
    # data_n = 'GBR_v4_ARM_ERA31_700m.csv'
    # data_out = 'GBR_v4_ARM_ERA31_700mInst.csv'
    qc_dir = '/mnt/d/AriMoss/smerge_QC'

    for data_n in four:
        data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
        data['Smerge_QC'] = np.nan
        i = 0
        for d in date_in:
            qc = pd.read_csv(qc_dir + '/' + 'SmergeQC_Air_' + str(d) + '_400.csv').set_index("PageName")
            g = qc.loc[qc.index.duplicated() == True]
            print(d)
            data.loc[data['Date'] == d, ['Smerge_QC']] = qc['MEAN']

            i = i + 1
        data.to_csv(input_dir + '/' + data_n.replace('.csv', 'smergeQC.csv'))
    for data_n in seven:
        data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
        data['Smerge_QC'] = np.nan
        i = 0
        for d in date_in:
            qc = pd.read_csv(qc_dir + '/' + 'SmergeQC_Air_' + str(d) + '_700.csv').set_index("PageName")
            data.loc[data['Date'] == d, ['Smerge_QC']] = qc['MEAN']
            i = i + 1
        data.to_csv(input_dir + '/' + data_n.replace('.csv', 'smergeQC.csv'))
    for data_n in ten:
        data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
        data['Smerge_QC'] = np.nan
        i = 0
        for d in date_in:
            qc = pd.read_csv(qc_dir + '/' + 'SmergeQC_Air_' + str(d) + '_1000.csv').set_index("PageName")
            data.loc[data['Date'] == d, ['Smerge_QC']] = qc['MEAN']
            i = i + 1
        data.to_csv(input_dir + '/' + data_n.replace('.csv', 'smergeQC.csv'))
    for data_n in fourteen:
        data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
        data['Smerge_QC'] = np.nan
        i = 0
        for d in date_in:
            qc = pd.read_csv(qc_dir + '/' + 'SmergeQC_Air_' + str(d) + '_1400.csv').set_index("PageName")
            data.loc[data['Date'] == d, ['Smerge_QC']] = qc['MEAN']
            i = i + 1
        data.to_csv(input_dir + '/' + data_n.replace('.csv', 'smergeQC.csv'))
    for data_n in twenty:
        data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
        data['Smerge_QC'] = np.nan
        i = 0
        for d in date_in:
            qc = pd.read_csv(qc_dir + '/' + 'SmergeQC_Air_' + str(d) + '_2000.csv').set_index("PageName")
            data.loc[data['Date'] == d, ['Smerge_QC']] = qc['MEAN']
            i = i + 1
        data.to_csv(input_dir + '/' + data_n.replace('.csv', 'smergeQC.csv'))
    for data_n in thirty:
        data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
        data['Smerge_QC'] = np.nan
        i = 0
        for d in date_in:
            qc = pd.read_csv(qc_dir + '/' + 'SmergeQC_Air_' + str(d) + '_3000.csv').set_index("PageName")
            g = data.loc[data.index.duplicated() == True]
            #print(g['Date'] == d)
            data.loc[data['Date'] == d, ['Smerge_QC']] = qc['MEAN']
            i = i + 1
        data.to_csv(input_dir + '/' + data_n.replace('.csv', 'smergeQC.csv'))
