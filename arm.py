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
era1_nvdi = ["MEAN_NDVI_2016_122","MEAN_NDVI__2016_142","MEAN_NDVI_2016_156","MEAN_NDVI__2016_175","MEAN_NDVI__2016_227","MEAN_NDVI__2016_241",
        "MEAN_NDVI__2016_255","MEAN_NDVI__2016_269","MEAN_NDVI__2016_283","MEAN_NDVI__2016_297","MEAN_NDVI__2016_311","MEAN_NDVI__2016_325",
        "MEAN_NDVI__2017_121","MEAN_NDVI__2017_135","MEAN_NDVI__2017_149","MEAN_NDVI__2017_163","MEAN_NDVI__2017_177","MEAN_NDVI__2017_191",
        "MEAN_NDVI__2017_205","MEAN_NDVI__2017_219","MEAN_NDVI_2017_233","MEAN_NDVI__2017_247","MEAN_NDVI__2017_261","MEAN_NDVI__2017_275",
        "MEAN_NDVI__2017_289","MEAN_NDVI__2017_303","MEAN_NDVI__2017_317","MEAN_NDVI__2017_331","MEAN_NDVI__2018_121","MEAN_NDVI__2018_135",
        "MEAN_NDVI__2018_149","MEAN_NDVI__2018_163","MEAN_NDVI__2018_177","MEAN_NDVI__2018_191","MEAN_NDVI__2018_205","MEAN_NDVI__2018_219",
        "MEAN_NDVI__2018_233","MEAN_NDVI__2018_247","MEAN_NDVI__2018_261","MEAN_NDVI__2018_275","MEAN_NDVI__2018_289","MEAN_NDVI__2018_303",
        "MEAN_NDVI__2018_317","MEAN_NDVI__2018_331","MEAN_NDVI__2019_121","MEAN_NDVI__2019_135","MEAN_NDVI__2019_149"]
era1_smerge = ["MEAN_Smerge_20160401","MEAN_Smerge_20160421","MEAN_Smerge_20160505","MEAN_Smerge_20160524","MEAN_Smerge_20160715","MEAN_Smerge_20170729"
    ,"MEAN_Smerge_20160812","MEAN_Smerge_20160826","MEAN_Smerge_20160909","MEAN_Smerge_20160923","MEAN_Smerge_20161007","MEAN_Smerge__20161021",
               "MEAN_Smerge_20170401","MEAN_Smerge_20170415","MEAN_Smerge_20170429","MEAN_Smerge_20170513","MEAN_Smerge_20170527","MEAN_Smerge_20170610",
               "MEAN_Smerge_20170624","MEAN_Smerge_20170708","MEAN_Smerge_20170722","MEAN_Smerge_20170805","MEAN_Smerge_20170819","MEAN_Smerge_20170902",
               "MEAN_Smerge_20170916","MEAN_Smerge_20170930","MEAN_Smerge_20171014","MEAN_Smerge_20171028","MEAN_Smerge_20180401","MEAN_Smerge_20180415",
               "MEAN_Smerge_20180429","MEAN_Smerge_20180513","MEAN_Smerge_20180527","MEAN_Smerge_20180610","MEAN_Smerge_20180624","MEAN_Smerge_20180708",
               "MEAN_Smerge_20180722","MEAN_Smerge_20180805","MEAN_Smerge_20180819","MEAN_Smerge_20180902","MEAN_Smerge_20180916","MEAN_Smerge_20180930",
               "MEAN_Smerge_20181014","MEAN_Smerge_20181028","MEAN_Smerge_20190401","MEAN_Smerge_20190415","MEAN_Smerge_20190429"]
doy = ["92","112","126","145","197","211","225","239","253","267","281","295","91","105","119","133","147","161","175","189","203","217",
       "231","245","259","273","287","301","91","105","119","133","147","161","175","189","203","217","231","245","259","273","287","301","91","105","119"]

date = ["4/1/2016","4/21/2016","5/5/2016","5/24/2016","7/15/2016","7/29/2016","8/12/2016","8/26/2016","9/9/2016","9/23/2016","10/7/2016","10/21/2016",
        "4/1/2017","4/15/2017","4/29/2017","5/13/2017","5/27/2017","6/10/2017","6/24/2017","7/8/2017","7/22/2017","8/5/2017","8/19/2017","9/2/2017",
        "9/16/2017","9/30/2017","10/14/2017","10/28/2017","4/1/2018","4/15/2018","4/29/2018","5/13/2018","5/27/2018","6/10/2018","6/24/2018","7/8/2018",
        "7/22/2018","8/5/2018","8/19/2018","9/2/2018","9/16/2018","9/30/2018","10/14/2018","10/28/2018","4/1/2019","4/15/2019","4/29/2019"]
k = 3
if k == 1:
    input_dir = "/mnt/d/ARM/Era1/ERA1_2/Static"
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
    index = pd.read_csv(os.path.join(input_dir,four[0]), usecols=["PageName"])
    static_400m = pd.DataFrame(index=index["PageName"])
    for f in four:
        temp = pd.read_csv(os.path.join(input_dir,f)).set_index("PageName")
        static_400m[f.split("_", 1)[0]] = temp['MEAN']
        print(f.split("_", 1)[0])
        static_400m.to_csv(input_dir+"/ARM_Static_400m.csv")
#########################################################################################################################################
    index = pd.read_csv(os.path.join(input_dir, seven[0]), usecols=["PageName"])
    static_700m = pd.DataFrame(index=index["PageName"])
    for s in seven:
        temp = pd.read_csv(os.path.join(input_dir,s)).set_index("PageName")
        static_700m[s.split("_", 1)[0]] = temp['MEAN']
        static_700m.to_csv(input_dir+"/ARM_Static_700m.csv")
#########################################################################################################################################
    index = pd.read_csv(os.path.join(input_dir, ten[0]), usecols=["PageName"])
    static_1000m = pd.DataFrame(index=index["PageName"])
    for t in ten:
        temp = pd.read_csv(os.path.join(input_dir,t)).set_index("PageName")
        static_1000m[t.split("_", 1)[0]] = temp['MEAN']
        static_1000m.to_csv(input_dir+"/ARM_Static_1000m.csv")
    k = 2
if k == 2:
    static_home = '/mnt/d/ARM/Era1/ERA1_2/Static/'
    ndvi_four = pd.read_csv("/mnt/d/ARM/Era1/ERA1_2/ndvi/ARM_1_2_NDVI_400.csv").set_index("PageName")
    ndvi_seven = pd.read_csv("/mnt/d/ARM/Era1/ERA1_2/ndvi/ARM_1_2_NDVI_700.csv").set_index("PageName")
    ndvi_ten = pd.read_csv("/mnt/d/ARM/Era1/ERA1_2/ndvi/ARM_1_2_NDVI_1000.csv").set_index("PageName")
    smerge_four = pd.read_csv('/mnt/d/ARM/Era1/smerge/ARM_1_2_SMERGE_400.csv').set_index("PageName")
    smerge_seven = pd.read_csv('/mnt/d/ARM/Era1/smerge/ARM_1_2_SMERGE_700.csv').set_index("PageName")
    smerge_ten = pd.read_csv('/mnt/d/ARM/Era1/smerge/ARM_1_2_SMERGE_1000.csv').set_index("PageName")
    lst_dir = '/mnt/d/LST/TXson'
    input_dir = "/mnt/d/ARM/Era1/ERA1_2/All_Data"
    four = []
    seven = []
    ten = []
    for f in os.listdir(input_dir):
        if f.endswith("400.csv"):
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
        if w.startswith("LST"):
            lst_four.append(os.path.join(input_dir, w))
    for t in seven:
        if t.startswith("ALB"):
            alb_seven.append(os.path.join(input_dir, t))
        if t.startswith("LAI"):
            lai_seven.append(os.path.join(input_dir, t))
        if t.startswith("LST"):
            lst_seven.append(os.path.join(input_dir, t))
    for h in ten:
        if h.startswith('ALB'):
            alb_ten.append(os.path.join(input_dir, h))
        if h.startswith('LAI'):
            lai_ten.append(os.path.join(input_dir, h))
        if h.startswith("LST"):
            lst_ten.append(os.path.join(input_dir, h))
    f_data = pd.DataFrame(columns=['SMERGE', 'Date','LST','LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt ', 'Slope', 'Elevation','Ascept'])
    #r = 110000
    r = 106150 #400m 16941
    static = pd.read_csv(static_home + "ARM_Static_400m.csv")
    print(lst_ten)
    for k in range(1,48):
        #print(lai_whole)
        current = pd.DataFrame(index=static["PageName"],columns=['SMERGE', 'Date','LST' , 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt ', 'Slope', 'Elevation', 'Ascept'] )
        index = static["PageName"]
        current['SMERGE'] = smerge_four[era1_smerge[k-1]]
        #lst_temp = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).dropna()
        #print(static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept','PageName']].set_index("PageName"))
        current['LST'] = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["LAI"] = pd.read_csv(lai_four[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current['LST'] = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["Albedo"] = pd.read_csv(alb_four[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current["NDVI"] = ndvi_four[era1_nvdi[k-1]]
        current[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept']] = static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept','PageName']].set_index("PageName")
        current['PageName'] = current.index
        current.index = range(current.shape[0])
        current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
        f_data = pd.concat([f_data, current])
        if k == 47:
            f_data.to_csv('ARM_400m_dataV1.csv')
    #r = 17500  # 1000m
    r = 16940 #1000m
    static = pd.read_csv(static_home + "ARM_Static_1000m.csv")
    f_data = pd.DataFrame(columns=['SMERGE', 'Date','LST' , 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt ', 'Slope', 'Elevation', 'Ascept'])
    for k in range(1,48):
        current = pd.DataFrame(index=static["PageName"],columns=['SMERGE', 'Date','LST' , 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt ', 'Slope', 'Elevation', 'Ascept'] )
        index = static["PageName"]
        print(k)
        #print(len(alb_hundred_m))
        current['SMERGE'] = smerge_ten[era1_smerge[k - 1]]
        #current['LST'] = pd.read_csv(lst_ten[k-1], usecols=["MEAN","PageName"]).sort_values(by=["PageName"]).drop("PageName",axis=1)
        #lst_temp = pd.read_csv(lst_ten[k - 1], usecols=["MEAN", "PageName"]).dropna()
        current['LST'] = pd.read_csv(lst_ten[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["LAI"] = pd.read_csv(lai_ten[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current['LST'] = pd.read_csv(lst_ten[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        print(lst_ten[k - 1])
        current["Albedo"] = pd.read_csv(alb_ten[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current["NDVI"] = ndvi_ten[era1_nvdi[k-1]]
        current[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept']] = static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept','PageName']].set_index("PageName")
        current['PageName'] = current.index
        current.index = range(current.shape[0])
        current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
        f_data = pd.concat([f_data, current])
        print(f_data[['LST', 'Date']])
        if k == 47:
            f_data.to_csv('ARM_1000m_dataV1.csv')
    #r = 37000 # 700m
    r = 34650 #700m
    static = pd.read_csv(static_home + "ARM_Static_700m.csv")
    current = pd.DataFrame(index=static["PageName"])
    index = static["PageName"]
    f_data = pd.DataFrame(columns=['SMERGE', 'Date','LST' , 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt ', 'Slope', 'Elevation', 'Ascept'])
    for k in range(1,48):
        current = pd.DataFrame(index=static["PageName"],columns=['SMERGE', 'Date','LST' , 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt ', 'Slope', 'Elevation', 'Ascept'] )
        index = static["PageName"]
        #print(w)
        #print(len(alb_thirty_m))
        current['SMERGE'] = smerge_seven[era1_smerge[k - 1]]
        current['LST'] = pd.read_csv(lst_seven[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["LAI"] = pd.read_csv(lai_seven[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current['LST'] = pd.read_csv(lst_seven[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["Albedo"] = pd.read_csv(alb_seven[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current["NDVI"] = ndvi_seven[era1_nvdi[k-1]]
        current[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept']] = static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept','PageName']].set_index("PageName")
        current['PageName'] = current.index
        current.index = range(current.shape[0])
        current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
        f_data = pd.concat([f_data,current])
        if k == 47:
            f_data.to_csv('ARM_700m_dataV1.csv')
            #k = 3
if k == 3:
    data = pd.read_csv('ARM_1000m_dataV1.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
    data1 = data1[~(data1[["LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept"]] < 0).any(axis=1)]
    data1 = data1.dropna()
    data1.to_csv('ARM_1000m_data_p.csv', index=False)
    #######################################################################################################
    data = pd.read_csv('ARM_700m_dataV1.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
    data1 = data1[~(data1[["LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept"]] < 0).any(axis=1)]
    data1 = data1.dropna()
    data1.to_csv('ARM_700m_data_p.csv', index=False)
    #####################################################################################################
    data = pd.read_csv('ARM_400m_dataV1.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
    data1 = data1[~(data1[["LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept"]] < 0).any(axis=1)]
    data1 = data1.dropna()
    data1.to_csv('ARM_400m_data_p.csv', index=False)
    k = 4
if k == 4:
    fourm = ["AX164","CL352","J70","DI534","DO147","FW240","AF301","CX18"]
    sevenm = ["E40","R172","AB94","AY201","BF10","BM306","BP84","CX137"]
    tenm = ["D28","M121","T66","AJ141","AO7","AS214","AV59","BT96"]
    # data = pd.read_csv('TX_400m_data_p.csv')
    # df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    # inst = df_train.loc[df_train['PageName'].isin(fourm)]#400m
    # df_train = df_train.loc[~df_train['PageName'].isin(fourm)]#400m
    # inst = df_train.loc[df_train['PageName'].isin(sevenm)] #700m
    # df_train = df_train.loc[~df_train['PageName'].isin(sevenm)]  # 700m
    data = pd.read_csv('ARM_700m_data_p.csv', usecols=["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"])
    #data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(sevenm)] #700m
    df_test = pd.concat([df_test, inst])
    df_train.to_csv('ARM_700m_dataV1_train.csv', index=False)
    df_test.to_csv('ARM_700m_dataV1_test.csv', index=False)
    ###################################################################################################
    data = pd.read_csv('ARM_1000m_data_p.csv',usecols=["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"])
    #data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(tenm)]  # 1000m
    df_train = df_train.loc[~df_train['PageName'].isin(tenm)]  # 1000m
    df_test = pd.concat([df_test,inst])
    df_train.to_csv('ARM_1000m_dataV1_train.csv', index=False)
    df_test.to_csv('ARM_1000m_dataV1_test.csv', index=False)
    ####################################################################################################
    data = pd.read_csv('ARM_400m_data_p.csv',usecols=["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"])
    #data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(fourm)]  # 1000m
    df_train = df_train.loc[~df_train['PageName'].isin(fourm)]  # 1000m
    df_test = pd.concat([df_test, inst])
    df_train.to_csv('ARM_400m_dataV1_train.csv', index=False)
    df_test.to_csv('ARM_400m_dataV1_test.csv', index=False)
    print("Completel donnnnnnnnnnnnnnnn")
    #k = 5
if k == 5:
    fourm = ["AX164", "CL352", "J70", "DI534", "DO147", "FW240", "AF301", "CX18"]
    sevenm = ["E40", "R172", "AB94", "AY201", "BF10", "BM306", "BP84", "CX137"]
    tenm = ["D28", "M121", "T66", "AJ141", "AO7", "AS214", "AV59", "BT96"]
    data = pd.read_csv('ARM_1000m_data_p.csv')
    df1, df2 = train_test_split(data, test_size=0.30, random_state=42)
    df_train, df_test = train_test_split(df2, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(tenm)]  # 1000m
    df_train = df_train.loc[~df_train['PageName'].isin(tenm)]  # 1000m
    df_test = pd.concat([df_test, inst])
    df_train.to_csv('ARM_1000m_dataV1_train.csv', index=False)
    df_test.to_csv('ARM_1000m_dataV1_test.csv', index=False)
if k == 6:
    fourm = ["AX164", "CL352", "J70", "DI534", "DO147", "FW240", "AF301", "CX18"]
    sevenm = ["E40", "R172", "AB94", "AY201", "BF10", "BM306", "BP84", "CX137"]
    tenm = ["D28", "M121", "T66", "AJ141", "AO7", "AS214", "AV59", "BT96"]
    data = pd.read_csv('RF_v1_ARM_ERA11_1000m7030.csv')
    # inst = data.loc[data['PageName'].isin(fourm)]  # 400m
    inst = data.loc[data['PageName'].isin(tenm)]#1000m
    #inst = data.loc[data['PageName'].isin(sevenm)] #700m
    inst.to_csv('RF_v1_ARM_1000mInst.csv', index=False)