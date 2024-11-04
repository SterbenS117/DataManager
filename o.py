import pandas as pd

# Create a DataFrame with columns of different types
data = {'Column1': ['A2', 'A11', 'A1', 'A20', 'A3'],
        'Column2': [pd.Timestamp('2022-01-01'), pd.Timestamp('2022-02-01'), pd.Timestamp('2022-01-15'), pd.Timestamp('2022-03-01'), pd.Timestamp('2022-02-15')],
        'Column3': ['B', 'A', 'B', 'A', 'B']}
df = pd.DataFrame(data)

# Define a custom sorting function for multiple columns, including datetime
def excel_sort(x):
    def convert_to_int(val):
        try:
            return int(val)
        except ValueError:
            return val

    # Extract and convert each part of the value for sorting
    parts = x.str.extract('(\D+)(\d+)', expand=False)
    parts[1] = parts[1].astype(str).apply(convert_to_int)
    return pd.concat([parts, df['Column2']], axis=1).values.tolist()

# Sort the DataFrame using the custom sorting function for multiple columns
df_sorted = df.sort_values(['Column1', 'Column2'], key=excel_sort)

# Display the sorted DataFrame
print(df_sorted)