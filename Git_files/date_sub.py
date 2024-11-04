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

data = pd.read_csv('/mnt/d/BigRun_NDVI/ALL/GBR_BigRunALL_1000.csv')
data_sub = data[data['Date'] == '06/15/2015']

data_sub.to_csv('/mnt/d/BigRun_NDVI/ALL/GBR_BigRunALL_1000_sub.csv')