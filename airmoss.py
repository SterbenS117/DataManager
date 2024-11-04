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
import sys
sys.setrecursionlimit(999999999)
#warnings.filterwarnings('ignore')
k = 11
index2 = (['20121024','20121027','20121030','20130617','20130716','20130719','20130723','20130927','20140416','20140418','20140424','20140708','20140711','20140715','20141014','20141017','20141021','20150416','20150420','20150807','20150811','20150814'])
index3 = (["20120421","20120601","20120608","20120615","20120628","20120705","20120712","20120719","20120726","20120802","20120817","20120824","20120831","20120907","20120922",
           "20120929","20121006","20121013","20121020","20121030","20121106","20121113","20121120","20121126","20130407","20130414","20130421","20130428","20130505","20130512",
           "20130519","20130530","20130606","20130613","20130626","20130703","20130710","20130717","20130724","20130801","20130810","20131006","20131013","20131020","20131110",
           "20131117","20131124","20141027","20150401","20150408","20150415","20150422","20150429","20150506","20150513","20150520","20150527","20150603","20150610","20150617",
           "20150624","20150701","20150708","20150715","20150722","20150729","20150805","20150812","20150819","20150826","20150902","20150909","20150916","20150923","20150930",
           "20151007","20151014","20151021","20151028"])
if k == 11:
    i = 0
    lst_home = '/mnt/d/Soilscape/NewFolder(2)/LST_Tables/'
    names = ['SSv2_30m_dataV3_train.csv','SSv2_30m_dataV3_test.csv','SSv2_100m_dataV3_train.csv','SSv2_100m_dataV3_test.csv']
    reso = ['30m','30m', '100m','100m']
    for n in names:
        data = pd.read_csv(n, usecols=["SMERGE","Date","PageName","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept"]).set_index("PageName")
        data["LST"] = np.NAN
        data.sort_index()
        data.sort_values(by=["Date"])
        for p in index3:
            lst_c = pd.read_csv(lst_home+reso[i]+"/Prism_"+p+"_Soil_Scape_"+reso[i]+".csv", usecols=["MEAN","PageName"]).set_index("PageName")
            q = pd.to_datetime(p, format='%Y%m%d')
            data['Date2'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
            print(q)
            #print(data[data['Date'] == int(p)]['LST'])
            print(lst_c["MEAN"])
            data.loc[data['Date2'] == q,'Temp'] = lst_c["MEAN"]
            print(data[data['Date2'] == q]['Temp'])
        # data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]

        data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
        data1 = data1[~(data1[["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt ", "Slope", "Elevation", "Ascept"]] < 0).any(
                axis=1)]
        #data1 = data1.dropna(subset=["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt ", "Slope", "Elevation", "Ascept","LST"])
        data1 = data1.drop(columns='Date2')
        try:
            print(data1.columns)
            print('data1 = data1.drop([LST])')
            data1 = data1.drop(columns='LST')
        except Exception as e:
            print(e)
        data1.columns = ["SMERGE","Date","LAI","Albedo","NDVI","Clay","Sand","Silt","Slope","Elevation","Ascept","Temp"]

        data1.to_csv(n.replace("V3","V5"), index=True)
        i = i + 1
if k == 12:
    i = 0
    lst_home = '/mnt/d/AriMoss/LST_Tables/'
    names = ['A2_400m_processed__train.csv','A2_400m_processed__test.csv','A2_700m_processed__train.csv','A2_700m_processed__test.csv','A2_1000m_processed__train.csv','A2_1000m_processed__test.csv',
             'A2_1400m_processed__train.csv','A2_1400m_processed__test.csv','A2_2000m_processed__train.csv','A2_2000m_processed__test.csv','A2_3000m_processed__train.csv','A2_3000m_processed__test.csv',]
    lst = ['LST_400.csv','LST_400.csv','LST_700.csv','LST_700.csv','LST_1000.csv','LST_1000.csv','LST_1400.csv','LST_1400.csv','LST_2000.csv','LST_2000.csv','LST_3000.csv','LST_3000.csv']
    reso = ['400','400', '700','700', '1000','1000', '1400','1400', '2000','2000','3000','3000']
    for n in names:
        data = pd.read_csv(n, usecols=["PageName","Clay","Sand","Silt ","Elevation","Slope","Ascept","NDVI","Smerge","Air","Date","Lai","Albedo","Water"]).set_index("PageName")
        data.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Slope', 'Ascept', 'NDVI','Smerge', 'Air', 'Date', 'Lai', 'Albedo', 'Water']
        print(data.columns)
        data["Temp"] = np.NAN
        data.sort_index()
        data.sort_values(by=["Date"])
        for p in index2:
            lst_c = pd.read_csv(lst_home+reso[i]+"/Prism_"+p+"_"+reso[i]+".csv", usecols=["MEAN","PageName"]).set_index("PageName")
            #print(data[data['Date'] == int(p)]['LST'])
            print(lst_c["MEAN"])
            data.loc[data['Date'] == int(p),'Temp'] = lst_c["MEAN"]
            print(data[data['Date'] == int(p)]['Temp'])
        # data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]

        data1 = data[(data['Lai'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0) & (data['Water'] < 0.25)]
        data1 = data1[~(data1[["Lai", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Ascept"]] < 0).any(
                axis=1)]
        data1 = data1.dropna(subset=["Lai", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Ascept","Temp"])
        print(n)
        data1 = data1.drop(columns='Water')
        data1.columns = ["Clay","Sand","Silt","Elevation","Slope","Ascept","NDVI","SMERGE","Air","Date","LAI","Albedo","Temp"]
        data1.to_csv(n.replace("A2","A4"), index=True)
        i = i + 1



if k == 7:
    static = pd.read_csv('700m_static.csv')
    smerge = pd.read_csv('700m_smerge_m.csv')
    ndvi = pd.read_csv('700m_ndvi.csv')
    air_m = pd.read_csv('700m_air_m.csv')
    air_sd = pd.read_csv('700m_air_sd.csv')
    static.columns = [col.replace('MEAN_','') for col in static.columns]
    ndvi.columns = [col.replace('MEAN_', '') for col in ndvi.columns]
    air_m.columns = [col.replace('MEAN_', '') for col in air_m.columns]
    air_sd.columns = [col.replace('SD_', '') for col in air_sd.columns]
    smerge.columns = [col.replace('MEAN_', '') for col in smerge.columns]
    print(static.columns)
    print(smerge.columns)
    print(ndvi.columns)
    print(air_m.columns)
    print(air_sd.columns)
    static.to_csv('700m_static1.csv',index=False)
    smerge.to_csv('700m_smerge2_m1.csv', index=False)
    ndvi.to_csv('700m_ndvi1.csv', index=False)
    air_m.columns = ['OBJECTID', 'OID_', 'PageName', 'PageNumber', 'COUNT', 'C_Air_2012_1a',
                      'C_Air_2012_2a', 'C_Air_2012_3a', 'C_Air_2013_0a', 'C_Air_2013_1a', 'C_Air_2013_2a',
                      'C_Air_2013_3a', 'C_Air_2013_4a', 'C_Air_2014_0a', 'C_Air_2014_1a', 'C_Air_2014_2a',
                      'C_Air_2014_3a', 'C_Air_2014_4a', 'C_Air_2014_5a', 'C_Air_2014_6a', 'C_Air_2014_7a',
                      'C_Air_2014_8a', 'C_Air_2015_0a', 'C_Air_2015_1a', 'C_Air_2015_2a', 'C_Air_2015_3a',
                      'C_Air_2015_4a', 'SHAPE_Leng', 'SHAPE_Area']
    air_m.to_csv('700m_air_m1.csv', index=False)
    air_sd.columns = ['OBJECTID', 'OID_', 'PageName', 'PageNumber', 'COUNT', 'C_Air_2012_1a',
       'C_Air_2012_2a', 'C_Air_2012_3a', 'C_Air_2013_0a', 'C_Air_2013_1a','C_Air_2013_2a',
        'C_Air_2013_3a', 'C_Air_2013_4a', 'C_Air_2014_0a','C_Air_2014_1a', 'C_Air_2014_2a',
        'C_Air_2014_3a', 'C_Air_2014_4a','C_Air_2014_5a', 'C_Air_2014_6a', 'C_Air_2014_7a',
        'C_Air_2014_8a','C_Air_2015_0a', 'C_Air_2015_1a', 'C_Air_2015_2a', 'C_Air_2015_3a',
       'C_Air_2015_4a','SHAPE_Leng', 'SHAPE_Area']
    air_sd.to_csv('700m_air_sd1.csv', index=False)

if k == 111:
    out_full = pd.DataFrame(columns=['Clay', 'Elevation', 'Sand', 'Silt ', 'Slope', 'Ascept', 'NDVI', 'Smerge', 'Air','Date'])
    a = ['OBJECTID', 'PageName', 'PageNumber', 'ORIG_FID', 'Clay_pt',
         'Elevation_', 'Sand_pt', 'Silt_pt_1', 'Slope_pt', 'Ascept_pt',
         'NDVI_2012_', 'NDVI_2013_', 'NDVI_20131', 'NDVI_20132', 'NDVI_2014_',
         'NDVI_20141', 'NDVI_20142', 'NDVI_2015_', 'NDVI_20151', 'SMERGE_201',
         'SMERGE_202', 'SMERGE_203', 'SMERGE_204', 'SMERGE_205', 'SMERGE_206',
         'SMERGE_207', 'SMERGE_208', 'SMERGE_209', 'SMERGE_210', 'SMERGE_211',
         'SMERGE_212', 'SMERGE_213', 'SMERGE_214', 'SMERGE_215', 'SMERGE_216',
         'SMERGE_217', 'SMERGE_218', 'SMERGE_219', 'SMERGE_220', 'SMERGE_221',
         'SMERGE_222', 'Air_2012_1', 'Air_2012_2', 'Air_2012_3', 'Air_2013_0',
         'Air_2013_1', 'Air_2013_2', 'Air_2013_3', 'Air_2013_4', 'Air_2014_0',
         'Air_2014_1', 'Air_2014_2', 'Air_2014_3', 'Air_2014_4', 'Air_2014_5',
         'Air_2014_6', 'Air_2014_7', 'Air_2014_8', 'Air_2015_0', 'Air_2015_1',
         'Air_2015_2', 'Air_2015_3', 'Air_2015_4']
    air_i = ['C_Air_2012_1a',
       'C_Air_2012_2a', 'C_Air_2012_3a', 'C_Air_2013_0a', 'C_Air_2013_1a',
       'C_Air_2013_2a', 'C_Air_2013_3a', 'C_Air_2013_4a', 'C_Air_2014_0a',
       'C_Air_2014_1a', 'C_Air_2014_2a', 'C_Air_2014_3a', 'C_Air_2014_4a',
       'C_Air_2014_5a', 'C_Air_2014_6a', 'C_Air_2014_7a', 'C_Air_2014_8a',
       'C_Air_2015_0a', 'C_Air_2015_1a', 'C_Air_2015_2a', 'C_Air_2015_3a',
       'C_Air_2015_4a']
    smerge = ['SMERGE_2012_1024_Clip', 'SMERGE_2012_1027','SMERGE_2012_1030', 'SMERGE_2013_0617','SMERGE_2013_0716', 'SMERGE_2013_0719','SMERGE_2013_0723', 'SMERGE_2013_0927','SMERGE_2014_0416', 'SMERGE_2014_0418',
       'SMERGE_2014_0424', 'SMERGE_2014_0708','SMERGE_2014_0711', 'SMERGE_2014_0715','SMERGE_2014_1014', 'SMERGE_2014_1017','SMERGE_2014_1021', 'SMERGE_2015_0416',
       'SMERGE_2015_0420', 'SMERGE_2015_0807','SMERGE_2015_0811', 'SMERGE_2015_0814']
    # smerge = ['MEAN_SMERG',
    #    'MEAN_SME_1', 'MEAN_SME_2', 'MEAN_SME_3', 'MEAN_SME_4', 'MEAN_SME_5',
    #    'MEAN_SME_6', 'MEAN_SME_7', 'MEAN_SME_8', 'MEAN_SME_9', 'MEAN_SM_10',
    #    'MEAN_SM_11', 'MEAN_SM_12', 'MEAN_SM_13', 'MEAN_SM_14', 'MEAN_SM_15',
    #    'MEAN_SM_16', 'MEAN_SM_17', 'MEAN_SM_18', 'MEAN_SM_19', 'MEAN_SM_20',
    #    'MEAN_SM_21']
    ndvi = ['NDVI_2012_332_', 'NDVI_2012_332_', 'NDVI_2012_332_', 'NDVI_2013_197', 'NDVI_2013_225',
            'NDVI_2013_225', 'NDVI_2013_225', 'NDVI_2013_295', 'NDVI_2014_140', 'NDVI_2014_140',
            'NDVI_2014_140', 'NDVI_2014_217', 'NDVI_2014_217', 'NDVI_2014_217', 'NDVI_2014_315',
            'NDVI_2014_315', 'NDVI_2014_315', 'NDVI_2015_132', 'NDVI_2015_132', 'NDVI_2015_251', 'NDVI_2015_251', 'NDVI_2015_251']

    csv_path1 = 'Static.csv'
    # air_df = pd.read_csv('AirMOSS1.csv', index_col=False)
    # air_sd = pd.read_csv('1000m_air_sd.csv',index_col=False)
    static1 = pd.read_csv('700m_static1.csv')
    #static1[static1['COUNT'] < 3142] = pd.NA
    smerge_df = pd.read_csv('700m_smerge2_m1.csv')
    #smerge_df[smerge_df['COUNT'] < 3142] = pd.NA
    ndvi_df = pd.read_csv('700m_ndvi1.csv')
    #ndvi_df[ndvi_df['COUNT'] < 3142] = pd.NA
    air_m = pd.read_csv('700m_air_m1.csv')
    #air_m[air_m['COUNT'] < 3142] = pd.NA
    air_sd = pd.read_csv('700m_air_sd1.csv')
    # full = pd.read_csv('full_res_data.csv')
    # air = pd.read_csv('AirMoss_Clean.csv')
    print(static1.columns)
    static = static1[['PageName', 'Clay_','Sand_', 'Silt_', 'Eleva', 'Slope', 'Aspec']]
    # ['PageName', 'MEAN_Clay_pt', 'MEAN_Sand_pt', 'MEAN_Silt_pt_1', 'MEAN_Elevation_pt_1', 'MEAN_Slope_pt',
    #  'MEAN_Ascept_pt']
    static.columns = ["PageName","Clay",  "Sand", "Silt ","Elevation",  "Slope","Ascept"]
    air_check = air_sd[air_i].isna()
    air_m[air_i] = air_m[air_i] * (~air_check)
    for gh in range(0, 22):
        print(gh)
        out = pd.DataFrame(
            columns=["PageName",'Clay',  'Sand', 'Silt ','Elevation', 'Slope', 'Ascept', 'NDVI', 'Smerge', 'Air', 'Date'])
        out2 = pd.DataFrame(
            columns=["PageNumber",'Clay',  'Sand', 'Silt ','Elevation', 'Slope', 'Ascept', 'NDVI', 'Smerge', 'Air', 'Date'])
        #dynamic = pd.read_csv(csv_path1, usecols=[air[gh], smerge[gh], ndvi[gh]], index_col=False)
        dynamic = pd.DataFrame(columns=['NDVI', 'Smerge', 'Air', 'Date'])
        dynamic['NDVI'] = ndvi_df[ndvi[gh]]
        dynamic['Smerge'] = smerge_df[smerge[gh]]
        dynamic['Air'] = air_m[air_i[gh]]
        #dynamic.columns = ['NDVI', 'Smerge', 'Air']
        dynamic['Date'] = float(index2[gh])
        # dynamic['Date'] = pd.to_datetime(dynamic['Date'], format="%Y-%m-%d")
        out[["PageName","Clay", "Elevation", "Sand", "Silt ", "Slope","Ascept"]] = static
        out[['NDVI', 'Smerge', 'Air', 'Date']] = dynamic
        #out = out[out['Air']>0]
        out_full = pd.concat([out_full, out])
    # out_full = out_full[out_full['Ascept'].notnull()]
    #out_full.to_csv('Y_Air_moss_processed_1.csv', index=False)
    out_full = out_full.dropna(subset=['PageName','Clay',  'Sand', 'Silt ','Elevation', 'Slope', 'Ascept', 'NDVI', 'Smerge'])
    #print(out_full)
    out_full = out_full[
        ['PageName', 'Clay', 'Sand', 'Silt ', 'Elevation', 'Slope', 'Ascept', 'NDVI', 'Smerge', 'Air', 'Date']]
    print(out_full)
    out_full.to_csv('700m_reprocessed_1.csv', index=False)


alphabet_list = list(string.ascii_letters)
def col2num(col):
    num = 0
    for c in col:
        if c in alphabet_list:
            #print(c)
            num = num * 26 + (ord(c) - ord('A')) + 1
    return num
# range_csv = 'Moi_gridData.csv'
# page_ranges = pd.read_csv(range_csv, usecols=['COUNT', 'MIN_PageName', 'MAX_PageName', 'PageNumber'])
# out = pd.read_csv('out_data(1).csv', index_col=False)
# print(out.columns)
# out3 = pd.DataFrame(
#     columns=['Clay', 'Elevation', 'Sand', 'Silt ', 'Slope', 'Ascept', 'NDVI',
#        'Smerge', 'Air', 'Date', 'PageName', 'Col', 'Row'])
# null = pd.DataFrame(
#     columns=['Clay', 'Elevation', 'Sand', 'Silt ', 'Slope', 'Ascept', 'NDVI',
#                  'Smerge', 'Air', 'Date', 'PageName', 'Col', 'Row'])
if k==8:
    range_csv = 'Moi_gridData.csv'
    page_ranges = pd.read_csv(range_csv, usecols=['COUNT', 'MIN_PageName', 'MAX_PageName', 'PageNumber'])
    cord = pd.DataFrame(columns=['min_row','max_row','min_column','max_column'])

    i=0
    for row in page_ranges.itertuples():
        print(row)
        min = re.split('(\d+)', row[3])
        max = re.split('(\d+)', row[4])
        temp_cord = pd.DataFrame.from_dict({'min_row':[col2num(min[0])], 'max_row':[col2num(max[0])], 'min_column':[int(min[1])], 'max_column':[int(max[1])], 'page_number':[row[1]]})
        # print(col2num(min[0]))
        # print(col2num(max[0]))
        # temp_cord[['min_column']] = col2num(min[0])
        # temp_cord[['max_column']] = col2num(max[0])
        # temp_cord[['min_row']] = int(min[1])
        # temp_cord[['max_row']] = int(max[1])
        print(temp_cord)
        cord = pd.concat([cord, temp_cord])
        i = i+1
    cord.to_csv('cord_data.csv', index=False)
if k == 0:
    dex = ['Air_2012_1','Air_2012_2', 'Air_2012_3', 'Air_2013_0', 'Air_2013_1', 'Air_2013_2','Air_2013_3', 'Air_2013_4', 'Air_2014_0', 'Air_2014_1', 'Air_2014_2','Air_2014_3', 'Air_2014_4', 'Air_2014_5', 'Air_2014_6', 'Air_2014_7',
       'Air_2014_8', 'Air_2015_0', 'Air_2015_1', 'Air_2015_2', 'Air_2015_3','Air_2015_4']
    air_moss = pd.read_csv('AirMoss_toClean.csv')
    print(air_moss.columns)
    for g in range(0,22):
        print(dex[g])
        air = air_moss[dex[g]].to_numpy()
        air[air==0]=np.NAN
        air_moss[dex[g]] =air
    air_moss.columns=['OBJECTID', 'PageName', 'PageNumber', 'ORIG_FID', 'C_Air_2012_1a',
       'C_Air_2012_2a', 'C_Air_2012_3a', 'C_Air_2013_0a', 'C_Air_2013_1a', 'C_Air_2013_2a',
       'C_Air_2013_3a', 'C_Air_2013_4a', 'C_Air_2014_0a', 'C_Air_2014_1a', 'C_Air_2014_2a',
       'C_Air_2014_3a', 'C_Air_2014_4a', 'C_Air_2014_5a', 'C_Air_2014_6a', 'C_Air_2014_7a',
       'C_Air_2014_8a', 'C_Air_2015_0a', 'C_Air_2015_1a', 'C_Air_2015_2a', 'C_Air_2015_3a',
       'C_Air_2015_4a']
    print(air_moss.columns)
    air_moss.to_csv('AirMoss_Clean.csv', index=False)

if k==-1:
    loc = '/mnt/c/Users/asanchez2415/PycharmProjects/Data_Cleaner2/inst_processing/LR'
    dir_list = os.listdir(loc)
    #iinst index 1400m,1KM,2KM,3KM,400m
    inst_loc = ['J81','N113','G57','F38','AH283']
    print(dir_list)
    i = 0
    for data in dir_list:
        cur = pd.read_csv(loc+'/'+data)
        out = cur[cur['PageName'] == inst_loc[i]]
        out.to_csv(loc+'/inst_'+data,  index=False)
        i = i+1
if k ==0:
    print(894651066498401321085979)
    df = pd.read_csv('700m_processed_.csv', index_col=False)
    df_train,df_test = train_test_split(df, test_size=0.30, random_state=42)
    df_train.to_csv('700m_train.csv', index=False)
    df_test.to_csv('700m_test.csv', index=False)