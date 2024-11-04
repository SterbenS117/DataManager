import os
import pandas as pd

index = pd.read_csv("E:\share\BIgRun\All_tables\Grid_1000_ExportTable.csv", usecols=['PageName']).set_index('PageName')
def combine_mean_columns(directory):
    mean_columns = []

    # List all CSV files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)

            # Read each CSV file
            df = pd.read_csv(filepath).set_index('PageName')

            var_name= filename.split('_')
            # Check if 'MEAN' column exists
            if 'MEAN' in df.columns:
                if df['MEAN'].max() > 500 and var_name[0] != 'Elevation':
                    df['MEAN'] = df['MEAN']/10_000
                # Append the 'MEAN' column to the list
                index[var_name[0]] = df['MEAN']
                mean_columns.append(df['MEAN'])

    # Combine all 'MEAN' columns into a single DataFrame
    combined_df = pd.concat(mean_columns, axis=1)

    # Save the combined DataFrame to a new CSV file
    index.to_csv('E:\share\BIgRun\All_tables\static_1000.csv', index=True)

# Usage
directory = 'E:\share\BIgRun\All_tables\S1000\ewfolder'  # Replace with your directory path
combine_mean_columns(directory)
