import pandas as pd
import dask.dataframe as dd
# Step 1: Read the CSV file
df = pd.read_csv(r'E:\BigRun\2025\Patch\XGB_BigRunWS_WS6PPD_nwater.csv')

# Step 2: Group by 'PageName', 'name_1', and 'date'
# This will group the DataFrame by those three columns, and for the other numeric columns, we will take the mean.
df.drop(columns=['PageName'], inplace=True)
grouped_df = df.groupby(['name_1', 'Date']).mean().reset_index()
dask_df = dd.from_pandas(grouped_df, npartitions=10)

print(grouped_df)
dask_df.to_csv(r'E:\BigRun\2025\Patch\XGB_BigRunWS_WS6PPD_watershed.csv', single_file=True, index=False)
# Step 3: Save or display the result


# Optionally, you can save the result back to a CSV file
#grouped_df.to_csv(r'E:\BigRun\L\XGB_BigRunWS_V5_L_watershed.csv', index=False)