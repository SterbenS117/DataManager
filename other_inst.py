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
k = -6
if k == -6:
    network = "USCRN"
    type = "XGB"
    era = [2,1]
    era_s = ["ERA11", "ERA12"]
    for e in era:
        four = []
        seven = []
        ten = []
        fourteen = []
        input_dir = '/mnt/d/ARM/Fontera/ARM1/Era1_' + str(e) + '/ML'
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
        if network == 'SCAN':
            inst_dir = '/mnt/d/SCAN/Era1/'  # SCAN
            if e == 1:
                fourm = ['AF352']
                sevenm = ['R201']
                tenm = ['M141']
                fourteenm = ['I101']
                names = ['Abrams']  # SCAN_1
            if e == 2:
                fourm = []
                sevenm = []
                tenm = []
                fourteenm = []
                names = []  # SCAN_2
        if network == 'USCRN':
            inst_dir = '/mnt/d/USCRN/Era1/'  # USCRN
            if e == 1:
                fourm = []
                sevenm = []
                tenm = []
                fourteenm = []
                names = []  # USCRN_1
            if e == 2:
                fourm = ['CK335', 'CP340']
                sevenm = ['AY192', 'BB194']
                tenm = ['AJ134', 'AL136']
                fourteenm = ['Z96', 'AA97']
                names = ['Stillwater-5-WNW', 'Stillwater-2-W']  # USCRN_2
        if names == []:
            continue
        for name in four:
            data_n = name
            data_out = name.replace('.csv', 'inst.csv')
            data = pd.read_csv(input_dir + '/' + data_n)
            inst = data.loc[data['PageName'].isin(fourm)]  # 400m
            p = len(fourm)
            inst = data.loc[data['PageName'].isin(fourm)]  # 1000m
            inst['Date2'] = inst['Date']
            inst['Station_Value'] = np.nan
            inst['Station_Name'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == fourm[q], ['Station_Name']] = names[q]
                print(q)

                inst_data = pd.read_csv(inst_dir + names[q]+'.csv').dropna(subset=['Date']).rename(columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_Value']] = inst_data['Value']
                print(inst)
                try:
                    inst.rename(columns={"LAI": "Lai"}, inplace=True)
                    inst.rename(columns={"ML": "ML_"}, inplace=True)
                except:
                    print(q)
                inst = inst[
                    ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                     'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_Value'] = pd.to_numeric(inst['Station_Value'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
                # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv',  network+'.xlsx'), engine='xlsxwriter')
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
            inst['Station_Value'] = np.nan
            inst['Station_Name'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q]+'.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_Value']] = inst_data['Value']
                try:
                    inst.rename(columns={"LAI": "Lai"}, inplace=True)
                    inst.rename(columns={"ML": "ML_"}, inplace=True)
                except:
                    print(q)
                inst = inst[
                    ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                     'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_Value'] = pd.to_numeric(inst['Station_Value'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv',  network+'.xlsx'), engine='xlsxwriter')
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
            inst['Station_Value'] = np.nan
            inst['Station_Name'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):

                inst.loc[inst['PageName'] == fourteenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q]+'.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_Value']] = inst_data['Value']
                try:
                    inst.rename(columns={"LAI": "Lai"},inplace=True)
                    inst.rename(columns={"ML": "ML_"},inplace=True)
                except:
                    print(q)
                inst = inst[
                    ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                     'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_Value'] = pd.to_numeric(inst['Station_Value'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', network+ '_.xlsx'), engine='xlsxwriter')
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
            inst['Station_Value'] = np.nan
            inst['Station_Name'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == sevenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q] + '.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_Value']] = inst_data['Value']
                try:
                    inst.rename(columns={"LAI": "Lai"}, inplace=True)
                    inst.rename(columns={"ML": "ML_"}, inplace=True)
                except:
                    print(q)
                inst = inst[
                    ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                     'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_Value'] = pd.to_numeric(inst['Station_Value'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', network + '.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()

if k == 6:
    network = "SCAN"
    type = "GBR"
    era = [4]
    era_s = ["ERA31","ERA32","ERA33","ERA34"]
    for e in era:
        four = []
        seven = []
        ten = []
        fourteen = []
        input_dir = '/mnt/d/ARM/Fontera/ARM3_V2/Era3_' + str(e) + '/ML'
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
        if network == 'SCAN':
            inst_dir = '/mnt/d/SCAN/Era3/'  # SCAN
            if e == 4:
                fourm = ['FM343']
                sevenm = ['CS196']
                tenm = ['BQ137']
                fourteenm = ['AW98']
                names = ['FortReno#1_Analog']  # SCAN_4
        if network == 'USCRN':
            inst_dir = '/mnt/d/USCRN/Era3/'  # USCRN
            if e == 4:
                fourm = ['G595','K600']
                sevenm = ['D340','G343']
                tenm = ['D238','F240']
                fourteenm = ['B170','D172']
                names = ['Stillwater-5-WNW', 'Stillwater-2-W']  # USCRN_4
        if names == []:
            continue
        for name in four:
            data_n = name
            data_out = name.replace('.csv', 'inst.csv')
            data = pd.read_csv(input_dir + '/' + data_n)
            inst = data.loc[data['PageName'].isin(fourm)]  # 400m
            p = len(fourm)
            inst = data.loc[data['PageName'].isin(fourm)]  # 1000m
            inst['Date2'] = inst['Date']
            inst['Station_Value'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == fourm[q], ['Station_Name']] = names[q]
                    # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                print(names[q])
                inst_data = pd.read_csv(inst_dir + names[q]+'.csv').dropna(subset=['Date']).rename(columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_Value']] = inst_data['Value']
                try:
                    inst = inst[['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                             'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                        'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_Name', 'Station_Value']
                    print(inst.columns)
                    inst = inst[
                            ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                             'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_Value'] = pd.to_numeric(inst['Station_Value'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
                # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv',  network+'.xlsx'), engine='xlsxwriter')
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
            inst['Station_Value'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == tenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q]+'.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_Value']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_Name', 'Station_Value']
                    print(inst.columns)
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_Value'] = pd.to_numeric(inst['Station_Value'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv',  network+'.xlsx'), engine='xlsxwriter')
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
            inst['Station_Value'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):

                inst.loc[inst['PageName'] == fourteenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q]+'.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_Value']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_Name', 'Station_Value']
                    print(inst.columns)
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_Value'] = pd.to_numeric(inst['Station_Value'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv', network+ '_.xlsx'), engine='xlsxwriter')
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
            inst['Station_Value'] = np.nan
            inst.set_index(['Date'], inplace=True)
            for q in range(0, p):
                inst.loc[inst['PageName'] == sevenm[q], ['Station_Name']] = names[q]
                # inst[(inst['PageName'] == tenm[q])]['Station_Name'] = names[q]
                inst_data = pd.read_csv(inst_dir + names[q]+'.csv').dropna(subset=['Date']).rename(
                    columns={"Date": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_Value']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                except:
                    inst.columns = ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'NDVI', 'Albedo',
                                    'Temp', 'ML_', 'SMERGE', 'PageName', 'Date2', 'Station_Name', 'Station_Value']
                    print(inst.columns)
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'ML_', 'PageName', 'Date2', 'Station_Name', 'Station_Value']]

                    # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst['Station_Value'] = pd.to_numeric(inst['Station_Value'], errors='coerce')
            inst.to_csv(input_dir + '/' + data_out, index=False)
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv',  network+'.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()