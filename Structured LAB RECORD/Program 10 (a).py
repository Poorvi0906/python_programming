import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

data = {
    "Laptop": ["Laptop A", "Laptop B", "Laptop C", "Laptop D"],
    "Operating System": ["Windows", "macOS", "Linux", "Windows"],
    "Storage": ["256GB", "512GB", "1TB", "256GB"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

onehot_encoder = OneHotEncoder(sparse_output=False)  # corrected sparse=False to sparse_output=False
os_encoded = onehot_encoder.fit_transform(df[["Operating System"]])

os_encoded_df = pd.DataFrame(os_encoded, columns=onehot_encoder.get_feature_names_out(["Operating System"]))
df = pd.concat([df, os_encoded_df], axis=1)

df.drop("Operating System", axis=1, inplace=True)

label_encoder = LabelEncoder()
df["Storage_Encoded"] = label_encoder.fit_transform(df["Storage"])

df.drop("Storage", axis=1, inplace=True)

print("\nDataFrame after encoding:")
print(df)