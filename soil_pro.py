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
from xlcalculator import ModelCompiler
from xlcalculator import Model
from xlcalculator import Evaluator

# filename_C = r'/mnt/d/SoilTest/Soil_US_Component.csv'
# filename_H = r'/mnt/d/SoilTest/Soil_US_Horizon.csv'
# pd.set_option('display.max_columns', None)
# componet = pd.read_csv(filename_C,low_memory=False)
# horizon = pd.read_csv(filename_H,low_memory=False)
# print(horizon)
# print(componet)
# componet_t = componet[['OID_','comppct_l','comppct_r','mukey','cokey']]
# horizon_t = horizon[['OID_','hzname','hzdepb_r', 'hzthk_r','sandtotal_r','silttotal_r','claytotal_r','cokey','chkey']]
# componet_t.to_csv('/mnt/d/SoilTest/Soil_US_Component_Trim.csv')
# horizon_t.to_csv('/mnt/d/SoilTest/Soil_US_Horizon_Trim.csv')

filename_C = r'/mnt/d/SoilTest/Soil_US_Component_Trim.csv'
filename_H = r'/mnt/d/SoilTest/Soil_US_Horizon_Trim.csv'
pd.set_option('display.max_columns', None)
componet = pd.read_csv(filename_C, low_memory=False,float_precision='high').replace('', np.NAN)
horizon = pd.read_csv(filename_H, low_memory=False,float_precision='high').replace('', np.NAN)
# for col in componet.columns:
#     try:
#         componet[col] = componet[col].astype('float64')
#     except ValueError:
#         pass
# for col in horizon.columns:
#     try:
#         horizon[col] = horizon[col].astype('float64')
#     except ValueError:
#         pass

horizon['check_1'] = horizon['sandtotal_r'].apply(lambda x: -1 if x == "<Null>" else 0)
horizon['check_2'] = horizon.apply(lambda row: 0 if row['hzdepb_r'] - row['hzthk_r'] > 40 else 1, axis=1)
horizon['check_3'] = horizon.apply(lambda row: np.NAN if row['check_2'] < 1 else (row['hzthk_r'] - (row['hzdepb_r'] - 40)) if row['hzdepb_r'] > 40 else np.NAN, axis=1)
horizon['check_4'] = horizon['check_3'].apply(lambda x: np.NAN if x < 0 else x).fillna(0)
horizon['check_5'] = horizon.apply(lambda row: np.NAN if row['hzdepb_r'] < 40 else row['hzthk_r'], axis=1).fillna(0)
horizon['TotalSand_process_1'] = horizon.apply(lambda row: (row['sandtotal_r'] * (row['check_4'] + row['check_5']) / 40) if row['check_1'] + row['check_2'] == 1 else np.NAN, axis=1)
horizon['TotalSilt_process_1'] = horizon.apply(lambda row: (row['silttotal_r'] * (row['check_4'] + row['check_5']) / 40) if row['check_1'] + row['check_2'] == 1 else np.NAN, axis=1)
horizon['TotalClay_process_1'] = horizon.apply(lambda row: (row['claytotal_r'] * (row['check_4'] + row['check_5']) / 40) if row['check_1'] + row['check_2'] == 1 else np.NAN, axis=1)

processing = pd.DataFrame()
processing['cokey'] = componet['cokey'].unique()
processing.set_index('cokey', inplace=True)
processing['TotalSand_process_2'] = horizon.groupby(horizon['cokey'])['TotalSand_process_1'].sum()
processing['TotalSilt_process_2'] = horizon.groupby(horizon['cokey'])['TotalSilt_process_1'].sum()
processing['TotalClay_process_2'] = horizon.groupby(horizon['cokey'])['TotalClay_process_1'].sum()#['comppct_r'].set_index('cokey')
processing['SSC_Sum'] = processing['TotalSand_process_2'] + processing['TotalSilt_process_2'] + processing['TotalClay_process_2']
temp = componet[['comppct_r','cokey']].set_index('cokey')
processing['comppct_r'] = temp
processing['Adjust_Comp'] = processing.apply(lambda row: 0 if row['TotalSand_process_2'] == 0 else row['comppct_r'], axis=1)
temp = componet[['mukey','cokey']].set_index('cokey')
processing['mukey'] = temp
processing['cokey_2'] = processing.index
processing['TotalSand_process_3'] = processing.apply(lambda row: 0 if row['TotalSand_process_2'] == 0 else row['TotalSand_process_2'] if row['SSC_Sum'] == 100 else row['TotalSand_process_2'] * (100 / row['SSC_Sum']), axis=1)
processing['TotalSilt_process_3'] = processing.apply(lambda row: 0 if row['TotalSilt_process_2'] == 0 else row['TotalSilt_process_2'] if row['SSC_Sum'] == 100 else row['TotalSilt_process_2'] * (100 / row['SSC_Sum']), axis=1)
processing['TotalClay_process_3'] = processing.apply(lambda row: 0 if row['TotalClay_process_2'] == 0 else row['TotalClay_process_2'] if row['SSC_Sum'] == 100 else row['TotalClay_process_2'] * (100 / row['SSC_Sum']), axis=1)
processing['SSC_Sum_2'] = processing['TotalSand_process_3'] + processing['TotalSilt_process_3'] + processing['TotalClay_process_3']

processing['TotalSand_process_4'] = processing.apply(lambda row: row['TotalSand_process_3'] * (row['comppct_r'] / 100), axis=1)
processing['TotalSilt_process_4'] = processing.apply(lambda row: row['TotalSilt_process_3'] * (row['comppct_r'] / 100), axis=1)
processing['TotalClay_process_4'] = processing.apply(lambda row: row['TotalClay_process_3'] * (row['comppct_r'] / 100), axis=1)

final_pro = pd.DataFrame()
final_pro['mukey'] = componet['mukey'].unique()
final_pro.set_index('mukey', inplace=True)
final_pro['mukey_2'] = final_pro.index
final_pro['Total'] = processing.groupby(processing['mukey'])['Adjust_Comp'].sum()
final_pro['TotalSand_process_5'] = processing.groupby(processing['mukey'])['TotalSand_process_4'].sum()
final_pro['TotalSilt_process_5'] = processing.groupby(processing['mukey'])['TotalSilt_process_4'].sum()
final_pro['TotalClay_process_5'] = processing.groupby(processing['mukey'])['TotalClay_process_4'].sum()
final_pro['SSC_Sum_3'] = final_pro['TotalSand_process_5'] + final_pro['TotalSilt_process_5'] + final_pro['TotalClay_process_5']

horizon.to_csv('Horizon_pre_pro.csv')
processing.to_csv('Horizon_processing.csv')
final_pro.to_csv('Horizon_finalpro.csv')

# # To reload the file later...
#
# print("Loading from compiled file...")
# excel2 = ExcelCompiler.from_file('ARM_3_4_horizon.xlsx.yaml')
#
# # test evaluation
# print("D1 is %s" % excel2.evaluate('Sheet1!D1'))
#
# print("Setting A1 to 1")
# excel2.set_value('HorizonE3_4_ExportTable!D1', 1)
#
# print("D1 is now %s (the same should happen in Excel)" % excel2.evaluate(
#     'Sheet1!D1'))