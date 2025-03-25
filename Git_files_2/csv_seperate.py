import pandas as pd


def split_csv_into_parts(input_file, output_prefix, parts=15):
    # Read the input CSV file
    data = pd.read_csv(input_file)

    # Calculate the number of rows per part
    rows_per_part = len(data) // parts
    remainder = len(data) % parts

    start_row = 0

    for i in range(parts):
        # Calculate end row for this part
        end_row = start_row + rows_per_part + (1 if i < remainder else 0)

        # Extract the part
        part_data = data[start_row:end_row]

        # Save the part to a new CSV file
        part_filename = f"{output_prefix}_part_{i + 1}.csv"
        part_data.to_csv(part_filename, index=False)

        # Update the start row for the next part
        start_row = end_row


# Example usage
input_file = r"E:\BigRun\2025_Big\BigRunWS_V6D_500_2-7-2025.csv"
output_prefix = r"E:\BigRun\2025_Big\BigRunWS_V6_500"
split_csv_into_parts(input_file, output_prefix)
