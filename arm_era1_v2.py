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
       "231","245","259","273","287","301","91","105","119","133","147","161","175","189","203","217","231","245","259","273","287","301","91","105","119"] #era1
# doy = ["121","135","149","163","177","191","205","242","256","270","283","326","122","136","151","165","179","199","213","227","241","255","269","283",
#        "297","311","325","121","135","149","163","177","191","209","224","238","264","278","293","307","321","121","135","218","248","268","282","296","310","324","201","255"] #era3

date = ["4/1/2016","4/21/2016","5/5/2016","5/24/2016","7/15/2016","7/29/2016","8/12/2016","8/26/2016","9/9/2016","9/23/2016","10/7/2016","10/21/2016",
        "4/1/2017","4/15/2017","4/29/2017","5/13/2017","5/27/2017","6/10/2017","6/24/2017","7/8/2017","7/22/2017","8/5/2017","8/19/2017","9/2/2017",
        "9/16/2017","9/30/2017","10/14/2017","10/28/2017","4/1/2018","4/15/2018","4/29/2018","5/13/2018","5/27/2018","6/10/2018","6/24/2018","7/8/2018",
        "7/22/2018","8/5/2018","8/19/2018","9/2/2018","9/16/2018","9/30/2018","10/14/2018","10/28/2018","4/1/2019","4/15/2019","4/29/2019"] #era1
# date = ["4/1/2003","4/15/2003","4/29/2003","5/13/2003","5/27/2003","6/10/2003","6/24/2003","7/31/2003","8/14/2003","8/28/2003","9/10/2003","10/23/2003","4/1/2004","4/15/2004",
#         "4/30/2004","5/14/2004","5/28/2004","6/17/2004","7/1/2004","7/15/2004","7/29/2004","8/12/2004","8/26/2004","9/9/2004","9/23/2004","10/7/2004","10/21/2004","4/1/2005",
#         "4/15/2005","4/29/2005","5/13/2005","5/27/2005","6/10/2005","6/28/2005","7/13/2005","7/27/2005","8/22/2005","9/5/2005","9/20/2005","10/4/2005","10/18/2005","4/1/2006",
#         "4/15/2006","7/7/2006","8/6/2006","8/26/2006","9/9/2006","9/23/2006","10/7/2006","10/21/2006","6/20/2007","8/13/2007"] #era3
k = 2
if k == 1:
    input_dir = "/mnt/d/ARM/Era1/ERA1_2/Static_1400"
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
    #k = 2
eras = ['1', '2']
if k == 2:
    for era in eras:
        static_home = '/mnt/d/ARM/Era1/ERA1_' + era +'/Static_1400/'
        lst_dir = '/mnt/d/%s/TXson' % 'Temp'
        input_dir = '/mnt/d/ARM/Era1/ERA1_' + era +'/All_Data'
        fourteen = []
        for f in os.listdir(input_dir):
            if f.endswith("1400.csv"):
                fourteen.append(f)
        fourteen = natsorted(fourteen)
        alb_fourteen = []
        lai_fourteen = []
        lst_fourteen = []
        ndvi_fourteen = []
        smerge_fourteen = []
        for w in fourteen:
            if w.startswith("ALB"):
                alb_fourteen.append(os.path.join(input_dir, w))
            if w.startswith("LAI"):
                lai_fourteen.append(os.path.join(input_dir, w))
            if w.startswith("Prism"):
                lst_fourteen.append(os.path.join(input_dir, w))
            if w.startswith("NDVI"):
                ndvi_fourteen.append(os.path.join(input_dir, w))
            if w.startswith("Smerge"):
                smerge_fourteen.append(os.path.join(input_dir, w))

        f_data = pd.DataFrame(
            columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope', 'Elevation',
                     'Aspect'])
        # r = 110000
        r = 106150  # 400m 16941
        static = pd.read_csv(static_home + "ARM_Static_1400m.csv")
        for k in range(1, 48):

            current = pd.DataFrame(index=static["PageName"],
                                   columns=['SMERGE', 'Date', 'Temp', 'LAI', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt',
                                            'Slope', 'Elevation', 'Aspect'])
            index = static["PageName"]
            current['SMERGE'] = pd.read_csv(smerge_fourteen[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
            # lst_temp = pd.read_csv(lst_four[k - 1], usecols=["MEAN", "PageName"]).dropna()
            # print(static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept','PageName']].set_index("PageName"))
            current['Temp'] = pd.read_csv(lst_fourteen[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
            current["LAI"] = pd.read_csv(lai_fourteen[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
            current['Temp'] = pd.read_csv(lst_fourteen[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
            current["Albedo"] = pd.read_csv(alb_fourteen[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
            current["NDVI"] = pd.read_csv(ndvi_fourteen[k - 1], usecols=["MEAN", "PageName"]).set_index("PageName")
            print(ndvi_fourteen[k - 1])
            current[['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Aspect']] = static[
                ['Clay', 'Sand', 'Silt', 'Slope', 'Elevation', 'Aspect', 'PageName']].set_index("PageName")
            current['PageName'] = current.index
            current.index = range(current.shape[0])
            current["Date"] = pd.DataFrame(date[k - 1], columns=['Date'], index=range(current.shape[0]))
            f_data = pd.concat([f_data, current])
            if k == 47:
                f_data.to_csv('ARM_1400m_dataV1_Era1' + era +'.csv')
    #k = 3
if k == 3:
    for era in eras:
        data = pd.read_csv('ARM_1400m_dataV1_Era1' + era +'.csv')
        data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Aspect'] > 0)]
        data1 = data1[
            ~(data1[["LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation", "Aspect"]] < 0).any(axis=1)]
        data1 = data1.dropna()
        data1.to_csv('ARM_1400m_data_pEra1' + era +'.csv', index=False)
    k = 4
if k == 4:
    h = [1,2]
    for o in h:
        # fourm = ["AX164","CL352","J70","DI534","DO147","FW240","AF301","CX18"] #Era 11
        # sevenm = ["E40","R172","AB94","AY201","BF10","BM306","BP84","CX137"]
        # tenm = ["D28","M121","T66","AJ141","AO7","AS214","AV59","BT96"]
        if o == 1:
            fourm = ["AN597", "BQ37", "EI311", "FM675"]  # Era31
            sevenm = ["X341", "AN21", "CB178", "CS386"]
            tenm = ["P239", "AB15", "BD125", "BP270"]
            fourteenm = ['C20','I86','N47','Z101','AC5','AG153','AH42','AY69']
        if o == 2:
            fourm = ["O21", "BS589", "EK306", "HJ528"]  # Era32
            sevenm = ["I12", "AO337", "CC175", "DU302"]
            tenm = ["F9", "AC236", "BE123", "CI212"]
            fourteenm = ['B3','G99','L31','AA64','AT11','AV99']
        data = pd.read_csv('ARM_1400m_data_pEra1'+str(o)+'.csv',
                           usecols=["SMERGE", "Date", ("%s" % 'Temp'), "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope",
                                    "Elevation", "Aspect", "PageName"])
        data.columns = ["SMERGE", "Date", ("%s" % 'Temp'), "LAI", "Albedo", "NDVI", "Clay", "Sand", "Silt", "Slope", "Elevation",
                        "Ascept", "PageName"]
        df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
        inst = df_train.loc[df_train['PageName'].isin(fourteenm)]  # 700m
        df_train = df_train.loc[~df_train['PageName'].isin(fourteenm)]  # 700m
        df_test = pd.concat([df_test, inst])
        df_train.to_csv('Era1_' + str(o) + 'ARM_1400m_dataV1_train.csv', index=False)
        df_test.to_csv('Era1_' + str(o) + 'ARM_1400m_dataV1_test.csv', index=False)
        ###################################################################################################
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