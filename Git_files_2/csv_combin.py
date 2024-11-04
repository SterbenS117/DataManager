import pandas as pd
import os


def merge_csv_files(directory_path, output_filename):
    # List to hold data from each CSV file
    dataframes = []

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            # Construct full file path
            file_path = os.path.join(directory_path, filename)
            # Read the CSV file and append it to the list
            df = pd.read_csv(file_path)
            dataframes.append(df)

    # Concatenate all DataFrames in the list
    combined_df = pd.concat(dataframes, ignore_index=True)
    print(combined_df)
    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(os.path.join(directory_path, output_filename), index=False)
    print(f"Combined CSV saved as {output_filename}")
    return combined_df

# Example usage
directory_path = '/mnt/e/BigRun/P2/GBR/'  # Replace this with your directory path
output_filename = '/mnt/e/BigRun/P2/GBR_BigRunWS3_CO_500.csv'  # Name of the output file
df = merge_csv_files(directory_path, output_filename)