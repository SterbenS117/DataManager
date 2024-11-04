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

k = 16

date_in =["20120421","20120601","20120608","20120615","20120628","20120705","20120712","20120719","20120726","20120802","20120817","20120824","20120831","20120907","20120922",
           "20120929","20121006","20121013","20121020","20121030","20121106","20121113","20121120","20121126","20130407","20130414","20130421","20130428","20130505","20130512",
           "20130519","20130530","20130606","20130613","20130626","20130703","20130710","20130717","20130724","20130801","20130810","20131006","20131013","20131020","20131110",
           "20131117","20131124","20141027","20150401","20150408","20150415","20150422","20150429","20150506","20150513","20150520","20150527","20150603","20150610","20150617",
           "20150624","20150701","20150708","20150715","20150722","20150729","20150805","20150812","20150819","20150826","20150902","20150909","20150916","20150923","20150930",
           "20151007","20151014","20151021","20151028"] #SoilScape Index
date = ['4/21/2012','6/1/2012','6/8/2012','6/15/2012','6/28/2012','7/5/2012','7/12/2012','7/19/2012','7/26/2012','8/2/2012','8/17/2012','8/24/2012',
    '8/31/2012','9/7/2012','9/22/2012','9/29/2012','10/6/2012','10/13/2012','10/20/2012','10/30/2012','11/6/2012','11/13/2012','11/20/2012','11/26/2012',
    '4/7/2013','4/14/2013','4/21/2013','4/28/2013','5/5/2013','5/12/2013','5/19/2013','5/30/2013','6/6/2013','6/13/2013','6/26/2013','7/3/2013',
    '7/10/2013','7/17/2013','7/24/2013','8/1/2013','8/10/2013','10/6/2013','10/13/2013','10/20/2013','11/10/2013','11/17/2013','11/24/2013','10/27/2014',
    '4/1/2015','4/8/2015','4/15/2015','4/22/2015','4/29/2015','5/6/2015','5/13/2015','5/20/2015','5/27/2015','6/3/2015','6/10/2015','6/17/2015',
    '6/24/2015','7/1/2015','7/8/2015','7/15/2015','7/22/2015','7/29/2015','8/5/2015','8/12/2015','8/19/2015','8/26/2015','9/2/2015','9/9/2015',
    '9/16/2015','9/23/2015','9/30/2015','10/7/2015','10/14/2015','10/21/2015','10/28/2015'] #SoilScape
if k == 16:
    three = []
    ten = []
    input_dir = '/mnt/d/Soilscape/NewFolder(2)'
    for f in os.listdir(input_dir):
        if f.endswith('.csv'):
            if ("_30m_" in f):
                three.append(f)
            if ("_100m_" in f):
                ten.append(f)
    # data_n = 'GBR_v4_ARM_ERA31_700m.csv'
    # data_out = 'GBR_v4_ARM_ERA31_700mInst.csv'
    qc_dir = '/mnt/d/Soilscape/NewFolder(2)/smerge_QC'
    for data_n in three:
        data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
        data['Smerge_QC'] = np.nan
        i = 0
        for d in date_in:
            qc = pd.read_csv(qc_dir + '/' + 'SmergeQCSoil_' + d + '_Soil_Scape_Coordina_30m.csv').set_index("PageName")
            data.loc[data['Date'] == date[i], ['Smerge_QC']] = qc['MEAN']
            i = i + 1
        data.to_csv(input_dir + '/' + data_n.replace('.csv', 'smergeQC.csv'))
    for data_n in ten:
        data = pd.read_csv(input_dir + '/' + data_n).set_index("PageName")
        data['Smerge_QC'] = np.nan
        i = 0
        for d in date_in:
            qc = pd.read_csv(qc_dir + '/' + 'SmergeQCSoil_' + d + '_Soil_Scape_100m.csv').set_index("PageName")
            data.loc[data['Date'] == date[i], ['Smerge_QC']] = qc['MEAN']
            i = i + 1
        data.to_csv(input_dir + '/' + data_n.replace('.csv', 'smergeQC.csv'))
