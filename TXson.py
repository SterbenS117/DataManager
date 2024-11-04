import os
#os.environ["MODIN_ENGINE"] = "dask"
import datetime
import pandas as pd
#import modin.pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from natsort import natsorted
from sklearn.preprocessing import StandardScaler
import re
import string
import warnings
import sys

date = ["03/01/2016","03/08/2016","03/15/2016","03/22/2016","03/29/2016","04/5/2016","04/12/2016","04/19/2016","04/26/2016","05/03/2016","5/10/2016","05/17/2016",
        "05/24/2016","05/31/2016","06/07/2016","06/14/2016","06/21/2016","06/28/2016","07/05/2016","07/12/2016","03/01/2017","03/15/2017","03/29/2017","04/12/2017",
        "04/26/2017","05/10/2017","05/24/2017","06/07/2017","06/21/2017","07/05/2017","07/19/2017","08/02/2017","08/16/2017","08/30/2017","9/13/2017","09/27/2017",
        "10/11/2017","10/25/2017","11/08/2017","11/22/2017","03/01/2018","3/15/2018","03/29/2018","04/12/2018","04/26/2018","05/10/2018","5/24/2018","06/07/2018",
        "6/21/2018","07/5/2018","07/19/2018","08/2/2018","08/16/2018","08/30/2018","09/13/2018","9/27/2018","10/11/2018","10/25/2018","11/8/2018","11/22/2018",
        "03/01/2019","03/15/2019","03/29/2019","04/12/2019","04/26/2019","05/10/2019"] #TXson
date_in =['20160301','20160308','20160315','20160322','20160329','20160405','20160412','20160419','20160426','20160503','20160510','20160517',
          '20160524','20160531','20160607','20160614','20160621','20160628','20160705','20160712','20170301','20170315','20170329','20170412',
          '20170426','20170510','20170524','20170607','20170621','20170705','20170719','20170802','20170816','20170830','20170913','20170927',
          '20171011','20171025','20171108','20171122','20180301','20180315','20180329','20180412','20180426','20180510','20180524','20180607',
          '20180621','20180705','20180719','20180802','20180816','20180830','20180913','20180927','20181011','20181025','20181108','20181122',
          '20190301','20190315','20190329','20190412','20190426','20190510'] #TXson Index
def main_data_synth(resolution):
    static_home = '/mnt/d/TxSON/'+resolution+'m/'
    input_dir = '/mnt/d/TxSON/'+resolution+'m/'
    file_list = []
    for f in os.listdir(input_dir):
        if f.endswith(".csv"):
            file_list.append(f)
    file_list = natsorted(file_list)
    alb_file_list = []
    lai_file_list = []
    lst_file_list = []
    ndvi_file_list = []
    smerge_file_list = []
    air_file_list = []
    for w in file_list:
        if w.startswith("ALB"):
            alb_file_list.append(os.path.join(input_dir, w))
        if w.startswith("LAI"):
            lai_file_list.append(os.path.join(input_dir, w))
        if w.startswith("Prism"):
            lst_file_list.append(os.path.join(input_dir, w))
        if w.startswith("CON"):
            ndvi_file_list.append(os.path.join(input_dir, w))
        if w.startswith("Sme"):
            smerge_file_list.append(os.path.join(input_dir, w))

    f_data = pd.DataFrame(
        columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope', 'Elevation',
                 'Aspect'])
    # r = 110000
    r = 106150  # 400m 16941
    static = pd.read_csv(static_home + 'Static_'+resolution+'.csv')
    for k in range(1, 67):
        # print(lai_whole)
        current = pd.DataFrame(index=static["PageName"],
                               columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt',
                                        'Slope', 'Elevation', 'Aspect'])
        index = static["PageName"]
        current['SMERGE'] = pd.read_csv(smerge_file_list[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        # lst_temp = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).dropna()
        # print(static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept','PageName']].set_index("PageName"))
        print(lst_file_list[k - 1])
        current['Temp'] = pd.read_csv(lst_file_list[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["LAI"] = pd.read_csv(lai_file_list[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current['Temp'] = pd.read_csv(lst_file_list[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["Albedo"] = pd.read_csv(alb_file_list[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["NDVI"] = pd.read_csv(ndvi_file_list[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current[['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Aspect']] = static[
            ['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Aspect', 'PageName']].set_index("PageName")
        current['PageName'] = current.index
        current.index = range(current.shape[0])
        current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
        f_data = pd.concat([f_data, current])
        if k == 66:
            f_data.to_csv('TXson_'+resolution+'m_dataV6.csv')
            data = pd.read_csv('TXson_'+resolution+'m_dataV6.csv')
            data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Aspect'] > 0)]
            data1 = data1[
                ~(data1[["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Aspect"]] < 0).any(
                    axis=1)]
            data1 = data1.dropna()
            data1.to_csv('TXson_'+resolution+'m_dataV6_p.csv', index=False)
opopopop = 9
op = 33336
if op == 1:
    data = pd.read_csv('/mnt/d/TxSON/LAI_AG_400v2.csv')
    col = data.columns
    home = '/mnt/d/TxSON/400m/'
    for c in col:
        f_data = data[['PageName', c]]
        f_data.columns = ['PageName', 'MEAN']
        if '' in c:
            f_data.to_csv(home + c.replace('MEAN_','')+'.csv')
        print(f_data)


if op == 4:
    ty = ['400']
    for y in ty:
        main_data_synth(y)
if op == 5:
    data = pd.read_csv('TXson_1400m_dataV1.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Aspect'] > 0)]
    data1 = data1[ ~(data1[["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Aspect"]] < 0).any(axis=1)]
    data1 = data1.dropna()
    data1.to_csv('TXson_1400m_dataV1_p.csv', index=False)
    op = 6

if op == 6:
    fourm = ['A31', 'AI25', 'AL96', 'AR52', 'AW59', 'AY60', 'AY75', 'B4', 'BA64', 'BA65', 'BG72', 'BH69', 'BH72',
             'BI70', 'BI72', 'BK52', 'BK70', 'BK92', 'BM52', 'BM69', 'BS34', 'BU84', 'CD95', 'CF2', 'E30',
             'G32', 'H42', 'I27', 'J27', 'J40', 'J49', 'J95', 'K42', 'L48', 'M29', 'M42', 'M43', 'N29', 'N43', 'S96']
    sevenm = ['A18', 'A3', 'AB34', 'AC34', 'AC43', 'AE37', 'AE37', 'AH41', 'AI40', 'AI40', 'AI41', 'AI41', 'AJ30',
              'AJ40', 'AJ53', 'AK40', 'AL30', 'AO20', 'AP48', 'AU55', 'AV1', 'C17', 'D18', 'E24', 'F16', 'F16', 'F23',
              'F24', 'F28', 'F55', 'G28', 'H17',
              'H17', 'H24', 'H25', 'H25', 'K55', 'T14', 'V55', 'Z30']
    tenm = ['A13', 'A2', 'AA21', 'AA28', 'AC14', 'AD34', 'AH1', 'AH38', 'C12', 'C13', 'D11', 'D17', 'E11', 'E16', 'E17',
            'E20', 'E38', 'F12', 'F12', 'F17', 'F17', 'F17', 'F20', 'H39', 'O10', 'P39', 'R21', 'T24', 'U24', 'U30',
            'V26', 'V26', 'X29', 'Y28',
            'Y28', 'Y29', 'Y29', 'Z21', 'Z28', 'Z37']
    fouteenm = ['A2','A9','B9','C8','C12','C14','C28','D9','D12','D13','D14','F28','J7','K28','M15','N17','O17','O22','P19','Q21',
               'R15','R20','R21','R27','S15','S20','U10','U24','X1','X28']
    ####################################################################################################
    data = pd.read_csv('TXson_400m_dataV6_p.csv',
                       usecols=["SMERGE", "Date", 'Temp', "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt",
                                "Slope",
                                "Elevation", "Aspect", "PageName"])
    # data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(fourm)]  # 400m
    df_train = df_train.loc[~df_train['PageName'].isin(fourm)]  # 400m
    df_test = pd.concat([df_test, inst])
    df_train.to_csv('TXson_400m_dataV6_train.csv', index=False)
    df_test.to_csv('TXson_400m_dataV6_test.csv', index=False)
    print("Completel donnnnnnnnnnnnnnnn")
    ###########################################################################################################
    # data = pd.read_csv('TXson_700m_dataV1_p.csv',
    #                    usecols=["SMERGE", "Date", 'Temp', "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt",
    #                             "Slope",
    #                             "Elevation", "Aspect", "PageName"])
    # # data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    # df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    # inst = df_train.loc[df_train['PageName'].isin(sevenm)]  # 700m
    # df_train = df_train.loc[~df_train['PageName'].isin(sevenm)]  # 700m
    # df_test = pd.concat([df_test, inst])
    # df_train.to_csv('TXson_700m_dataV5_train.csv', index=False)
    # df_test.to_csv('TXson_700m_dataV5_test.csv', index=False)
    # # ###################################################################################################
    # data = pd.read_csv('TXson_1000m_dataV1_p.csv',
    #                    usecols=["SMERGE", "Date", 'Temp', "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt",
    #                             "Slope",
    #                             "Elevation", "Aspect", "PageName"])
    # # data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    # df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    # inst = df_train.loc[df_train['PageName'].isin(tenm)]  # 700m
    # df_train = df_train.loc[~df_train['PageName'].isin(tenm)]  # 700m
    # df_test = pd.concat([df_test, inst])
    # df_train.to_csv('TXson_1000m_dataV5_train.csv', index=False)
    # df_test.to_csv('TXson_1000m_dataV5_test.csv', index=False)
    ####################################################################################################
    # data = pd.read_csv('TXson_1400m_dataV1_p.csv',
    #                    usecols=["SMERGE", "Date", 'Temp', "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt",
    #                             "Slope",
    #                             "Elevation", "Aspect", "PageName"])
    # # data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    # df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    # inst = df_train.loc[df_train['PageName'].isin(fouteenm)]  # 1400m
    # df_train = df_train.loc[~df_train['PageName'].isin(fouteenm)]  # 1400m
    # df_test = pd.concat([df_test, inst])
    # df_train.to_csv('TXson_1400m_dataV1_train.csv', index=False)
    # df_test.to_csv('TXson_1400m_dataV1_test.csv', index=False)
    # print("Completel donnnnnnnnnnnnnnnn")



if op == 11:
    i = 0
    lst_home = '/mnt/d/TXson/LST_Tables/'
    names = ['TX_400m_dataV3_test.csv','TX_400m_dataV3_train.csv','TX_700m_dataV3_test.csv','TX_700m_dataV3_train.csv','TX_1000m_dataV3_test.csv','TX_1000m_dataV3_train.csv']
    reso = ['400','400', '700','700', '1000', '1000']
    for n in names:
        data = pd.read_csv(n, usecols=['SMERGE','Date','PageName','LAI','Albedo','NDVI','Clay','Sand','Silt ','Slope','Elevation','Ascept']).set_index("PageName")
        print(n)
        print(data.columns)
        data.columns = ['SMERGE','Date','LAI','Albedo','NDVI','Clay','Sand','Silt','Slope','Elevation','Ascept']
        data["Temp"] = np.NAN
        data.sort_index()
        data.sort_values(by=["Date"])
        for p in date_in:
            lst_c = pd.read_csv(lst_home+"Prism_TXson_"+p+"_"+reso[i]+".csv", usecols=["MEAN","PageName"]).set_index("PageName")
            q = pd.to_datetime(p, format='%Y%m%d')
            data['Date2'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
            print(q)
            #print(data[data['Date'] == int(p)]['LST'])
            print(lst_c["MEAN"])
            data.loc[data['Date2'] == q,'Temp'] = lst_c["MEAN"]
            print(data[data['Date2'] == q]['Temp'])
        # data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]

        #data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
        data1 = data[~(data[["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Ascept"]] < 0).any(
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

        data1.to_csv(n.replace("V3","V4"), index=True)
        i = i + 1

if opopopop == 9:
    print('sdakojpoiafdjhposidafhjuidosa')
    # fourm = ["A31", "B4", "E30", "G32", "H42", "I27", "J27", "J40", "J49", "J95", "K42", "L48", "M29", "M42", "M43","N29", "N43", "S96", "AI25", "AL96", "AR52","AW59", "AY60", "AY75", "BA64", "BA65", "BG72", "BH69", "BH72", "BI70", "BI72", "BK52", "BK70", "BK92","BM52", "BM69", "BS34", "BU84", "CD95", "CF2"]
    # sevenm = ["A3", "A18", "C17", "D18", "E24", "F16", "F23", "F24", "F28", "F55", "G28", "H17", "H24", "H25", "K55","T14", "V55", "Z30", "AB34", "AC34", "AC43", "AE37","AH41", "AI40", "AI41", "AJ30", "AJ40", "AJ53", "AK40", "AL30", "AO20", "AP48", "AU55", "AV1"]
    # tenm = ["A2", "A13", "C12", "C13", "D11", "D17", "E11", "E16", "E17", "E20", "E38", "F12", "F17", "F20", "H39","O10", "P39", "R21", "T24", "U24", "U30", "V26","X29", "Y28", "Y29", "Z21", "Z28", "Z37", "AA21", "AA28", "AC14", "AD34", "AH1", "AH38"]
    fourm = ['A31', 'AI25', 'AL96', 'AR52', 'AW59', 'AY60', 'AY75', 'B4', 'BA64', 'BA65', 'BG72', 'BH69', 'BH72', 'BI70','BI72', 'BK52', 'BK70', 'BK92', 'BM52', 'BM69', 'BS34', 'BU84', 'CD95', 'CF2', 'E30',
             'G32', 'H42', 'I27', 'J27','J40', 'J49', 'J95', 'K42', 'L48', 'M29', 'M42', 'M43', 'N29', 'N43', 'S96']
    four_n = ['CR200-28','LCRA-4','LCRA-5','CR200-10','CR200-2','CR200-16','CR200-8','CR1000-4','CR200-17','CR1000-3','CR200-24','CR200-15','CR200-25','CR1000-2','CR200-18','CR200-5','CR200-6','LCRA-6','CR200-11','CR200-7',
              'CR200-12','CR200-23','LCRA-3','LCRA-7','CR200-29','CR1000-6','CR200-1','CR200-13','CR200-22','CR200-9','CR200-4','LCRA-1','CR200-3','CR200-21','LCRA-2','CR200-26','CR1000-1','CR200-19','CR200-14','CR1000-5']
    sevenm = ['A18','A3','AB34','AC34','AC43','AE37','AE37','AH41','AI40','AI40','AI41','AI41','AJ30','AJ40','AJ53','AK40','AL30','AO20','AP48','AU55','AV1','C17','D18','E24','F16','F16','F23','F24','F28','F55','G28','H17',
              'H17','H24','H25','H25','K55','T14','V55','Z30']
    seven_n = ['CR200-28', 'CR1000-4', 'CR200-2', 'CR200-16', 'CR200-8', 'CR1000-3', 'CR200-17', 'CR200-24', 'CR1000-2','CR200-15', 'CR200-18', 'CR200-25','CR200-5', 'CR200-6', 'LCRA-6',
               'CR200-7', 'CR200-11', 'CR200-12', 'CR200-23', 'LCRA-3', 'LCRA-7','CR200-29', 'CR1000-6', 'CR200-1', 'CR200-13',
              'CR200-22', 'CR200-9', 'CR200-3', 'CR200-4', 'LCRA-1', 'CR200-21', 'CR200-19', 'LCRA-2', 'CR200-26','CR1000-1', 'CR200-14', 'CR1000-5', 'LCRA-4', 'LCRA-5', 'CR200-10']
    tenm = ['A13','A2','AA21','AA28','AC14','AD34','AH1','AH38','C12','C13','D11','D17','E11','E16','E17','E20','E38','F12','F12','F17','F17','F17','F20','H39','O10','P39','R21','T24','U24','U30','V26','V26','X29','Y28',
            'Y28','Y29','Y29','Z21','Z28','Z37']
    ten_n = ['CR200-28','CR1000-4','CR200-11','CR200-7','CR200-12','CR200-23','LCRA-7','LCRA-3','CR200-29','CR1000-6','CR200-13','CR200-1','CR200-22','CR200-9','CR200-3','CR200-4','LCRA-1','CR200-19','LCRA-2','CR1000-1',
             'CR200-14','CR200-26','CR200-21','CR1000-5','LCRA-4','LCRA-5','CR200-10','CR200-2','CR200-16','CR200-8','CR1000-3','CR200-17','CR200-24','CR1000-2','CR200-15','CR200-18','CR200-25','CR200-5','CR200-6','LCRA-6']
    fourteenm = ['A2','A9','B9','B9','C12','C12','C12','C14','C28','C8','C8','D12','D13','D13','D14','D9','D9','F28','J7','K28','M15','N17','O17','O22','P19','P19','Q21','R15','R20','R20','R20','R21','R21','R27',
                 'S15','S20','U10','U24','X1','X28']
    fourteen_n = ['CR1000-4','CR200-28','CR200-29','CR1000-6','CR200-1','CR200-3','CR200-9','CR200-4','LCRA-1','CR200-13','CR200-22','CR200-26','CR200-14','CR1000-1','CR200-21','CR200-19','LCRA-2','CR1000-5','LCRA-4','LCRA-5',
                  'CR200-10','CR200-2','CR200-16','CR200-8','CR200-17','CR1000-3','CR200-24','CR200-5','CR200-6','CR200-15','CR1000-2','CR200-18','CR200-25','LCRA-6','CR200-11','CR200-7','CR200-12','CR200-23','LCRA-7','LCRA-3']
    home = '/mnt/d/TXson/ML/'
    res = 'RF'
    data_csv = ['_V6_TX_400m_.csv']
    #data_csv = ['_V4_TX_1000m_.csv','_V4_TX_400m_.csv','_V4_TX_700m_.csv']
    #data_csv = ['_V4_TX_1400m_.csv']
    for d in data_csv:
        print(d)
        # if '1400m' in d:
        #     try:
        #         data = pd.read_csv(home + res + d).rename({'Lai' : 'LAI'}, axis='columns')
        #     except:
        #         data = pd.read_csv(home + d)
        #     data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
        #     p = len(fourteenm)
        #     out = pd.DataFrame(columns=['Clay', 'Sand', 'Silt', 'Elevation', 'Aspect', 'Slope', 'LAI', 'SMERGE','NDVI', 'Albedo', 'Temp', 'Date', 'ML_', 'PageName', 'Station'])
        #     for q in range(0, p):
        #         #inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
        #         inst = data[data['PageName'] == fourteenm[q]]
        #         inst['Station'] = fourteen_n[q]
        #         inst.reset_index(inplace = True)
        #
        #         out = pd.concat([out, inst])
        #     out.sort_values(by=['Station', 'Date'], inplace=True)
        #     out.drop(columns=['index'], inplace=True)
        #     print(home + res + '_v4_TXson1_1400mInst.csv')
        #     out.to_csv(home + res +'_v4_TXson1_1400mInst.csv', index=False)
        # if '1000m' in d:
        #     try:
        #         data = pd.read_csv(home + res + d).rename({'Lai' : 'LAI'}, axis='columns')
        #     except:
        #         data = pd.read_csv(home + d)
        #     data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
        #     p = len(tenm)
        #     out = pd.DataFrame(columns=['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'LAI', 'SMERGE','NDVI', 'Albedo', 'Temp', 'Date', 'ML_', 'PageName', 'Station'])
        #     for q in range(0, p):
        #         #inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
        #         inst = data[data['PageName'] == tenm[q]]
        #         inst['Station'] = ten_n[q]
        #         inst.reset_index(inplace = True)
        #
        #         out = pd.concat([out, inst])
        #     out.sort_values(by=['Station', 'Date'], inplace=True)
        #     out.drop(columns=['index'], inplace=True)
        #     print(home + res + '_v4_TXson1_1000mInst.csv')
        #     out.to_csv(home + res +'_v4_TXson1_1000mInst.csv', index=False)
        # if '700m' in d:
        #     try:
        #         data = pd.read_csv(home + res + d).rename({'Lai': 'LAI'}, axis='columns')
        #     except:
        #         data = pd.read_csv(home + d)
        #     data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
        #     p = len(sevenm)
        #     out = pd.DataFrame(
        #         columns=['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'LAI', 'SMERGE', 'NDVI', 'Albedo',
        #                  'Temp', 'Date', 'ML_', 'PageName', 'Station'])
        #     for q in range(0, p):
        #         # inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
        #         inst = data[data['PageName'] == sevenm[q]]
        #         inst['Station'] = seven_n[q]
        #         inst.reset_index(inplace=True)
        #
        #         out = pd.concat([out, inst])
        #     out.sort_values(by=['Station', 'Date'], inplace=True)
        #     out.drop(columns=['index'], inplace=True)
        #     print(home + res + '_v4_TXson1_700mInst.csv')
        #     out.to_csv(home + res + '_v4_TXson1_700mInst.csv', index=False)
        if '_400m' in d:
            try:
                data = pd.read_csv(home + res + d).rename({'Lai': 'LAI'}, axis='columns')
            except:
                data = pd.read_csv(home + res + d)
            data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
            p = len(fourm)
            out = pd.DataFrame(
                columns=['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'LAI', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'Date', 'ML_', 'PageName', 'Station'])
            for q in range(0, p):
                # inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
                inst = data[data['PageName'] == fourm[q]]
                inst['Station'] = four_n[q]
                inst.reset_index(inplace=True)

                out = pd.concat([out, inst])
            out.sort_values(by=['Station', 'Date'], inplace=True)
            out.drop(columns=['index'], inplace=True)
            print(home + res + '_v4_TXson1_400mInst.csv')
            out.to_csv(home + res + '_v4_TXson1_400mInst.csv', index=False)

