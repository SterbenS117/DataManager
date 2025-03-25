import pandas as pd
import os
import numpy as np


def average_csv_by_index(directory_path, output_filename):
    # List to hold data from each CSV file
    dataframes = []

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            # Construct full file path
            file_path = os.path.join(directory_path, filename)
            # Read the CSV file with the first column as index
            df = pd.read_csv(file_path, index_col=0)
            dataframes.append(df)

    # Concatenate all DataFrames in the list along the columns (axis=1)
    # This assumes that all CSVs have the same indexes but potentially different columns
    combined_df = pd.concat(dataframes, axis=1)

    # Calculate the mean across columns for each row (index)
    # Replace NaN values with 0 or your preferred value before calculating the mean
    # If each CSV contains exactly the same columns, and you only want to average those, you can directly use mean(axis=1)
    mean_df = combined_df.groupby(level=0, axis=1).mean()

    # Save the resulting DataFrame to a new CSV file
    mean_df.to_csv(os.path.join(directory_path, output_filename))
    print(f"Mean values by index saved as {output_filename}")


# Example usage
directory_path = r'E:\BigRun\2025\WS\Sense\RF'  # Replace this with your directory path
output_filename = 'RF_BigRunWS_WS6PD_500_IMMD.csv'  # Name of the output file
average_csv_by_index(directory_path, output_filename)