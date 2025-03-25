import pandas as pd
import concurrent.futures
import dask.dataframe as dd

def write_csv(df, filename):
    df.to_csv(filename, index=False)

# Load the CSV files
csv2 = pd.read_csv(r"E:\BigRun\Grid_500_Spatial_ExportTableV2.csv")
csv1 = pd.read_csv(r"E:\BigRun\2025\WS2\XGB_BigRunWS_WS6D_v3_500.csv")


# Merge the two DataFrames on the 'PageName' column
merged_csv = pd.merge(csv1, csv2[['PageName', 'name_1']], on='PageName', how='left')

merged_csv.drop(columns=['PageName'], inplace=True)
grouped_df = merged_csv.groupby(['name_1', 'Date']).mean().reset_index()
dask_df = dd.from_pandas(grouped_df, npartitions=10)

dask_df.to_csv(r'E:\BigRun\2025\WS2\XGB_BigRunWS_WS6D_v3_watershed.csv', single_file=True, index=False)
# Save the result to a new CSV file
#merged_csv.to_csv(r"E:\BigRun\2025\WS2\GBR_BigRunWS_WS6PD_nwater.csv", index=False)
#merged_csv.to_csv('/mnt/d/BigRun_NDVI/WS_5/XGB_BigRunWS3_nwater.csv', index=False)

print("Merged CSV has been saved as 'merged_file.csv'")
