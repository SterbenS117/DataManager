import pandas as pd
import os


def split_csv_into_12(dir,file_path, name):
    # Read the original CSV file
    df = pd.read_csv(file_path, engine='pyarrow').sample(frac=1).reset_index(drop=True)

    # Calculate the number of rows per split
    num_rows = len(df)
    rows_per_split = num_rows // 10

    # Create a directory to store the split CSV files
    output_dir = dir #r"E:\share\BIgRun\Watershed_Cal"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(10):
        start_row = i * rows_per_split
        # Handle the last split to include any remaining rows
        if i == 19:
            end_row = num_rows
        else:
            end_row = (i + 1) * rows_per_split

        # Slice the dataframe
        df_split = df[start_row:end_row]

        # Define the output file path
        output_file_path = os.path.join(output_dir, name + f"{i + 1}.csv")

        # Write the split dataframe to a new CSV file
        df_split.to_csv(output_file_path, index=False)

    print(f"CSV file split into 12 parts and saved in directory: {output_dir}")

# Example usage (commented out to prevent execution in PCI)
# split_csv_into_12("path/to/your/input.csv")
# file = r'E:\share\BIgRun\Watershed_Cal\T\BigRunWS_V5_2_500_train.csv'
# split_csv_into_12(r'E:\share\BIgRun\Watershed_Cal\T',file, 'BigRunWS_V5_T_500_train_part_')
#
# file = r'E:\share\BIgRun\Watershed_Cal\T\BigRunWS_V5_2_500_test.csv'
# split_csv_into_12(r'E:\share\BIgRun\Watershed_Cal\T',file, 'BigRunWS_V5_T_500_test_part_')

# file = r'E:\BigRun\BigRunWS5_L_500_train.csv'
# split_csv_into_12(r'E:\BigRun',file, 'BigRunWS_V5_L_500_train_part_')

# file = r'E:\BigRun\BigRunWS5_L_500_test.csv'
# split_csv_into_12(r'E:\BigRun',file, 'BigRunWS_V5_L_500_test_part_')

file = r'E:\BigRun\BigRunWS_V5_TS_500_train.csv'
split_csv_into_12(r'E:\BigRun',file, 'BigRunWS_V5_TS_500_train_part_')

file = r'E:\BigRun\BigRunWS_V5_TS_500_test.csv'
split_csv_into_12(r'E:\BigRun',file, 'BigRunWS_V5_TS_500_test_part_')