import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from natsort import natsorted
from sklearn.preprocessing import StandardScaler
import os
import string
import warnings
import sys

# The script will separate the CSV file based on the 'Date' column and save new CSV files with the date in their names.

def separate_csv_by_date(filename,input_file_path, output_folder):
    import pandas as pd
    import os

    # Load the original CSV
    data = pd.read_csv(input_file_path)

    # Ensure the 'Date' column is in datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Create a directory for output if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Group by date and save each group as a separate CSV
    for (date, group) in data.groupby(data['Date'].dt.strftime('%Y-%m-%d')):
        output_file_name = filename.replace('.csv', '') + '_' + f"{date}.csv"
        output_file_path = os.path.join(output_folder, output_file_name)
        group.to_csv(output_file_path, index=False)

    print("CSV files have been separated by date.")

# Set the input directory
input_d = input("Enter the input directory: ")

# Set the output directory
output_folder = input("Enter the output directory: ")
for f in os.listdir(input_d):
    if f.endswith(".csv"):
        input_file_path = os.path.join(input_d, f)
        separate_csv_by_date(f, input_file_path, output_folder)


# # Run the script
# separate_csv_by_date(input_file_path, output_folder)