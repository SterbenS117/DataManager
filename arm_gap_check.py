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

if k == 16:
    type = "ARM"
    era = [1,2,3,4]
    era_s = ["Era3_1","Era3_2","Era3_3","Era3_4"]
    for e in era:
        four = []
        seven = []
        ten = []
        fourteen = []
        input_dir = '/mnt/d/ARM/Fontera/ARM3_V2'
        for f in os.listdir(input_dir):
            if era_s[e-1] in f and f.endswith('.csv'):
                if ("_400m_" in f) and f.startswith(type):
                    four.append(f)
                if ("_700m_" in f) and f.startswith(type):
                    seven.append(f)
                if ("_1000m_" in f) and f.startswith(type):
                    ten.append(f)
                if ("_1400m_" in f) and f.startswith(type):
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
                print()
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

                except:
                    inst.columns = ['Index', 'SMERGE', 'Temp', 'Lai', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope',
                                    'Elevation',
                                    'Ascept', 'PageName', 'Date2', 'Station_E', 'Station_W', 'Station_Name']
                    inst = inst[
                        ['Index', 'Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI',
                         'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

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
                print(inst.columns)
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                print(inst.columns)
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

                except:
                    inst.columns = ['Index', 'SMERGE', 'Temp', 'Lai', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope', 'Elevation',
                                    'Ascept', 'PageName', 'Date2', 'Station_E', 'Station_W', 'Station_Name']
                    inst = inst[
                        ['Index','Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]
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
                print(data_n)
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

                except:
                    inst.columns = ['Index', 'SMERGE', 'Temp', 'Lai', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope',
                                    'Elevation',
                                    'Ascept', 'PageName', 'Date2', 'Station_E', 'Station_W', 'Station_Name']
                    inst = inst[
                        ['Index', 'Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI',
                         'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]
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
                print(data_n)
                inst.loc[inst['Station_Name'] == names[q], ['Station_E']] = inst_data['Value']
                inst_data = pd.read_csv(inst_dir + names[q] + '_W.csv').dropna(subset=['Name']).rename(
                    columns={"Name": "Date"}).set_index("Date")
                inst.loc[inst['Station_Name'] == names[q], ['Station_W']] = inst_data['Value']
                try:
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]

                except:
                    inst.columns = ['Index', 'SMERGE', 'Temp', 'Lai', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope',
                                    'Elevation',
                                    'Ascept', 'PageName', 'Date2', 'Station_E', 'Station_W', 'Station_Name']
                    inst = inst[
                        ['Index', 'Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI',
                         'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W']]
                # inst.sort_index(inplace=True)
                inst['Date2'] = pd.to_datetime(inst['Date2'], format="%m/%d/%Y")
            inst.sort_values(by=['Station_Name', 'Date2'], inplace=True)
            inst2 = inst.set_index(['Station_Name', 'Date2'])
            temp = inst2.reindex(four_index.index)
            temp['Station_E'] = pd.to_numeric(temp['Station_E'], errors='coerce')
            temp['Station_W'] = pd.to_numeric(temp['Station_W'], errors='coerce')
            print("##############################################################################################################################################")
            # Create an Excel writer object
            writer = pd.ExcelWriter(input_dir + '/' + data_out.replace('.csv','.xlsx'), engine='xlsxwriter')
            # Write each DataFrame to a separate sheet
            inst.to_excel(writer, sheet_name='Sheet1', index=False)
            temp.to_excel(writer, sheet_name='Sheet2', index=True)
            inst.to_csv(input_dir + '/' + data_out, index=False)
            temp.to_csv(input_dir + '/' + data_out2, index=True)
            writer.save()


if k == -6:
    type = "ARM"
    era = [1,2]
    era_s = ["Era1_1", "Era1_2"]
    for e in era:
        four = []
        seven = []
        ten = []
        fourteen = []
        input_dir = '/mnt/d/ARM/Fontera/ARM1_V3'
        for f in os.listdir(input_dir):
            if era_s[e - 1] in f and f.endswith('.csv'):
                if ("_400m_" in f) and f.startswith(type):
                    four.append(f)
                if ("_700m_" in f) and f.startswith(type):
                    seven.append(f)
                if ("_1000m_" in f) and f.startswith(type):
                    ten.append(f)
                if ("_1400m_" in f) and f.startswith(type):
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
            print(inst)
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
                    inst = inst[
                        ['Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI', 'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                except:
                    inst.columns = ['Index', 'SMERGE', 'Temp', 'Lai', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope', 'Elevation',
                                    'Ascept', 'PageName', 'Date2', 'Station_E', 'Station_W', 'Station_S', 'Station_Name']
                    inst = inst[
                        ['Index', 'Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI',
                         'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

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
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                except:
                    inst.columns = ['Index', 'SMERGE', 'Temp', 'Lai', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope',
                                    'Elevation',
                                    'Ascept', 'PageName', 'Date2', 'Station_E', 'Station_W', 'Station_S',
                                    'Station_Name']
                    inst = inst[
                        ['Index', 'Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI',
                         'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

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
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                except:
                    inst.columns = ['Index', 'SMERGE', 'Temp', 'Lai', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope',
                                    'Elevation',
                                    'Ascept', 'PageName', 'Date2', 'Station_E', 'Station_W', 'Station_S',
                                    'Station_Name']
                    inst = inst[
                        ['Index', 'Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI',
                         'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

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
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

                except:
                    inst.columns = ['Index', 'SMERGE', 'Temp', 'Lai', 'Albedo', 'NDVI', 'Clay', 'Sand', 'Silt', 'Slope',
                                    'Elevation',
                                    'Ascept', 'PageName', 'Date2', 'Station_E', 'Station_W', 'Station_S',
                                    'Station_Name']
                    inst = inst[
                        ['Index', 'Clay', 'Sand', 'Silt', 'Elevation', 'Ascept', 'Slope', 'Lai', 'SMERGE', 'NDVI',
                         'Albedo',
                         'Temp', 'PageName', 'Date2', 'Station_Name', 'Station_E', 'Station_W', 'Station_S']]

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