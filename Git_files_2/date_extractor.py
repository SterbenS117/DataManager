import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime
np.set_printoptions(suppress=True,linewidth=500,threshold=500)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 25)

data = pd.read_csv(r"E:\BigRun\T2\XGB_BigRunWS_V5_T2_500(1).csv", engine='pyarrow')

print(data[data['Date']==datetime.date(2014, 7, 30)])
sample = data[data['Date']==datetime.date(2014, 7, 30)]

sample.to_csv(r"E:\BigRun\T2\XGB_BigRunWS_V5_T2_500_sample-20140730.csv", index=False)