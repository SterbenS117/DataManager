import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(suppress=True,linewidth=500,threshold=500)

#mm6_3 = pd.read_csv(r'E:\share\BIgRun\Verifying\anamoly_cal_data_V4_1000.csv', engine='pyarrow')
mm6_3 = pd.read_csv(r"E:\BigRun\2025_Big\All-BR_V6D_anamoly_data.csv", engine='pyarrow')

mm6_3.rename(columns={'Smerge': 'SMERGE'}, inplace=True)

mm6_3['Date'] = pd.to_datetime(mm6_3['Date'], format="%Y-%m-%d")

mm6_3['Month'] = mm6_3['Date'].dt.month
mm6_3['Year'] = mm6_3['Date'].dt.year

mm6_3['Date'] = mm6_3['Date'].astype(pd.StringDtype())

mm6_3['Date2'] = mm6_3['Date']

mm6_3['Date'] = mm6_3['Date'].str.replace(' 00:00:00', '', regex=False)

mm6_3['Date2'] = mm6_3['Date']

mm6_3['PageName2'] = mm6_3['PageName']

mm6_3.reset_index(inplace=True)

mm6_3.set_index(['PageName','Date'], inplace=True)

monthly_average = mm6_3[['SMERGE','AHRR','Year','Month','PageName2']].groupby(['Year', 'Month','PageName2']).mean()

monthly_average.to_csv(r'E:\BigRun\2025_Big\Watershed_Cal\mean_cal_V5.csv')

monthly_average.reset_index(inplace=True)



hist_monthly_average = monthly_average[['SMERGE','AHRR','Month','PageName2']].groupby(['Month','PageName2']).mean()

hist_monthly_average.columns = ['SMERGE_M','AHRR_M']

hist_monthly_average.reset_index(inplace=True)

hist_monthly_average.rename(columns={'PageName2': 'PageName'}, inplace=True)

hist_monthly_average.to_csv(r'E:\BigRun\2025_Big\anamoly_calculated_dataV5_500.csv')