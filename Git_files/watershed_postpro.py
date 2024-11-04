import os
import pandas as pd

def get_numerical_columns(dataframe):
    """
    Returns a list of the names of numerical columns in the dataframe.

    :param dataframe: Pandas DataFrame
    :return: List of numerical column names
    """
    # Select columns with numerical data types
    numerical_cols = dataframe.select_dtypes(include=['int64', 'float64', 'uint64']).columns

    return list(numerical_cols)

def calculate_average(dataframe, column_name, value_list, cols):
    """
    Calculate the average of rows in a dataframe where the values in a specified column are in a given list.

    :param dataframe: Pandas DataFrame
    :param column_name: The name of the column to check the values
    :param value_list: List of values to filter the rows
    :return: DataFrame with the average of the rows meeting the condition
    """
    # Filter the DataFrame based on the values in the specified column
    filtered_df = dataframe[dataframe[column_name].isin(value_list)]
    print(filtered_df)
    # Calculate the average of the filtered DataFrame
    average_df = filtered_df[cols].mean()

    return average_df

# Set the input directory
input_d = input("Enter the input directory: ")

# Set the output directory
output_folder = input("Enter the output directory: ")
value_text = open("Lower Salt Fork Arkansas.txt", "r")
value = value_text.read().split(',')

all_columns_text = open("columns.txt", "r")
all_columns = all_columns_text.read().split(',')

full_out = pd.DataFrame(columns=all_columns)
for f in os.listdir(input_d):
    if f.endswith(".csv"):
        input_file_path = os.path.join(input_d, f)
        data = pd.read_csv(input_file_path)
        cols = get_numerical_columns(data)
        out_data = calculate_average(data, 'PageName', value,cols)
        full_out = pd.concat([full_out[cols],out_data])

full_out.to_csv('RF_averages_1000.csv', index=False)