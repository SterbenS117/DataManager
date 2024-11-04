import pandas as pd

# Load the CSV files
csv2 = pd.read_csv(r"E:\BigRun\Grid_500_Spatial_ExportTable.csv")
csv1 = pd.read_csv(r"E:\BigRun\L\XGB_BigRunWS_V5_L11_500.csv")


# Merge the two DataFrames on the 'PageName' column
merged_csv = pd.merge(csv1, csv2[['PageName', 'name_1']], on='PageName', how='left')

# Save the result to a new CSV file
merged_csv.to_csv(r'E:\BigRun\L\XGB_BigRunWS_V5_L11_nwater.csv', index=False)
#merged_csv.to_csv('/mnt/d/BigRun_NDVI/WS_5/XGB_BigRunWS3_nwater.csv', index=False)

print("Merged CSV has been saved as 'merged_file.csv'")
