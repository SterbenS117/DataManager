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

era3_nvdi = ["MEAN_N20030401", "MEAN_N20030415", "MEAN_N20030429", "MEAN_N20030513", "MEAN_N20030527", "MEAN_N20030610",
             "MEAN_N20030624","MEAN_N20030731","MEAN_N20030814","MEAN_N20030828","MEAN_N20030910","MEAN_N20031023",
             "MEAN_N20040401","MEAN_N20040415","MEAN_N20040430","MEAN_N20040514","MEAN_N20040528","MEAN_N20040617",
             "MEAN_N20040701","MEAN_N20040715","MEAN_N20040729","MEAN_N20040812","MEAN_N20040826","MEAN_N20040909",
             "MEAN_N20040923","MEAN_N20041007","MEAN_N20041021","MEAN_N20050401","MEAN_N20050415","MEAN_N20050429",
             "MEAN_N20050513","MEAN_N20050527","MEAN_N20050610","MEAN_N20050628","MEAN_N20050713","MEAN_N20050727",
             "MEAN_N20050822","MEAN_N20050905","MEAN_N20050920","MEAN_N20051004","MEAN_N20051018","MEAN_N20060401",
             "MEAN_N20060415","MEAN_N20060707","MEAN_N20060806","MEAN_N20060826","MEAN_N20060909","MEAN_N20060923",
             "MEAN_N20061007","MEAN_N20061021","MEAN_N20070620","MEAN_N20070813"]
era3_smerge = ["MEAN_F20030401", "MEAN_F20030415", "MEAN_F20030429", "MEAN_F20030513", "MEAN_F20030527", "MEAN_F20030610", "MEAN_F20030624",
               "MEAN_F20030731","MEAN_F20030814","MEAN_F20030828","MEAN_F20030910","MEAN_F20031023","MEAN_F20040401","MEAN_F20040415",
               "MEAN_F20040430","MEAN_F20040514","MEAN_F20040528","MEAN_F20040617","MEAN_F20040701","MEAN_F20040715","MEAN_F20040729",
               "MEAN_F20040812","MEAN_F20040826","MEAN_F20040909","MEAN_F20040923","MEAN_F20041007","MEAN_F20041021","MEAN_F20050401",
               "MEAN_F20050415","MEAN_F20050429","MEAN_F20050513","MEAN_F20050527","MEAN_F20050610","MEAN_F20050628","MEAN_F20050713",
               "MEAN_F20050727","MEAN_F20050822","MEAN_F20050905","MEAN_F20050920","MEAN_F20051004","MEAN_F20051018","MEAN_F20060401",
               "MEAN_F20060415","MEAN_F20060707","MEAN_F20060806","MEAN_F20060826","MEAN_F20060909","MEAN_F20060923","MEAN_F20061007",
               "MEAN_F20061021","MEAN_F20070620","MEAN_F20070813"]
doy = ["121","135","149","163","177","191","205","242","256","270","283","326","122","136","151","165","179","199","213","227","241","255","269","283",
       "297","311","325","121","135","149","163","177","191","209","224","238","264","278","293","307","321","121","135","218","248","268","282","296","310","324","201","255"]

date = ["4/1/2003","4/15/2003","4/29/2003","5/13/2003","5/27/2003","6/10/2003","6/24/2003","7/31/2003","8/14/2003","8/28/2003","9/10/2003","10/23/2003","4/1/2004","4/15/2004",
        "4/30/2004","5/14/2004","5/28/2004","6/17/2004","7/1/2004","7/15/2004","7/29/2004","8/12/2004","8/26/2004","9/9/2004","9/23/2004","10/7/2004","10/21/2004","4/1/2005",
        "4/15/2005","4/29/2005","5/13/2005","5/27/2005","6/10/2005","6/28/2005","7/13/2005","7/27/2005","8/22/2005","9/5/2005","9/20/2005","10/4/2005","10/18/2005","4/1/2006",
        "4/15/2006","7/7/2006","8/6/2006","8/26/2006","9/9/2006","9/23/2006","10/7/2006","10/21/2006","6/20/2007","8/13/2007"]
k = 16
if k == 1:
    for o in range(1,5):
        input_dir = "/mnt/d/ARM/Era3/Static/Era3_"+str(o)+"/"
        four = []
        seven = []
        ten = []
        for f in os.listdir(input_dir):
            print(f)
            if f.endswith("400.csv"):
                four.append(f)
            if f.endswith("700.csv"):
                seven.append(f)
            if f.endswith("1000.csv"):
                ten.append(f)
        four = natsorted(four)
        seven = natsorted(seven)
        print(seven)
        ten = natsorted(ten)
        #########################################################################################################################################
        index = pd.read_csv(os.path.join(input_dir, four[0]), usecols=["PageName"])
        static_400m = pd.DataFrame(index=index["PageName"])
        for f in four:
            temp = pd.read_csv(os.path.join(input_dir, f)).set_index("PageName")
            static_400m[f.split("_", 1)[0]] = temp['MEAN']
            print(f.split("_", 1)[0])
            static_400m.to_csv(input_dir + "/ARM_Static_400m.csv")
        #########################################################################################################################################
        index = pd.read_csv(os.path.join(input_dir, seven[0]), usecols=["PageName"])
        static_700m = pd.DataFrame(index=index["PageName"])
        for s in seven:
            temp = pd.read_csv(os.path.join(input_dir, s)).set_index("PageName")
            static_700m[s.split("_", 1)[0]] = temp['MEAN']
            static_700m.to_csv(input_dir + "/ARM_Static_700m.csv")
        #########################################################################################################################################
        index = pd.read_csv(os.path.join(input_dir, ten[0]), usecols=["PageName"])
        static_1000m = pd.DataFrame(index=index["PageName"])
        for t in ten:
            temp = pd.read_csv(os.path.join(input_dir, t)).set_index("PageName")
            static_1000m[t.split("_", 1)[0]] = temp['MEAN']
            static_1000m.to_csv(input_dir + "/ARM_Static_1000m.csv")

if k == 2:
    for o in range(1,5):
        static_home = '/mnt/d/ARM/Era3/Static/ERA3_'+str(o)+'/'
        ndvi_four = pd.read_csv("/mnt/d/ARM/Era3/tables/NDVI_ARM_3_"+str(o)+"_400.csv").dropna(axis=1).set_index("PageName")
        ndvi_seven = pd.read_csv("/mnt/d/ARM/Era3/tables/NDVI_ARM_3_"+str(o)+"_700.csv").dropna(axis=1).set_index("PageName")
        ndvi_ten = pd.read_csv("/mnt/d/ARM/Era3/tables/NDVI_ARM_3_"+str(o)+"_1000.csv").dropna(axis=1).set_index("PageName")
        smerge_four = pd.read_csv('/mnt/d/ARM/Era3/tables/ARM_3_'+str(o)+'_SMERGE_400.csv').dropna(axis=1).set_index("PageName")
        smerge_seven = pd.read_csv('/mnt/d/ARM/Era3/tables/ARM_3_'+str(o)+'_SMERGE_700.csv').dropna(axis=1).set_index("PageName")
        smerge_ten = pd.read_csv('/mnt/d/ARM/Era3/tables/ARM_3_'+str(o)+'_SMERGE_1000.csv').dropna(axis=1).set_index("PageName")
        lst_dir = '/mnt/d/%s/TXson' % 'Temp'
        input_dir = "/mnt/d/ARM/Era3/ERA3_"+str(o)+"/All_Data"
        four = []
        seven = []
        ten = []
        for f in os.listdir(input_dir):
            if f.endswith("-400.csv"):
                four.append(f)
            if f.endswith("700.csv"):
                seven.append(f)
            if f.endswith("1000.csv"):
                ten.append(f)
        four = natsorted(four)
        seven = natsorted(seven)
        ten = natsorted(ten)
        print(seven)
        print(123456789)
        alb_four = []
        alb_seven = []
        alb_ten = []
        lai_four = []
        lai_seven = []
        lai_ten = []
        lst_four = []
        lst_seven = []
        lst_ten = []
        for w in four:
            if w.startswith("ALB"):
                alb_four.append(os.path.join(input_dir, w))
            if w.startswith("LAI"):
                lai_four.append(os.path.join(input_dir, w))
            if w.startswith("Prism"):
                lst_four.append(os.path.join(input_dir, w))
        for t in seven:
            if t.startswith("ALB"):
                alb_seven.append(os.path.join(input_dir, t))
            if t.startswith("LAI"):
                lai_seven.append(os.path.join(input_dir, t))
            if t.startswith("Prism"):
                lst_seven.append(os.path.join(input_dir, t))
        for h in ten:
            if h.startswith('ALB'):
                alb_ten.append(os.path.join(input_dir, h))
            if h.startswith('LAI'):
                lai_ten.append(os.path.join(input_dir, h))
            if h.startswith("Prism"):
                lst_ten.append(os.path.join(input_dir, h))
        f_data = pd.DataFrame(
            columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope', 'Elevation',
                     'Ascept'])
        # r = 110000
        r = 106150  # 400m 16941
        static = pd.read_csv(static_home + "ARM_Static_400m.csv")
        for k in range(1, 53):
            print(lst_four[k - 1])
            current = pd.DataFrame(index=static["PageName"],
                                   columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt',
                                            'Slope', 'Elevation', 'Ascept'])
            index = static["PageName"]
            sm = [col for col in smerge_four.columns if era3_smerge[k - 1] in col]
            nv = [col for col in ndvi_four.columns if era3_nvdi[k - 1] in col]
            current["NDVI"] = ndvi_four[nv[0]]
            current['SMERGE'] = smerge_four[sm[0]]
            # lst_temp = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).dropna()
            # print(static[['Clay' ,'Sand' ,'Silt','Slope' ,'Elevation' ,'Ascept','PageName']].set_index("PageName"))
            current['Temp'] = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current["LAI"] = pd.read_csv(lai_four[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current['Temp'] = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current["Albedo"] = pd.read_csv(alb_four[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current[['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Ascept']] = static[
                ['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Ascept', 'PageName']].set_index("PageName")
            current['PageName'] = current.index
            current.index = range(current.shape[0])
            current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
            f_data = pd.concat([f_data, current])
            if k == 52:
                f_data.to_csv('ARM_400m_dataV1_Era3_'+str(o)+'.csv')
        r = 17500  # 1000m
        r = 16940  # 1000m
        static = pd.read_csv(static_home + "ARM_Static_1000m.csv")
        f_data = pd.DataFrame(
            columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope', 'Elevation',
                     'Ascept'])
        for k in range(1, 53):
            current = pd.DataFrame(index=static["PageName"],
                                   columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt',
                                            'Slope', 'Elevation', 'Ascept'])
            index = static["PageName"]
            print(k)
            # print(len(alb_hundred_m))
            sm = [col for col in smerge_ten.columns if era3_smerge[k - 1] in col]
            nv = [col for col in ndvi_ten.columns if era3_nvdi[k - 1] in col]
            current["NDVI"] = ndvi_ten[nv[0]]
            current['SMERGE'] = smerge_ten[sm[0]]
            # current['LST'] = pd.read_csv(lst_ten[k-1], usecols=["MEAN","PageName"]).sort_values(by=["PageName"]).drop("PageName",axis=1)
            # lst_temp = pd.read_csv(lst_ten[k - 1], usecols=["MEAN", "PageName"]).dropna()
            current['Temp'] = pd.read_csv(lst_ten[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current["LAI"] = pd.read_csv(lai_ten[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current['Temp'] = pd.read_csv(lst_ten[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            print(lst_ten[k - 1])
            current["Albedo"] = pd.read_csv(alb_ten[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current[['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Ascept']] = static[
                ['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Ascept', 'PageName']].set_index("PageName")
            current['PageName'] = current.index
            current.index = range(current.shape[0])
            current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
            f_data = pd.concat([f_data, current])
            print(f_data[['Temp', 'Date']])
            if k == 52:
                f_data.to_csv('ARM_1000m_dataV1_Era3_'+str(o)+'.csv')
        # r = 37000 # 700m
        r = 34650  # 700m
        static = pd.read_csv(static_home + "ARM_Static_700m.csv")
        current = pd.DataFrame(index=static["PageName"])
        index = static["PageName"]
        f_data = pd.DataFrame(
            columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope', 'Elevation',
                     'Ascept'])
        for k in range(1, 53):
            current = pd.DataFrame(index=static["PageName"],
                                   columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt',
                                            'Slope', 'Elevation', 'Ascept'])
            index = static["PageName"]
            # print(w)
            # print(len(alb_thirty_m))
            sm = [col for col in smerge_seven.columns if era3_smerge[k - 1] in col]
            nv = [col for col in ndvi_seven.columns if era3_nvdi[k - 1] in col]
            current["NDVI"] = ndvi_seven[nv[0]]
            current['SMERGE'] = smerge_seven[sm[0]]
            current['Temp'] = pd.read_csv(lst_seven[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current["LAI"] = pd.read_csv(lai_seven[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current['Temp'] = pd.read_csv(lst_seven[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current["Albedo"] = pd.read_csv(alb_seven[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
            current[['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Ascept']] = static[
                ['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Ascept', 'PageName']].set_index("PageName")
            current['PageName'] = current.index
            current.index = range(current.shape[0])
            current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
            f_data = pd.concat([f_data, current])
            if k == 52:
                f_data.to_csv('ARM_700m_dataV1_Era3_'+str(o)+'.csv')
                #k = 3
if k == 3:
    for o in range(1, 5):
        data = pd.read_csv('ARM_700m_dataV1_Era3_'+str(o)+'.csv')
        data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
        data1 = data1[
            ~(data1[["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Ascept"]] < 0).any(axis=1)]
        data1 = data1.dropna()
        data1.to_csv('ARM_700m_dataV1_pEra3_'+str(o)+'.csv', index=False)
        #######################################################################################################
        data = pd.read_csv('ARM_1000m_dataV1_Era3_'+str(o)+'.csv')
        data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
        data1 = data1[
            ~(data1[["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Ascept"]] < 0).any(axis=1)]
        data1 = data1.dropna()
        data1.to_csv('ARM_1000m_data_pEra3_'+str(o)+'.csv', index=False)
        #####################################################################################################
        data = pd.read_csv('ARM_400m_dataV1_Era3_'+str(o)+'.csv')
        data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
        data1 = data1[
            ~(data1[["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Ascept"]] < 0).any(
                axis=1)]
        data1 = data1.dropna()
        data1.to_csv('ARM_400m_data_pEra3_'+str(o)+'.csv', index=False)
    k = 4
if k == 4:
    for o in range(1,5):
        # fourm = ["AX164","CL352","J70","DI534","DO147","FW240","AF301","CX18"] #Era 11
        # sevenm = ["E40","R172","AB94","AY201","BF10","BM306","BP84","CX137"]
        # tenm = ["D28","M121","T66","AJ141","AO7","AS214","AV59","BT96"]
        if o == 1:
            fourm = ["AN597", "BQ37", "EI311", "FM675"]  # Era31
            sevenm = ["X341", "AN21", "CB178", "CS386"]
            tenm = ["P239", "AB15", "BD125", "BP270"]
        if o == 2:
            fourm = ["O21", "BS589", "EK306", "HJ528"]  # Era32
            sevenm = ["I12", "AO337", "CC175", "DU302"]
            tenm = ["F9", "AC236", "BE123", "CI212"]
        if o == 3:
            fourm = ["Q108", "DA217", "FL40"]  # Era33
            sevenm = ["K62", "BI124", "CS23"]
            tenm = ["H44", "AQ87", "BP16"]
        if o == 4:
            fourm = ["AA32", "FI629", "FK343", "HP76"]  # Era34
            sevenm = ["P19", "CQ360", "CR196", "DX44"]
            tenm = ["L13", "BO252", "BP137", "CM31"]
        data = pd.read_csv('ARM_700m_dataV1_pEra3_'+str(o)+'.csv',
                           usecols=["SMERGE", "Date", ("%s" % 'Temp'), "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope",
                                    "Elevation", "Ascept", "PageName"])
        data.columns = ["SMERGE", "Date", ("%s" % 'Temp'), "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation",
                        "Ascept", "PageName"]
        df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
        inst = df_train.loc[df_train['PageName'].isin(sevenm)]  # 700m
        df_train = df_train.loc[~df_train['PageName'].isin(sevenm)]  # 700m
        df_test = pd.concat([df_test, inst])
        df_train.to_csv('Era3_' + str(o) + 'ARM_700m_dataV1_train.csv', index=False)
        df_test.to_csv('Era3_' + str(o) + 'ARM_700m_dataV1_test.csv', index=False)
        ###################################################################################################
        data = pd.read_csv('ARM_1000m_data_pEra3_'+str(o)+'.csv',
                           usecols=["SMERGE", "Date", ("%s" % 'Temp'), "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope",
                                    "Elevation", "Ascept", "PageName"])
        # data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
        df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
        inst = df_train.loc[df_train['PageName'].isin(tenm)]  # 1000m
        df_train = df_train.loc[~df_train['PageName'].isin(tenm)]  # 1000m
        df_test = pd.concat([df_test, inst])
        df_train.to_csv('Era3_' + str(o) + 'ARM_1000m_dataV1_train.csv', index=False)
        df_test.to_csv('Era3_' + str(o) + 'ARM_1000m_dataV1_test.csv', index=False)
        ####################################################################################################
        data = pd.read_csv('ARM_400m_data_pEra3_'+str(o)+'.csv',
                           usecols=["SMERGE", "Date", ("%s" % 'Temp'), "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope",
                                    "Elevation", "Ascept", "PageName"])
        # data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
        df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
        inst = df_train.loc[df_train['PageName'].isin(fourm)]  # 1000m
        df_train = df_train.loc[~df_train['PageName'].isin(fourm)]  # 1000m
        df_test = pd.concat([df_test, inst])
        df_train.to_csv('Era3_' + str(o) + 'ARM_400m_dataV1_train.csv', index=False)
        df_test.to_csv('Era3_' + str(o) + 'ARM_400m_dataV1_test.csv', index=False)
        print("Completel donnnnnnnnnnnnnnnn")
    #k = 5
if k == 6:
    fourm = ["Q108", "DA217", "FL40"]  # Era33
    sevenm = ["K62", "BI124", "CS23"]
    tenm = ["H44", "AQ87", "BP16"]
    data = pd.read_csv('RF_v4_ARM_ERA33_1000m7030.csv')
    inst = data.loc[data['PageName'].isin(fourm)]  # 400m
    #inst = data.loc[data['PageName'].isin(tenm)]#1000m
    #inst = data.loc[data['PageName'].isin(sevenm)] #700m
    inst.to_csv('RF_v4_ARM_ERA33_1000mInst2.csv', index=False)
if k == 16:
    type = "RF"
    era = [1,2,3,4]
    era_s = ["ERA31","ERA32","ERA33","ERA34"]
    for e in era:
        four = []
        seven = []
        ten = []
        fourteen = []
        input_dir = '/mnt/d/ARM/Fontera/ARM3_V3_400fixed/Era3_'+str(e)+'/ML'
        for f in os.listdir(input_dir):
            if era_s[e-1] in f:
                if f.endswith("_400m.csv") & f.startswith(type):
                    four.append(f)
                if f.endswith("_700m.csv") & f.startswith(type):
                    seven.append(f)
                if f.endswith("_1000m.csv") & f.startswith(type):
                    ten.append(f)
                if f.endswith("_1400m.csv") & f.startswith(type):
                    fourteen.append(f)
        # data_n = 'GBR_v4_ARM_ERA31_700m.csv'
        # data_out = 'GBR_v4_ARM_ERA31_700mInst.csv'
        inst_dir = '/mnt/d/ARM/Era3/ARM3_CSV/ARM_3_'
        if e == 1:
            fourm = ["AN597", "BQ37", "EI311", "FM675"]  # Era31
            sevenm = ["X341", "AN21", "CB178", "CS386"]
            tenm = ["P239", "AB15", "BD125", "BP270"]
            fourteenm = ["M171", "U11", "AO89", "AW193"]
            names = ["HillsBoro", "Larned", "Plevna", "Towanda"]  # Era31

        if e == 2:
            fourm = ["O21", "BS589", "EK306", "HJ528"]  # Era32
            sevenm = ["I12", "AO337", "CC175", "DU302"]
            tenm = ["F9", "AC236", "BE123", "CI212"]
            fourteenm = ["E6", "U169", "AO88", "BK151"]
            names = ["Coldwater", "Ashton", "Byron", "Lamont-CF1"]  # Era32
        if e == 3:
            fourm = ["Q108", "DA217", "FL40"]  # Era33
            sevenm = ["K62", "BI124", "CS23"]
            tenm = ["H44", "AQ87", "BP16"]
            fourteenm = ["F31", "AE62", "AW12"]
            names = ["ElkFalls", "Tyro", "Pawhuska"]  # Era33
        if e == 4:
            fourm = ["AA32", "FI629", "FK343", "HP76"]  # Era34
            sevenm = ["P19", "CQ360", "CR196", "DX44"]
            tenm = ["L13", "BO252", "BP137", "CM31"]
            fourteenm = ["H10", "AV180", "AV98", "BL22"]
            names = ["Vici","Meeker","ElReno", "Cordell"]  # Era34

        for name in four:
            data_n = name
            data_out = name.replace('.csv', 'inst.csv')
            data = pd.read_csv(input_dir + '/' + data_n)
            print(data_n)
            print(data)
            inst = data.loc[data['PageName'].isin(fourm)]  # 400m
            p = len(fourm)
            inst = data.loc[data['PageName'].isin(fourm)]  # 1000m
            inst['Date2'] = inst['Date']
            inst['Station_E'] = np.nan
            inst['Station_W'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == fourm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q] + '_E.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                print(inst.columns)
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_E',
                                    'Station_W', 'Station_Name']
                    print(inst.columns)
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

                # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_E'] = pd.to_numeric(inst['Station_E'], errors='coerce')
            inst['Station_W'] = pd.to_numeric(inst['Station_W'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            four_dex = input_dir + '/' + data_out
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', 'Fixed4.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()
        four_index = pd.read_csv(four_dex).set_index(['Station_Name', 'Date2'])########################################################################################
        for name in ten:
            data_out = name.replace('.csv', 'inst.csv')
            data_out2 = name.replace('.csv', 'inst_trim.csv')
            data_n = name
            data = pd.read_csv(input_dir + '/' + data_n)
            print(data)
            inst = data.loc[data['PageName'].isin(tenm)]  # 1000m
            inst['Date2'] = inst['Date']
            inst['Station_E'] = np.nan
            inst['Station_W'] = np.nan
            inst.set_index(['Date'], inplace=True)
            p = len(tenm)
            for q in range(0, p):
                inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q] + '_E.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                print(inst)
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_E',
                                    'Station_W', 'Station_Name']
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]
                # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst.to_csv(input_dir + '/' + data_out, index=False)
            inst2 = inst.set_index(['Station_Name', 'Date2'])
            temp = inst2.reindex(four_index.index)
            temp['Station_E'] = pd.to_numeric(temp['Station_E'], errors='coerce')
            temp['Station_W'] = pd.to_numeric(temp['Station_W'], errors='coerce')
            temp.to_csv(input_dir + '/' + data_out2, index=True)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', '.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            temp.to_excel(writer, sheet_name='Sheet2', index=True)
            writer.save()

        for name in fourteen:
            data_out = name.replace('.csv', 'inst.csv')
            data_out2 = name.replace('.csv', 'inst_trim.csv')
            data_n = name
            data = pd.read_csv(input_dir + '/' + data_n)
            print(data)
            inst = data.loc[data['PageName'].isin(fourteenm)]  # 1000m
            inst['Date2'] = inst['Date']
            inst['Station_E'] = np.nan
            inst['Station_W'] = np.nan
            inst.set_index(['Date'], inplace=True)
            p = len(fourteenm)
            for q in range(0, p):
                inst.loc[inst['PageName'] == fourteenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q] + '_E.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                print(inst)
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_E',
                                    'Station_W', 'Station_Name']
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]
                # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst.to_csv(input_dir + '/' + data_out, index=False)
            inst2 = inst.set_index(['Station_Name', 'Date2'])
            temp = inst2.reindex(four_index.index)
            temp['Station_E'] = pd.to_numeric(temp['Station_E'], errors='coerce')
            temp['Station_W'] = pd.to_numeric(temp['Station_W'], errors='coerce')
            temp.to_csv(input_dir + '/' + data_out2, index=True)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', '.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            temp.to_excel(writer, sheet_name='Sheet2', index=True)
            writer.save()

        for name in seven:
            data_out = name.replace('.csv', 'inst.csv')
            data_out2 = name.replace('.csv', 'inst_trim.csv')
            data_n = name
            data = pd.read_csv(input_dir + '/' + data_n)
            p = len(sevenm)
            inst = data.loc[data['PageName'].isin(sevenm)]  # 700m
            inst['Date2'] = inst['Date']
            inst['Station_E'] = np.nan
            inst['Station_W'] = np.nan
            inst.set_index(['Date'], inplace=True)
            p = len(sevenm)
            for q in range(0, p):
                inst.loc[inst['PageName'] == sevenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q] + '_E.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                print(inst.columns)
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_E',
                                    'Station_W', 'Station_Name']
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]
                # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst2 = inst.set_index(['Station_Name', 'Date2'])
            temp = inst2.reindex(four_index.index)
            temp['Station_E'] = pd.to_numeric(temp['Station_E'], errors='coerce')
            temp['Station_W'] = pd.to_numeric(temp['Station_W'], errors='coerce')
            print("##############################################################################################################################################")
            print(temp.dtypes)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv','.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            temp.to_excel(writer, sheet_name='Sheet2', index=True)
            inst.to_csv(input_dir + '/' + data_out, index=False)
            temp.to_csv(input_dir + '/' + data_out2, index=True)
            writer.save()





