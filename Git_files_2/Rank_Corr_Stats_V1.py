import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(suppress=True,linewidth=500,threshold=500)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 25)
def calculate_ubRMS(column1, column2):
    """
    Calculate the unbiased Root Mean Square (ubRMS) of two columns.

    Parameters:
    column1 (array-like): First data column. Test Column
    column2 (array-like): Second data column. Verifier Column

    Returns:
    float: Unbiased RMS of the two columns.
    """
    # Combine the two columns
    combined_data = np.vstack([column1, column2])

    # Calculate the ubRMS
    n = np.shape(combined_data)[1]
    if n <= 1:
        raise ValueError("Insufficient data points for unbiased RMS calculation.")
    dif_mean = np.mean(column2) - np.mean(column1)
    ubRMS = (np.sqrt(np.sum((column1 + dif_mean - column2) ** 2) / n)) / 1000

    return ubRMS

# Function to interpret correlation results
def interpret_correlation(correlation, p_value, name):
    # Interpret the strength of the correlation
    abs_corr = abs(correlation)
    if abs_corr > 0.8:
        strength = 'very strong'
    elif abs_corr > 0.6:
        strength = 'strong'
    elif abs_corr > 0.4:
        strength = 'moderate'
    elif abs_corr > 0.2:
        strength = 'weak'
    else:
        strength = 'very weak'

    # Interpret the direction of the correlation
    if correlation > 0:
        direction = 'positive'
    else:
        direction = 'negative'

    # Assess the significance
    if p_value < 0.05:
        significance = 'statistically significant'
    else:
        significance = 'not statistically significant'

    print(f"{name}'s rank correlation coefficient: {correlation} ({strength}, {direction})")
    print(f"This correlation is {significance} (p-value: {p_value})\n")
def create_correction_matrix(df):
    """
    Create a correction matrix for all numerical columns of a pandas DataFrame.

    Parameters:
    df (pandas.DataFrame): Input DataFrame with numerical columns.

    Returns:
    pandas.DataFrame: Correction matrix of the numerical columns.
    """
    # Select only numerical columns
    numerical_df = df.select_dtypes(include=[np.number])

    # Calculate the correlation matrix
    corr_matrix = numerical_df.corr()

    return corr_matrix




hist_monthly_average = pd.read_csv(r"E:\BigRun\anamoly_calculated_dataV4_500.csv", engine='pyarrow')

# data = pd.read_csv(r"E:\share\BIgRun\Watershed_Cal\BigRunWS_V3_2_500.csv", engine='pyarrow')
#data = pd.read_csv(r"E:\share\BIgRun\Watershed_Cal\T\T2\BigRunWS_V5_T_500_test_part_6.csv", engine='pyarrow')
data = pd.read_csv(r"E:\BigRun\T2\source\BigRunWS_V5_T_500_test_part_1.csv", engine='pyarrow')

#data = data[data['AHRR'] > 0]

data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year
data = data[data['Month'] > 5]
data = data[data['Month'] < 9]
data = data[data['Year'] < 2018]

data['Soil'] = data['Sand'] + data['Silt'] + data['Clay']
data = data[data['Soil'] >= 99.99]

data_t = data.merge(hist_monthly_average, on= ['PageName', 'Month'])
data_t['SMERGE_A'] = data_t['Smerge'] - data_t['SMERGE_M']
#data_t['SMERGE_A'] = data_t['Smerge'] - data_t['SMERGE_M']
data_t['AHRR_A'] = data_t['AHRR'] - data_t['AHRR_M']




import numpy as np
from scipy.stats import spearmanr, kendalltau
d = data_t.groupby(['Month', 'Year']).agg(avg_AHRR_A=('AHRR_A', 'mean'), avg_Smerge_A=('SMERGE_A', 'mean')).reset_index()
#Sample data
x = d['avg_AHRR_A']
y = d['avg_Smerge_A']
# d = data_t[['AHRR_A','SMERGE_A']].dropna()
# x = d['AHRR_A']
# y = d['SMERGE_A']

# Calculate Spearman's rank correlation
spearman_corr, spearman_p_value = spearmanr(x, y)
print(f"Spearman's rank correlation coefficient: {spearman_corr}")
print(f"Spearman's p-value: {spearman_p_value}")

# Calculate Kendall's tau correlation
kendall_corr, kendall_p_value = kendalltau(x, y)
print(f"Kendall's tau correlation coefficient: {kendall_corr}")
print(f"Kendall's p-value: {kendall_p_value}")
print('')
interpret_correlation(spearman_corr, spearman_p_value, 'SMERGE_A')

# corr = create_correction_matrix(data_t)
# print(corr)