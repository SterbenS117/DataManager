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

opopopop = 9
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
    res = 'GBR'
    data_csv = ['_V6_TX_1000m_.csv', '_V6_TX_700m_.csv']
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
        #     print(home + res + '_v6_TXson1_1400mInst.csv')
        #     out.to_csv(home + res +'_v6_TXson1_1400mInst.csv', index=False)
        if '1000m' in d:
            try:
                data = pd.read_csv(home + res + d).rename({'Lai' : 'LAI'}, axis='columns')
            except:
                data = pd.read_csv(home + res + d)
            data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
            p = len(tenm)
            out = pd.DataFrame(columns=['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'LAI', 'SMERGE','NDVI', 'Albedo', 'Temp', 'Date', 'ML_', 'PageName', 'Station'])
            for q in range(0, p):
                #inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
                inst = data[data['PageName'] == tenm[q]]
                inst['Station'] = ten_n[q]
                inst.reset_index(inplace = True)

                out = pd.concat([out, inst])
            out.sort_values(by=['Station', 'Date'], inplace=True)
            out.drop(columns=['index'], inplace=True)
            print(home + res + '_v6_TXson1_1000mInst.csv')
            out.to_csv(home + res +'_v6_TXson1_1000mInst.csv', index=False)
        if '700m' in d:
            try:
                data = pd.read_csv(home + res + d).rename({'Lai': 'LAI'}, axis='columns')
            except:
                data = pd.read_csv(home + d)
            data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
            p = len(sevenm)
            out = pd.DataFrame(
                columns=['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'LAI', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'Date', 'ML_', 'PageName', 'Station'])
            for q in range(0, p):
                # inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
                inst = data[data['PageName'] == sevenm[q]]
                inst['Station'] = seven_n[q]
                inst.reset_index(inplace=True)

                out = pd.concat([out, inst])
            out.sort_values(by=['Station', 'Date'], inplace=True)
            out.drop(columns=['index'], inplace=True)
            print(home + res + '_v6_TXson1_700mInst.csv')
            out.to_csv(home + res + '_v6_TXson1_700mInst.csv', index=False)
        # if '_400m' in d:
        #     try:
        #         data = pd.read_csv(home + res + d).rename({'Lai': 'LAI'}, axis='columns')
        #     except:
        #         data = pd.read_csv(home + d)
        #     data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
        #     p = len(fourm)
        #     out = pd.DataFrame(
        #         columns=['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'LAI', 'SMERGE', 'NDVI', 'Albedo',
        #                  'Temp', 'Date', 'ML_', 'PageName', 'Station'])
        #     for q in range(0, p):
        #         # inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
        #         inst = data[data['PageName'] == fourm[q]]
        #         inst['Station'] = four_n[q]
        #         inst.reset_index(inplace=True)
        #
        #         out = pd.concat([out, inst])
        #     out.sort_values(by=['Station', 'Date'], inplace=True)
        #     out.drop(columns=['index'], inplace=True)
        #     print(home + res + '_v6_TXson1_400mInst.csv')
        #     out.to_csv(home + res + '_v6_TXson1_400mInst.csv', index=False)