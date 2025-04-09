import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler

df = pd.read_csv(r"C:\Users\poorv\Downloads\3Salary_Data.csv")

print("Original Dataset:")
print(df.head())

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
data_to_scale = df[numerical_columns]

normalizer = Normalizer()
normalized_data = normalizer.fit_transform(data_to_scale)

normalized_df = pd.DataFrame(normalized_data, columns=numerical_columns)
print("\nNormalized Data (using Normalizer):")
print(normalized_df.head())

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data_to_scale)

scaled_df = pd.DataFrame(scaled_data, columns=numerical_columns)
print("\nScaled Data (using MinMaxScaler):")
print(scaled_df.head())

normalized_df.to_csv(r'C:\Path\To\Your\File\normalized_3Salary_Data.csv', index=False)
scaled_df.to_csv(r'C:\Path\To\Your\File\scaled_3Salary_Data.csv', index=False)
print("\nNormalized and scaled data have been saved to new CSV files.")
