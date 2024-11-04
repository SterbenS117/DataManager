import pandas as pd
from sklearn.model_selection import train_test_split
print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
# # Sample DataFrame creation
# # This is just for demonstration; replace it with your actual DataFrame
# df = pd.read_csv("E:\share\BIgRun\All_tables\BigRunE_500_train.csv")
# print(df)
# # Randomly split df into two DataFrames: df1 and df2
# # Adjust test_size to change the proportion of the split
# df1, df2 = train_test_split(df, test_size=0.5, random_state=42)
#
# df1.to_csv("E:\share\BIgRun\All_tables\BigRunE1_500_train.csv", index=False)
# df2.to_csv("E:\share\BIgRun\All_tables\BigRunE2_500_train.csv", index=False)

# Sample DataFrame creation
# This is just for demonstration; replace it with your actual DataFrame
df = pd.read_csv("E:\share\BIgRun\All_tables\BigRunE_500_test.csv")
print(df)
# Randomly split df into two DataFrames: df1 and df2
# Adjust test_size to change the proportion of the split
df1, df2 = train_test_split(df, test_size=0.5, random_state=42)

df1.to_csv("E:\share\BIgRun\All_tables\BigRunE1_500_test.csv", index=False)
df2.to_csv("E:\share\BIgRun\All_tables\BigRunE2_500_test.csv", index=False)
