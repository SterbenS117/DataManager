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

k = -4
if k == -4:
    fourm = ["A31", "B4", "E30", "G32", "H42", "I27", "J27", "J40", "J49", "J95", "K42", "L48", "M29", "M42", "M43",
             "N29", "N43", "S96", "AI25", "AL96", "AR52",
             "AW59", "AY60", "AY75", "BA64", "BA65", "BG72", "BH69", "BH72", "BI70", "BI72", "BK52", "BK70", "BK92",
             "BM52", "BM69", "BS34", "BU84", "CD95", "CF2"]
    sevenm = ["A3", "A18", "C17", "D18", "E24", "F16", "F23", "F24", "F28", "F55", "G28", "H17", "H24", "H25", "K55",
              "T14", "V55", "Z30", "AB34", "AC34", "AC43", "AE37",
              "AH41", "AI40", "AI41", "AJ30", "AJ40", "AJ53", "AK40", "AL30", "AO20", "AP48", "AU55", "AV1"]
    tenm = ["A2", "A13", "C12", "C13", "D11", "D17", "E11", "E16", "E17", "E20", "E38", "F12", "F17", "F20", "H39",
            "O10", "P39", "R21", "T24", "U24", "U30", "V26",
            "X29", "Y28", "Y29", "Z21", "Z28", "Z37", "AA21", "AA28", "AC14", "AD34", "AH1", "AH38"]
    data = pd.read_csv('RF_v2-6_TXson1_1000m7030.csv')
    # inst = data.loc[data['PageName'].isin(fourm)]  # 400m
    inst = data.loc[data['PageName'].isin(tenm)]#1000m
    #inst = data.loc[data['PageName'].isin(sevenm)] #700m
    inst.to_csv('RF_v2-6_TXson1_1000mInst.csv', index=False)
if k == -2:
    data = pd.read_csv('TX_1000m_dataV4.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
    data1 = data1.dropna()
    data1.to_csv('TX_1000m_data_p.csv', index=False)
    #######################################################################################################
    data = pd.read_csv('TX_700m_dataV4.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
    data1 = data1.dropna()
    data1.to_csv('TX_700m_data_p.csv', index=False)
    #####################################################################################################
    data = pd.read_csv('TX_400m_dataV4.csv')
    data1 = data[(data['LAI'] <= 249) & (data['Albedo'] != 32767) & (data['Ascept'] > 0)]
    data1 = data1.dropna()
    data1.to_csv('TX_400m_data_p.csv', index=False)
    k = -3
if k == -3:
    fourm = ["A31","B4","E30","G32","H42","I27","J27","J40","J49","J95","K42","L48","M29","M42","M43","N29","N43","S96","AI25","AL96","AR52",
         "AW59","AY60","AY75","BA64","BA65","BG72","BH69","BH72","BI70","BI72","BK52","BK70","BK92","BM52","BM69","BS34","BU84","CD95","CF2"]
    sevenm = ["A3","A18","C17","D18","E24","F16","F23","F24","F28","F55","G28","H17","H24","H25","K55","T14","V55","Z30","AB34","AC34","AC43","AE37",
         "AH41","AI40","AI41","AJ30","AJ40","AJ53","AK40","AL30","AO20","AP48","AU55","AV1"]
    tenm = ["A2","A13","C12","C13","D11","D17","E11","E16","E17","E20","E38","F12","F17","F20","H39","O10","P39","R21","T24","U24","U30","V26",
         "X29","Y28","Y29","Z21","Z28","Z37","AA21","AA28","AC14","AD34","AH1","AH38"]
    # data = pd.read_csv('TX_400m_data_p.csv')
    # df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    # inst = df_train.loc[df_train['PageName'].isin(fourm)]#400m
    # df_train = df_train.loc[~df_train['PageName'].isin(fourm)]#400m
    # inst = df_train.loc[df_train['PageName'].isin(sevenm)] #700m
    # df_train = df_train.loc[~df_train['PageName'].isin(sevenm)]  # 700m
    data = pd.read_csv('TX_700m_data_p.csv')
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(sevenm)] #700m
    df_test = pd.concat([df_test, inst])
    df_train.to_csv('TX_700m_dataV3_train.csv', index=False)
    df_test.to_csv('TX_700m_dataV3_test.csv', index=False)
    ###################################################################################################
    data = pd.read_csv('TX_1000m_data_p.csv')
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(tenm)]  # 1000m
    df_train = df_train.loc[~df_train['PageName'].isin(tenm)]  # 1000m
    df_test = pd.concat([df_test,inst])
    df_train.to_csv('TX_1000m_dataV3_train.csv', index=False)
    df_test.to_csv('TX_1000m_dataV3_test.csv', index=False)
    ####################################################################################################
    data = pd.read_csv('TX_400m_data_p.csv')
    df_train, df_test = train_test_split(data, test_size=0.30, random_state=42)
    inst = df_train.loc[df_train['PageName'].isin(fourm)]  # 1000m
    df_train = df_train.loc[~df_train['PageName'].isin(fourm)]  # 1000m
    df_test = pd.concat([df_test, inst])
    df_train.to_csv('TX_400m_dataV3_train.csv', index=False)
    df_test.to_csv('TX_400m_dataV3_test.csv', index=False)
    print("Completel donnnnnnnnnnnnnnnn")

if k == -1:
    input_dir = "/mnt/d/TxSON/Static"
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
    print(seven)
    ten = natsorted(ten)
    static_400m = pd.DataFrame(index=range(8064))
    for f in four:
        temp = pd.read_csv(os.path.join(input_dir,f))
        static_400m[f.split("_", 1)[0]] = temp['MEAN']
        static_400m.to_csv("TX_Static_400m.csv",index=False)
    static_700m = pd.DataFrame(index=range(2640))
    for s in seven:
        temp = pd.read_csv(os.path.join(input_dir,s))
        static_700m[s.split("_", 1)[0]] = temp['MEAN']
        static_700m.to_csv("TX_Static_700m.csv",index=False)
    static_1000m = pd.DataFrame(index=range(1326))
    for t in ten:
        temp = pd.read_csv(os.path.join(input_dir,t))
        static_1000m[t.split("_", 1)[0]] = temp['MEAN']
        static_1000m.to_csv("TX_Static_1000m.csv",index=False)

if k == 1:
    temp_a = pd.read_csv("gillespie_mean_temperature_anomaly.csv")
    temp_m = pd.read_csv("gillespie_mean_temperature_monthly.csv")
    precp_m = pd.read_csv("gillespie_precipitation_monthly.csv")
    precp_a = pd.read_csv("gillespie_precipitation_anomaly.csv")
    temp_a['period'] = temp_a['period'].astype("string")
    temp_m['period'] = temp_m['period'].astype("string")
    static_whole = pd.read_csv("TX_Static_400m.csv")
    static_hundred = pd.read_csv("TX_Static_700m.csv")
    static_thirty = pd.read_csv("TX_Static_1000m.csv")
    lst_dir = '/mnt/d/LST/TXson'
    input_dir = "/mnt/d/TxSON"
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
    ndvi_four = []
    ndvi_seven = []
    ndvi_ten = []
    smerge_four = []
    smerge_seven = []
    smerge_ten = []
    for w in four:
        if w.startswith("Alb"):
            alb_four.append(os.path.join(input_dir, w))
        if w.startswith("LAI"):
            lai_four.append(os.path.join(input_dir, w))
        if w.startswith("NDVI"):
            ndvi_four.append(os.path.join(input_dir, w))
        if w.startswith("SMERGE"):
            smerge_four.append(os.path.join(input_dir, w))
    for t in seven:
        if t.startswith("Alb"):
            alb_seven.append(os.path.join(input_dir, t))
        if t.startswith("LAI"):
            lai_seven.append(os.path.join(input_dir, t))
        if t.startswith("NDVI"):
            ndvi_seven.append(os.path.join(input_dir, t))
        if t.startswith("SMERGE"):
            smerge_seven.append(os.path.join(input_dir, t))
    for h in ten:
        if h.startswith('A'):
            alb_ten.append(os.path.join(input_dir, h))
        if h.startswith('L'):
            lai_ten.append(os.path.join(input_dir, h))
        if h.startswith('N'):
            ndvi_ten.append(os.path.join(input_dir, h))
        if h.startswith("S"):
            smerge_ten.append(os.path.join(input_dir, t))
    f_data = pd.DataFrame(columns=['SMERGE', 'Date', 'PageName', 'LAI', 'Albedo', 'NDVI','Temp_M','Temp_A', 'Clay', 'Sand', 'Silt ', 'Slope', 'Elevation','Ascept'])
    doy = ["03/01/2016","03/08/2016","03/15/2016","03/22/2016","03/29/2016","04/5/2016","04/12/2016",
            "04/19/2016","04/26/2016","05/03/2016","5/10/2016","05/17/2016","05/24/2016","05/31/2016",
            "06/07/2016","06/14/2016","06/21/2016","06/28/2016","07/05/2016","07/12/2016","03/01/2017",
            "03/15/2017","03/29/2017","04/12/2017","04/26/2017","05/10/2017","05/24/2017","06/07/2017",
            "06/21/2017","07/05/2017","07/19/2017","08/02/2017","08/16/2017","08/30/2017","9/13/2017",
            "09/27/2017","10/11/2017","10/25/2017","11/08/2017","11/22/2017","03/01/2018","3/15/2018",
            "03/29/2018","04/12/2018","04/26/2018","05/10/2018","5/24/2018","06/07/2018","6/21/2018",
            "07/5/2018","07/19/2018","08/2/2018","08/16/2018","08/30/2018","09/13/2018","9/27/2018",
            "10/11/2018","10/25/2018","11/8/2018","11/22/2018","03/01/2019","03/15/2019",
            "03/29/2019","04/12/2019","04/26/2019","05/10/2019"]
    r = 8064
    current = pd.DataFrame( index=range(r))
    w = 0
    print(temp_a)
    for k in range(1,67):
        #print(lai_whole)
        static = pd.read_csv("TX_Static_400m.csv")
        date = pd.to_datetime(doy[k - 1], format='%m/%d/%Y')
        #sm = pd.DataFrame(smerge.iloc[w]['SMERGE'], columns=['SMERGE'], index=range(r))
        current['SMERGE'] = pd.read_csv(smerge_four[w], usecols=["MEAN_SMERGE_"+str(k)])
        current["Date"] = pd.DataFrame(doy[k-1], columns=['Date'], index=range(r))
        print(str(date.month).rjust(2,"0"))
        t_a = temp_a[temp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2,"0"))]
        t_m = temp_m[temp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2,"0"))]
        current["Temp_A"] = pd.DataFrame(float(t_a['mean_temperature_anomaly_degf']), columns=['Date'], index=range(r))
        current["Temp_M"] = pd.DataFrame(float(t_m['mean_temperature_monthly_degf']), columns=['Date'], index=range(r))
        p_a = precp_a[precp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2,"0"))]
        p_m = precp_m[precp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2, "0"))]
        current["Precip_A"] = pd.DataFrame(float(p_a['precipitation_anomaly_percent_of_average']), columns=['Date'], index=range(r))
        current["Precip_M"] = pd.DataFrame(float(p_m['precipitation_monthly_inches']), columns=['Date'], index=range(r))
        current["PageName"] = pd.read_csv(alb_four[w], usecols=["PageName"])
        current["LAI"] = pd.read_csv(lai_four[w], usecols=["MEAN_LAI_"+str(k)])
        current["Albedo"] = pd.read_csv(alb_four[w], usecols=["MEAN_Albedo_"+str(k)])
        current["NDVI"] = pd.read_csv(ndvi_four[w], usecols=['MEAN_CONU'+ str(k-1)])
        current[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept']] = static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept']]
        f_data = pd.concat([f_data, current])
        if k == 66:
            f_data.to_csv('TX_400m_dataV4.csv', index=False)
    r = 1326 #1000m
    current = pd.DataFrame(index=range(r))
    f_data = pd.DataFrame(columns=['SMERGE', 'Date', 'PageName', 'LAI', 'Albedo', 'NDVI','Temp_M','Temp_A', 'Clay', 'Sand', 'Silt ', 'Slope', 'Elevation', 'Ascept'])
    for k in range(1,67):
        #print(w)
        #print(len(alb_hundred_m))
        static = pd.read_csv("TX_Static_1000m.csv")
        date = pd.to_datetime(doy[k-1], format='%m/%d/%Y')
        current['SMERGE'] = pd.read_csv(smerge_ten[w], usecols=["MEAN_SMERGE_" + str(k)])
        current["Date"] = pd.DataFrame(doy[k-1], columns=['Date'], index=range(r))
        t_a = temp_a[temp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2, "0"))]
        t_m = temp_m[temp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2, "0"))]
        current["Temp_A"] = pd.DataFrame(float(t_a['mean_temperature_anomaly_degf']), columns=['Date'], index=range(r))
        current["Temp_M"] = pd.DataFrame(float(t_m['mean_temperature_monthly_degf']), columns=['Date'], index=range(r))
        p_a = precp_a[precp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2, "0"))]
        p_m = precp_m[precp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2, "0"))]
        current["Precip_A"] = pd.DataFrame(float(p_a['precipitation_anomaly_percent_of_average']), columns=['Date'],index=range(r))
        current["Precip_M"] = pd.DataFrame(float(p_m['precipitation_monthly_inches']), columns=['Date'], index=range(r))
        current["PageName"] = pd.read_csv(alb_ten[w], usecols=["PageName"])
        current["LAI"] = pd.read_csv(lai_ten[w], usecols=["MEAN_LAI_" + str(k)])
        current["Albedo"] = pd.read_csv(alb_ten[w], usecols=["MEAN_Albedo_" + str(k)])
        current["NDVI"] = pd.read_csv(ndvi_ten[w], usecols=['MEAN_CONU' + str(k - 1)])
        current[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept']] = static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept']]
        f_data = pd.concat([f_data, current])
        if k == 66:
            f_data.to_csv('TX_1000m_dataV4.csv', index=False)
    r = 2640 #700m
    current = pd.DataFrame(index=range(r))
    f_data = pd.DataFrame(columns=['SMERGE', 'Date', 'PageName', 'LAI', 'Albedo', 'NDVI','Temp_M','Temp_A', 'Clay', 'Sand', 'Silt ', 'Slope', 'Elevation', 'Ascept'])
    for k in range(1,67):
        #print(w)
        #print(len(alb_thirty_m))
        static = pd.read_csv("TX_Static_700m.csv")
        date = pd.to_datetime(doy[k - 1], format='%m/%d/%Y')
        current['SMERGE'] = pd.read_csv(smerge_seven[w], usecols=["MEAN_SMERGE_" + str(k)])
        current["Date"] = pd.DataFrame(doy[k-1], columns=['Date'], index=range(r))
        t_a = temp_a[temp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2, "0"))]
        t_m = temp_m[temp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2, "0"))]
        current["Temp_A"] = pd.DataFrame(float(t_a['mean_temperature_anomaly_degf']), columns=['Date'], index=range(r))
        current["Temp_M"] = pd.DataFrame(float(t_m['mean_temperature_monthly_degf']), columns=['Date'], index=range(r))
        p_a = precp_a[precp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2, "0"))]
        p_m = precp_m[precp_a['period'] == (str(date.year) + '-' + str(date.month).rjust(2, "0"))]
        current["Precip_A"] = pd.DataFrame(float(p_a['precipitation_anomaly_percent_of_average']), columns=['Date'], index=range(r))
        current["Precip_M"] = pd.DataFrame(float(p_m['precipitation_monthly_inches']), columns=['Date'], index=range(r))
        current["PageName"] = pd.read_csv(alb_seven[w], usecols=["PageName"])
        current["LAI"] = pd.read_csv(lai_seven[w], usecols=["MEAN_LAI_" + str(k)])
        current["Albedo"] = pd.read_csv(alb_seven[w], usecols=["MEAN_Albedo_" + str(k)])
        current["NDVI"] = pd.read_csv(ndvi_seven[w], usecols=['MEAN_CONU' + str(k - 1)])
        current[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept']] = static[['Clay' ,'Sand' ,'Silt ','Slope' ,'Elevation' ,'Ascept']]
        f_data = pd.concat([f_data,current])
        if k == 66:
            f_data.to_csv('TX_700m_dataV4.csv', index=False)
