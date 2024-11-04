import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(suppress=True,linewidth=500,threshold=500)
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

# Set the input directory
input_data = '/mnt/d/BigRun_NDVI/Summer/XGB_BigRunS_1000.csv' #input("Enter the file path: ")
data = pd.read_csv(input_data)
data['Date2'] = data['Date']
data['PageName2'] = data['PageName']
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
data.set_index(['PageName','Date'], inplace=True)

compl = pd.read_csv('/mnt/d/SmergeCCI_table_1000_1.csv')
compl['Date2'] = compl['Date']
compl['PageName2'] = compl['PageName']
compl['Date'] = pd.to_datetime(compl['Date2'], format="%d/%m/%Y")
compl.set_index(['PageName','Date'], inplace=True)

# Assuming `df` is your dataframe and is already loaded
# Ensure the Date column is in datetime format
compl['Date2'] = pd.to_datetime(compl['Date2'], format="%d/%m/%Y")
compl.rename(columns={'Smerge': 'SMERGE'}, inplace=True)
compl = compl[compl['Date2'].dt.year > 2002]
compl = compl[compl['Date2'].dt.year < 2020]

# Extract year and month for grouping
compl['Month'] = compl['Date2'].dt.month
compl['Year'] = compl['Date2'].dt.year

# Assuming `df` is your dataframe and is already loaded
# Ensure the Date column is in datetime format
data['Date2'] = pd.to_datetime(data['Date2'], format="%Y-%m-%d")
# Extract year and month for grouping
data['Month'] = data['Date2'].dt.month
data['Year'] = data['Date2'].dt.year

# Group by Year and Month, then calculate the average of 'Cope'
monthly_avg_A = data.groupby(['Month','PageName2'])['AHRR'].transform('mean')

# Calculate the difference and add it as a new column
data['AHRR_A'] = data['AHRR'] - monthly_avg_A

# Group by Year and Month, then calculate the average of 'Cope'
monthly_avg_S = compl.groupby(['Month','PageName2'])['SMERGE'].transform('mean')

# Calculate the difference and add it as a new column
data['SMERGE_A'] = data['SMERGE'] - monthly_avg_S


monthly_avg_M = data.groupby(['Month','PageName2'])['ML_'].transform('mean')

# Calculate the difference and add it as a new column
data['ML_A'] = data['ML_'] - monthly_avg_M

import numpy as np
from scipy.stats import spearmanr, kendalltau



d = data.groupby(['Month', 'Year']).agg(avg_AHRR_A=('AHRR_A', 'mean'), avg_ML_A=('ML_A', 'mean')).reset_index()
# Sample data
x = d['avg_AHRR_A']
y = d['avg_ML_A']

# Calculate Spearman's rank correlation
spearman_corr, spearman_p_value = spearmanr(x, y)
print(f"Spearman's rank correlation coefficient: {spearman_corr}")
print(f"Spearman's p-value: {spearman_p_value}")

# Calculate Kendall's tau correlation
kendall_corr, kendall_p_value = kendalltau(x, y)
print(f"Kendall's tau correlation coefficient: {kendall_corr}")
print(f"Kendall's p-value: {kendall_p_value}")
print('')
interpret_correlation(spearman_corr, spearman_p_value, 'ML_A')

d = data.groupby(['Month', 'Year']).agg(avg_AHRR_A=('AHRR_A', 'mean'), avg_Smerge_A=('SMERGE_A', 'mean')).reset_index()
# Sample data
x = d['avg_AHRR_A']
y = d['avg_Smerge_A']

# Calculate Spearman's rank correlation
spearman_corr, spearman_p_value = spearmanr(x, y)
print(f"Spearman's rank correlation coefficient: {spearman_corr}")
print(f"Spearman's p-value: {spearman_p_value}")

# Calculate Kendall's tau correlation
kendall_corr, kendall_p_value = kendalltau(x, y)
print(f"Kendall's tau correlation coefficient: {kendall_corr}")
print(f"Kendall's p-value: {kendall_p_value}")
print('')
interpret_correlation(spearman_corr, spearman_p_value, 'AHRR_A')

corr = create_correction_matrix(data)
print(corr)