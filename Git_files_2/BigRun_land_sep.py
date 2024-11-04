import os
import datetime
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from natsort import natsorted
import re
import string
import warnings
import sys


data = pd.read_csv(r"E:\BigRun\BigRunWS_V5_500_9-20-2024.csv", engine='pyarrow')
out = r'E:\BigRun'
n = 'BigRunWS5_L_500'
index = 'PageName'
data.set_index(['PageName','Date'],inplace=True)
df_train, df_test = train_test_split(data, test_size = 0.20, random_state = 42)
mosssit = pd.read_csv(r"E:\BigRun\Grid_500_Spatial_ExportTable.csv")
mossit_index = mosssit['PageName'].to_list()
print(df_train)
inst = data.loc[data.index.get_level_values(index).isin(mossit_index)]
df_train = df_train.loc[~df_train.index.get_level_values(index).isin(mossit_index)]
df_train.to_csv(os.path.join(out, n+'_train.csv'))
inst.to_csv(os.path.join(out, n+'_test.csv'))