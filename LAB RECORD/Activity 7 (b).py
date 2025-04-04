import pandas as pd

df = pd.read_csv(r'C:\SHANTHI\RVU\Programs\Minors\IDA\Activities\Datasets\6Mcd_null_values.csv')

df.fillna(df.mean(numeric_only=True), inplace=True)
df.fillna({col: df[col].mode()[0] for col in df.columns if df[col].dtype == 'object'}, inplace=True)

df.drop_duplicates(inplace=True)

print(df)
