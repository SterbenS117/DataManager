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

def rank_corr(data, hist_monthly_average):
    data['Soil'] = data['Sand'] + data['Silt'] + data['Clay']
    data = data[data['Soil'] >= 99.99]
    # print(data.dtypes)
    ml_month_ave = data[['ML_', 'Year', 'Month', 'PageName']].groupby(['Year', 'Month', 'PageName']).mean()
    ml_month_ave.reset_index(inplace=True)
    hist_ml_month_ave = ml_month_ave[['ML_', 'Month', 'PageName']].groupby(
        ['Month', 'PageName']).mean()  # .reset_index()

    hist_ml_month_ave.reset_index(inplace=True)

    hist_ml_month_ave.rename(columns={'ML_': 'ML_M'}, inplace=True)

    data_m = data.merge(hist_ml_month_ave, on=['PageName', 'Month'])

    data_t = data_m.merge(hist_monthly_average, on=['PageName', 'Month'])

    data_t.drop(columns=[''], inplace=True)

    data_t['SMERGE_A'] = data_t['SMERGE'] - data_t['SMERGE_M']
    data_t['ML_A'] = data_t['ML_'] - data_t['SMERGE_M']  # data_t['ML_M']
    data_t['AHRR_A'] = data_t['AHRR'] - data_t['AHRR_M']

    data_t = data_t[data_t['Month'] > 5]
    data_t = data_t[data_t['Month'] < 9]

    import numpy as np
    from scipy.stats import spearmanr, kendalltau
    d = data_t.groupby(['Month', 'Year']).agg(avg_AHRR_A=('AHRR_A', 'mean'),
                                              avg_Smerge_A=('SMERGE_A', 'mean')).reset_index()
    # Sample data
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

    d = data_t.groupby(['Month', 'Year']).agg(avg_AHRR_A=('AHRR_A', 'mean'), avg_ML_A=('ML_A', 'mean')).reset_index()
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

hist_monthly_average = pd.read_csv(r"E:\BigRun\anamoly_calculated_dataV4_500.csv", engine='pyarrow')

landC_2008 = pd.read_csv(r"E:\BigRun\Land_Cover\grid_500_landcover2008.csv", engine='pyarrow').rename(columns={'PAGENAME': 'PageName'})
landC_2011 = pd.read_csv(r"E:\BigRun\Land_Cover\grid_500_landcover2011.csv", engine='pyarrow').rename(columns={'PAGENAME': 'PageName'})
landC_2013 = pd.read_csv(r"E:\BigRun\Land_Cover\grid_500_landcover2013.csv", engine='pyarrow').rename(columns={'PAGENAME': 'PageName'})
landC_2016 = pd.read_csv(r"E:\BigRun\Land_Cover\grid_500_landcover2016.csv", engine='pyarrow').rename(columns={'PAGENAME': 'PageName'})
landC_2019 = pd.read_csv(r"E:\BigRun\Land_Cover\grid_500_landcover2019.csv", engine='pyarrow').rename(columns={'PAGENAME': 'PageName'})


#data = pd.read_csv(r"E:\share\BIgRun\Watershed_Cal\2\RF_BigRunWS4_500.csv", engine='pyarrow')
#data = pd.read_csv(r"E:\share\BIgRun\Watershed_Cal\4\GBR_BigRunWS5_1_500.csv", engine='pyarrow')
data = pd.read_csv(r"E:\BigRun\T2\RF_BigRunWS_V5_T2_500.csv", engine='pyarrow')
try:
    data.drop(columns=['PPT'], inplace=True)
except:
    print('No PPT')

data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year
data = data[data['Year'] < 2018]
data.dropna(inplace=True)


data_L2008 = data[(data['Year'] > 2006) & (data['Year'] <= 2009)]
data_L2011 = data[(data['Year'] > 2009) & (data['Year'] <= 2012)]
data_L2013 = data[(data['Year'] > 2012) & (data['Year'] <= 2014)]
data_L2016 = data[(data['Year'] > 2014) & (data['Year'] <= 2016)]
data_L2019 = data[(data['Year'] > 2016) & (data['Year'] <= 2020)]

data_L2008_M = pd.merge(data_L2008, landC_2008[['PageName', 'MAJORITY']], on='PageName', how='left')
data_L2011_M = pd.merge(data_L2011, landC_2011[['PageName', 'MAJORITY']], on='PageName', how='left')
data_L2013_M = pd.merge(data_L2013, landC_2013[['PageName', 'MAJORITY']], on='PageName', how='left')
data_L2016_M = pd.merge(data_L2016, landC_2016[['PageName', 'MAJORITY']], on='PageName', how='left')
data_L2019_M = pd.merge(data_L2019, landC_2019[['PageName', 'MAJORITY']], on='PageName', how='left')

all_data = pd.concat([data_L2008_M, data_L2011_M, data_L2013_M, data_L2016_M, data_L2019_M], ignore_index=True)

#Developed 21, 22, 23, 24
#Category A (Herbaceous, Cropland, Developed)
category_A = [71, 81, 82]
#Category B (Scrubland, Barren)
category_B = [52, 31]
#Category C (Forest, Wetlands)
category_C = [41, 42, 43, 90, 95]


data_A = all_data.loc[all_data['MAJORITY'].isin(category_A)]
data_B = all_data.loc[all_data['MAJORITY'].isin(category_B)]
data_C = all_data.loc[all_data['MAJORITY'].isin(category_C)]
data_D = all_data.loc[~all_data['MAJORITY'].isin([21,22,23,24])]


#
#
# corr = create_correction_matrix(data_t)
# print(corr)