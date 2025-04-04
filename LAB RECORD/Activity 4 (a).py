import pandas as pd
# Replaceing the 'your_file.csv' with the path to your CSV file
csv_file_path = 'your_file.csv'
# Reading the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
# Displaying  the last 3 rows only
print("Last 3 rows of the DataFrame:")
print(df.tail(3))
# Displaying the description and information of the DataFrame
print("\nDescription of the DataFrame:")
print(df.describe())
print("\nInformation about the DataFrame:")
print(df.info())
# Displaying the column names
print("\nColumn names of the DataFrame:")
print(df.columns)
