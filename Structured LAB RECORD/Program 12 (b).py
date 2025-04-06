import pandas as pd

df = pd.read_csv(r'C:\Path\To\Your\File\laptop_data.csv')

screen_size_column = "Screen_size_inches"  
if screen_size_column in df.columns:
    Q1 = df[screen_size_column].quantile(0.25)  
    Q3 = df[screen_size_column].quantile(0.75)  
    IQR = Q3 - Q1 
  
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[screen_size_column] < lower_bound) | (df[screen_size_column] > upper_bound)]

    print(f"Outliers in '{screen_size_column}' column:")
    print(outliers)

    print("\nScreen_size_inches column statistics:")
    print(f"Q1 (25th percentile): {Q1}")
    print(f"Q3 (75th percentile): {Q3}")
    print(f"IQR: {IQR}")
    print(f"Lower Bound: {lower_bound}")
    print(f"Upper Bound: {upper_bound}")
else:
    print(f"Column '{screen_size_column}' not found in the dataset. Please check the column name.")
