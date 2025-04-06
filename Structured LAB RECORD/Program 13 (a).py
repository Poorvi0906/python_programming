import pandas as pd

data1 = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Department": ["HR", "IT", "Finance"],
    "Salary": [50000, 60000, 70000]
}

data2 = {
    "ID": [4, 5],
    "Name": ["David", "Eve"],
    "Department": ["IT", "HR"],
    "Salary": [80000, 55000]
}

data3 = {
    "ID": [1, 2, 3, 4, 5],
    "Experience": [3, 5, 7, 6, 4]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nDataFrame 3:")
print(df3)

grouped_median = df1.groupby("Department").median()
print("\nGrouped by Department (Median):")
print(grouped_median)

merged_df = pd.merge(df1, df2, how="outer")
print("\nMerged DataFrame (Outer Join):")
print(merged_df)

joined_df = df1.set_index("ID").join(df3.set_index("ID"))
print("\nJoined DataFrame:")
print(joined_df)

concat_df = pd.concat([df1, df3], axis=1)
print("\nConcatenated DataFrame (Horizontally):")
print(concat_df)
