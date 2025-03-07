import pandas as pd
# Create a DataFrame from a dictionary
data = {
    "Name": ["Ram", "Robert", "Rahim"],
    "Age": [25, 30, 35],
    "City": ["Ayodya", "Chennai", "Delhi"],
}
df = pd.DataFrame(data)

print(df)
print("--------")

# Access a column
print("Access a column\n",df["Name"],"\n")

# Accessing a row by label
print("Accessing a row by label\n", df.loc[0], "\n")

# Access a row by index
print("Access a row by index\n", df.iloc[1], "\n")

# Access a specific cell
print("Access a specific cell\n",df.at ["delhi"],"\n")  # Corrected line
# Slicing
print("Slicing",df[1:3])  # Slicing rows