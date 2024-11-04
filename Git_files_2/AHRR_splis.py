import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import dask.dataframe as dd
np.set_printoptions(suppress=True,linewidth=500,threshold=500)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 25)


master_data = pd.read_csv(r"E:\BigRun\BigRunWS_V5_T2_500.csv", engine='pyarrow')

#data = pd.read_csv(r"E:\share\BIgRun\Watershed_Cal\2\RF_BigRunWS4_500.csv", engine='pyarrow')
#data = pd.read_csv(r"E:\share\BIgRun\Watershed_Cal\4\GBR_BigRunWS5_1_500.csv", engine='pyarrow')
data = pd.read_csv(r"E:\BigRun\TS\XGB_BigRunWS_V5_TS1_500.csv", engine='pyarrow')

data.set_index(['PageName','Date'], inplace=True)
master_data.set_index(['PageName','Date'], inplace=True)
data['AHRR'] = master_data['AHRR']
dask_df = dd.from_pandas(data.reset_index(), npartitions=10)
dask_df.to_csv(r"E:\BigRun\TS\XGB_BigRunWS_V5_TS1_500(1).csv", single_file=True, index=False)
#data.to_csv(r"E:\BigRun\T2\RF_BigRunWS_V5_T2_500(1).csv")