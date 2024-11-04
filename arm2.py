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
k = -6
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
o = '2'
if k == 2:
    #o = '2'
    static_home = '/mnt/d/ARM/Era1/ERA1_'+o+'/Static/'
    ndvi_four = pd.read_csv("/mnt/d/ARM/Era1/ERA1_"+o+"/ndvi/ARM_1_"+o+"_NDVI_400.csv").set_index("PageName")
    ndvi_seven = pd.read_csv("/mnt/d/ARM/Era1/ERA1_"+o+"/ndvi/ARM_1_"+o+"_NDVI_700.csv").set_index("PageName")
    ndvi_ten = pd.read_csv("/mnt/d/ARM/Era1/ERA1_"+o+"/ndvi/ARM_1_"+o+"_NDVI_1000.csv").set_index("PageName")
    smerge_four = pd.read_csv('/mnt/d/ARM/Era1/smerge/ARM_1_'+o+'_SMERGE_400.csv').set_index("PageName")
    smerge_seven = pd.read_csv('/mnt/d/ARM/Era1/smerge/ARM_1_'+o+'_SMERGE_700.csv').set_index("PageName")
    smerge_ten = pd.read_csv('/mnt/d/ARM/Era1/smerge/ARM_1_'+o+'_SMERGE_1000.csv').set_index("PageName")
    input_dir = "/mnt/d/ARM/Era1/ERA1_"+o+"/All_Data"
    four = []
    seven = []
    ten = []
    for f in os.listdir(input_dir):
        if f.endswith("_400.csv"):
            four.append(f)
        if f.endswith("700.csv"):
            seven.append(f)
        if f.endswith("1000.csv"):
            ten.append(f)
    four = natsorted(four)
    seven = natsorted(seven)
    ten = natsorted(ten)
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
    f_data = pd.DataFrame(columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', ('%s' % 'Silt'), 'Slope', 'Elevation', 'Ascept'])
    #r = 110000
    r = 106150 #400m 16941
    static = pd.read_csv(static_home + "ARM_Static_400m.csv")
    for k in range(1,48):
        print(lst_four[k - 1])
        current = pd.DataFrame(index=static["PageName"], columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand',
                                                                  ('%s' % 'Silt'), 'Slope', 'Elevation', 'Ascept'])
        index = static["PageName"]
        current['SMERGE'] = smerge_four[era1_smerge[k-1]]
        #lst_temp = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).dropna()
        #print(static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept','PageName']].set_index("PageName"))
        current['Temp'] = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["LAI"] = pd.read_csv(lai_four[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current['Temp'] = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["Albedo"] = pd.read_csv(alb_four[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current["NDVI"] = ndvi_four[era1_nvdi[k-1]]
        current[['Clay' ,'Sand' , ('%s' % 'Silt'), 'Slope' , 'Elevation' , 'Ascept']] = static[['Clay' , 'Sand' ,
                                                                                               ('%s' % 'Silt'), 'Slope' , 'Elevation' , 'Ascept', 'PageName']].set_index("PageName")
        current['PageName'] = current.index
        current.index = range(current.shape[0])
        current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
        f_data = pd.concat([f_data, current])
        if k == 47:
            f_data.to_csv('ARM_400m_dataV1_Era1_'+str(o)+'.csv')
    #r = 17500  # 1000m
    r = 16940 #1000m
    static = pd.read_csv(static_home + "ARM_Static_1000m.csv")
    f_data = pd.DataFrame(columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', ('%s' % 'Silt'), 'Slope', 'Elevation', 'Ascept'])
    for k in range(1,48):
        current = pd.DataFrame(index=static["PageName"], columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand',
                                                                  ('%s' % 'Silt'), 'Slope', 'Elevation', 'Ascept'])
        index = static["PageName"]
        print(k)
        #print(len(alb_hundred_m))
        current['SMERGE'] = smerge_ten[era1_smerge[k - 1]]
        #current['LST'] = pd.read_csv(lst_ten[k-1], usecols=["MEAN","PageName"]).sort_values(by=["PageName"]).drop("PageName",axis=1)
        #lst_temp = pd.read_csv(lst_ten[k - 1], usecols=["MEAN", "PageName"]).dropna()
        current['Temp'] = pd.read_csv(lst_ten[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        current["LAI"] = pd.read_csv(lai_ten[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current['Temp'] = pd.read_csv(lst_ten[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
        print(lst_ten[k - 1])
        current["Albedo"] = pd.read_csv(alb_ten[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current["NDVI"] = ndvi_ten[era1_nvdi[k-1]]
        current[['Clay' ,'Sand' , ('%s' % 'Silt'), 'Slope' , 'Elevation' , 'Ascept']] = static[['Clay' , 'Sand' ,
                                                                                               ('%s' % 'Silt'), 'Slope' , 'Elevation' , 'Ascept', 'PageName']].set_index("PageName")
        current['PageName'] = current.index
        current.index = range(current.shape[0])
        current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
        f_data = pd.concat([f_data, current])
        print(f_data[['Temp', 'Date']])
        if k == 47:
            f_data.to_csv('ARM_1000m_dataV1_Era1_'+str(o)+'.csv')
    #r = 37000 # 700m
    r = 34650 #700m
    static = pd.read_csv(static_home + "ARM_Static_700m.csv")
    current = pd.DataFrame(index=static["PageName"])
    index = static["PageName"]
    f_data = pd.DataFrame(columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', ('%s' % 'Silt'), 'Slope', 'Elevation', 'Ascept'])
    for k in range(1,48):
        current = pd.DataFrame(index=static["PageName"], columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand',
                                                                  ('%s' % 'Silt'), 'Slope', 'Elevation', 'Ascept'])
        index = static["PageName"]
        #print(w)
        #print(len(alb_thirty_m))
        current['SMERGE'] = smerge_seven[era1_smerge[k - 1]]
        current['Temp'] = pd.read_csv(lst_seven[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
        current["LAI"] = pd.read_csv(lai_seven[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current['Temp'] = pd.read_csv(lst_seven[k - 1], usecols=["MEAN", "PageName"]).dropna().set_index("PageName")
        current["Albedo"] = pd.read_csv(alb_seven[k-1],  usecols=["MEAN","PageName"]).set_index("PageName")
        current["NDVI"] = ndvi_seven[era1_nvdi[k-1]]
        current[['Clay' ,'Sand' , ('%s' % 'Silt'), 'Slope' , 'Elevation' , 'Ascept']] = static[['Clay' , 'Sand' ,
                                                                                               ('%s' % 'Silt'), 'Slope' , 'Elevation' , 'Ascept', 'PageName']].set_index("PageName")
        current['PageName'] = current.index
        current.index = range(current.shape[0])
        current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
        f_data = pd.concat([f_data,current])
        if k == 47:
            f_data.to_csv('ARM_700m_dataV1_Era1_'+str(o)+'.csv')
            k = 3
if k == 3:
    #o = 2
    data = pd.read_csv('ARM_1000m_dataV1_Era1_'+str(o)+'.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
    data1 = data1[~(data1[["LAI","Albedo","NDVI","Clay","Sand", 'Silt', "Slope", "Elevation", "Ascept"]] < 0).any(axis=1)]
    data1 = data1.dropna()
    data1.to_csv('ARM_1000m_data_pEra1'+str(o)+'.csv', index=False)
    #######################################################################################################
    data = pd.read_csv('ARM_700m_dataV1_Era1_'+str(o)+'.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
    data1 = data1[~(data1[["LAI","Albedo","NDVI","Clay","Sand", 'Silt', "Slope", "Elevation", "Ascept"]] < 0).any(axis=1)]
    data1 = data1.dropna()
    data1.to_csv('ARM_700m_data_pEra1'+str(o)+'.csv', index=False)
    #####################################################################################################
    data = pd.read_csv('ARM_400m_dataV1_Era1_'+str(o)+'.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
    data1 = data1[~(data1[["LAI","Albedo","NDVI","Clay","Sand", 'Silt', "Slope", "Elevation", "Ascept"]] < 0).any(axis=1)]
    data1 = data1.dropna()
    data1.to_csv('ARM_400m_data_pEra1'+str(o)+'.csv', index=False)
    k = 4
if k == 4:
    #o = 2
    if o == '1':
        fourm = ["AX164", "CL352", "J70", "DI534", "DO147", "FW240", "AF301", "CX18"]  # Era 11
        sevenm = ["E40", "R172", "AB94", "AY201", "BF10", "BM306", "BP84", "CX137"]
        tenm = ["D28", "M121", "T66", "AJ141", "AO7", "AS214", "AV59", "BT96"]
    if o == '2':
        fourm = ["FI346", "G8", "AN107", "CP223", "W346", "FD39"]  # Era12
        sevenm = ["D5", "BB128", "CN22", "W61", "CQ198", "M198"]
        tenm = ["BN139", "C4", "I139", "P43", "BL16", "AL89"]
    # data = pd.read_csv('TX_400m_data_p.csv')
    # df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    # inst = df_train.loc[df_train['PageName'].isin(fourm)]#400m
    # df_train = df_train.loc[~df_train['PageName'].isin(fourm)]#400m
    # inst = df_train.loc[df_train['PageName'].isin(sevenm)] #700m
    # df_train = df_train.loc[~df_train['PageName'].isin(sevenm)]  # 700m
    data = pd.read_csv('ARM_700m_data_pEra1'+str(o)+'.csv', usecols=["SMERGE","Date", ("%s" % 'Temp'), "LAI", "Albedo", "NDVI", "Clay", "Sand",
                                                            ("%s" % 'Silt'), "Slope", "Elevation", "Ascept", "PageName"])
    #data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(sevenm)] #700m
    df_test = pd.concat([df_test, inst])
    df_train.to_csv('Era1_'+str(o)+'ARM_700m_dataV1_train.csv', index=False)
    df_test.to_csv('Era1_'+str(o)+'ARM_700m_dataV1_test.csv', index=False)
    ###################################################################################################
    data = pd.read_csv('ARM_1000m_data_pEra1'+str(o)+'.csv', usecols=["SMERGE","Date", ("%s" % 'Temp'), "LAI", "Albedo", "NDVI", "Clay", "Sand",
                                                             'Silt', "Slope", "Elevation", "Ascept", "PageName"])
    #data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(tenm)]  # 1000m
    df_train = df_train.loc[~df_train['PageName'].isin(tenm)]  # 1000m
    df_test = pd.concat([df_test,inst])
    df_train.to_csv('Era1_'+str(o)+'ARM_1000m_dataV1_train.csv', index=False)
    df_test.to_csv('Era1_'+str(o)+'ARM_1000m_dataV1_test.csv', index=False)
    ####################################################################################################
    data = pd.read_csv('ARM_400m_data_pEra1'+str(o)+'.csv', usecols=["SMERGE","Date", ("%s" % 'Temp'), "LAI", "Albedo", "NDVI", "Clay", "Sand",
                                                            'Silt', "Slope", "Elevation", "Ascept", "PageName"])
    #data.columns = ["SMERGE","Date","LST","LAI","Albedo","NDVI","Clay","Sand","Silt ","Slope","Elevation","Ascept","PageName"]
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(fourm)]  # 1000m
    df_train = df_train.loc[~df_train['PageName'].isin(fourm)]  # 1000m
    df_test = pd.concat([df_test, inst])
    df_train.to_csv('Era1_'+str(o)+'ARM_400m_dataV1_train.csv', index=False)
    df_test.to_csv('Era1_'+str(o)+'ARM_400m_dataV1_test.csv', index=False)
    print("Completel donnnnnnnnnnnnnnnn")
    #k = 5
if k == -64352: #Era1_1
    fourm = ['J70','AF301','CX18','FW240','AX164','DO147','CL352','DI534']
    sevenm = ['E40','R172','BF10','CX137','AB94','BP84','AY201','BM306']
    tenm = ['D28','M121','AO7','BT96','T66','AV59','AJ141','AS214']
    fourteenm = ['C20','I86','AC5','AY69','N47','AH42','Z101','AG153']
    name = ['Anthony','Ashton','Bryon','Lamont-CF1','MapleCity','Medford','Newkirk','Pawhuska']
    files = ['RF_v4_ARM_ERA11_400m.csv','RF_v4_ARM_ERA11_700m.csv','RF_v4_ARM_ERA11_1000m.csv','RF_v4_ARM_ERA11_1400m.csv']
    for f in files:
        data = pd.read_csv('/mnt/d/ARM/Fontera/ARM1/Era1_1/ML/'+f)
        print('/mnt/d/ARM/Fontera/ARM1/Era1_1/ML/'+f)
        if '_1400m' in f:
            inst = data.loc[data['PageName'].isin(fourteenm)]  # 1400m
        if '_1000m' in f:
            inst = data.loc[data['PageName'].isin(tenm)]  # 1000m
        if '_700m' in f:
            inst = data.loc[data['PageName'].isin(sevenm)]  # 700m
        if '_400m':
            inst = data.loc[data['PageName'].isin(fourm)]  # 400m
        inst.to_csv(f.replace('m.csv','m_Inst.csv'), index=False)

if k == -61111: #Era1_2
    fourm = ["FI346","G8","AN107","CP223","W346","FD39"]
    sevenm = ["D5","BB128","CN22","W61","CQ198","M198"]
    tenm = ["BN139","C4","I139","P43","BL16","AL89"]
    data = pd.read_csv('Era12_ABR_1000m_SSv5_r2.csv')
    #inst = data.loc[data['PageName'].isin(fourm)]  # 400m
    inst = data.loc[data['PageName'].isin(tenm)]#1000m
    #inst = data.loc[data['PageName'].isin(sevenm)] #700m
    inst.to_csv('Era12_ABR_1000m_Inst.csv', index=False)

if k == 6:
    fourm = ["O21", "BS589", "EK306", "HJ528"]  # Era32
    sevenm = ["I12", "AO337", "CC175", "DU302"]
    tenm = ["F9", "AC236", "BE123", "CI212"]
    names = ["Coldwater", "Ashton", "Byron", "Lamont-CF1"]  # Era32
    data = pd.read_csv('RF_v4_ARM_ERA32_400m.csv')
    inst = data.loc[data['PageName'].isin(fourm)]  # 400m
    # inst = data.loc[data['PageName'].isin(tenm)]#1000m
    # inst = data.loc[data['PageName'].isin(sevenm)]  # 700m
    inst.to_csv('RF_v4_ARM_ERA32_400mInst.csv', index=False)

if k == -6:
    type = "RF"
    era = [1,2]
    era_s = ["ERA11", "ERA12"]
    for e in era:
        four = []
        seven = []
        ten = []
        fourteen = []
        input_dir = '/mnt/d/ARM/Fontera/ARM1_V4/Era1_' + str(e) + '/ML'
        for f in os.listdir(input_dir):
            if era_s[e - 1] in f:
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
            inst_dir = '/mnt/d/ARM/Era1/ARM1_CSV/ARM_1_'
        if e == 1:
            fourm = ['J70', 'AF301', 'CX18', 'FW240', 'AX164', 'DO147', 'CL352', 'DI534']
            sevenm = ['E40', 'R172', 'BF10', 'CX137', 'AB94', 'BP84', 'AY201', 'BM306']
            tenm = ['D28', 'M121', 'AO7', 'BT96', 'T66', 'AV59', 'AJ141', 'AS214']
            fourteenm = ['C20', 'I86', 'AC5', 'AY69', 'N47', 'AH42', 'Z101', 'AG153']
            names = ['Anthony', 'Ashton', 'Bryon', 'Lamont-CF1', 'MapleCity', 'Medford', 'Newkirk', 'Pawhuska']#Era1_1
        if e == 2:
            fourm = ['CP223', 'W346', 'FD39', 'G8', 'FI346', 'AN107']
            sevenm = ['BB128', 'M198', 'CN22', 'D5', 'CQ198', 'W61']
            tenm = ['AL89', 'I139', 'BL16', 'C4', 'BN139', 'P43']
            fourteenm = ['AA64', 'G99', 'AT11', 'B3', 'AV99', 'L31']
            names = ['Marshall', 'Morrison', 'Omega', 'Ringwood', 'Tyron', 'Waukomis']  # Era1_2
        for name in four:
            data_n = name
            data_out = name.replace('.csv', 'inst.csv')
            data = pd.read_csv(input_dir + '/' + data_n)
            inst = data.loc[data['PageName'].isin(fourm)]  # 400m
            p = len(fourm)
            inst = data.loc[data['PageName'].isin(fourm)]  # 1000m
            inst['Date2'] = inst['Date']
            inst['Station_E'] = np.nan
            inst['Station_W'] = np.nan
            inst['Station_S'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == fourm[q], ['Station_Name']] = names[q]
                    # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q] + '_E.csv').dropna(subset=['Date']).rename(columns={"Date": "Date"}).set_index("Date")
                print(inst.columns)
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Date']).rename(columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_S.csv').dropna(subset=['Date']).rename(columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_S']] = inst_data['Value']
                try:
                    inst = inst[['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                             'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                        'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_E',
                                        'Station_W', 'Station_S', 'Station_Name']
                    print(inst.columns)
                    inst = inst[
                            ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                             'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_E'] = pd.to_numeric(inst['Station_E'], errors='coerce')
            inst['Station_W'] = pd.to_numeric(inst['Station_W'], errors='coerce')
            inst['Station_S'] = pd.to_numeric(inst['Station_S'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
                # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', 'Fixed4.xlsx'), engine='xlsxwriter')
                # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()
        for name in ten:
            data_n = name
            data_out = name.replace('.csv', 'inst.csv')
            data = pd.read_csv(input_dir + '/' + data_n)
            inst = data.loc[data['PageName'].isin(tenm)]  # 400m
            p = len(tenm)
            inst = data.loc[data['PageName'].isin(tenm)]  # 1000m
            inst['Date2'] = inst['Date']
            inst['Station_E'] = np.nan
            inst['Station_W'] = np.nan
            inst['Station_S'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q] + '_E.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_S.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_S']] = inst_data['Value']
                print(inst)
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_E',
                                    'Station_W', 'Station_S', 'Station_Name']
                    print(inst)
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_E'] = pd.to_numeric(inst['Station_E'], errors='coerce')
            inst['Station_W'] = pd.to_numeric(inst['Station_W'], errors='coerce')
            inst['Station_S'] = pd.to_numeric(inst['Station_S'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', '.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()

        for name in fourteen:
            data_n = name
            data_out = name.replace('.csv', 'inst.csv')
            data = pd.read_csv(input_dir + '/' + data_n)
            inst = data.loc[data['PageName'].isin(fourteenm)]  # 400m
            p = len(fourteenm)
            inst = data.loc[data['PageName'].isin(fourteenm)]  # 1000m
            inst['Date2'] = inst['Date']
            inst['Station_E'] = np.nan
            inst['Station_W'] = np.nan
            inst['Station_S'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):

                inst.loc[inst['PageName'] == fourteenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q] + '_E.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_S.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_S']] = inst_data['Value']
                print(inst.loc[inst['Station_Name'] == names[q], ['Station_S']])
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_E',
                                    'Station_W', 'Station_S', 'Station_Name']
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_E'] = pd.to_numeric(inst['Station_E'], errors='coerce')
            inst['Station_W'] = pd.to_numeric(inst['Station_W'], errors='coerce')
            inst['Station_S'] = pd.to_numeric(inst['Station_S'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', '.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()

        for name in seven:
            data_n = name
            data_out = name.replace('.csv', 'inst.csv')
            data = pd.read_csv(input_dir + '/' + data_n)
            inst = data.loc[data['PageName'].isin(sevenm)]  # 400m
            p = len(sevenm)
            inst = data.loc[data['PageName'].isin(sevenm)]  # 1000m
            inst['Date2'] = inst['Date']
            inst['Station_E'] = np.nan
            inst['Station_W'] = np.nan
            inst['Station_S'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == sevenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q] + '_E.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                print(inst.columns)
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_S.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_S']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_E',
                                    'Station_W', 'Station_S', 'Station_Name']
                    print(inst.columns)
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_E'] = pd.to_numeric(inst['Station_E'], errors='coerce')
            inst['Station_W'] = pd.to_numeric(inst['Station_W'], errors='coerce')
            inst['Station_S'] = pd.to_numeric(inst['Station_S'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', '.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()
