import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv(r"E:\share\BIgRun\Watershed_Cal\BigRunWS_V5_2_500_test.csv", engine='pyarrow')

print(data.dtypes)