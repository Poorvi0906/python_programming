import pandas as pd
df = pd.read_csv(r'C:\Path\To\Your\File\2Salary.csv')
print("Dataset:")
print(df)

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    print(f"\nStatistics for column: {column}")
    print(f"Mean: {df[column].mean()}")
    print(f"Median: {df[column].median()}")
    print(f"Mode: {df[column].mode()[0]}")
    print(f"Variance: {df[column].var()}")
    print(f"Standard Deviation: {df[column].std()}")
    print(f"Range: {df[column].max() - df[column].min()}")
