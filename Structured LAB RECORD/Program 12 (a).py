import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\poorv\Downloads\4laptops.csv")

print("Dataset:")
print(df.head())

column_to_plot = "Price" 

if column_to_plot in df.columns:
  
    plt.figure(figsize=(8, 6))
    plt.boxplot(df[column_to_plot])
    plt.title(f"Box Plot of {column_to_plot} (Matplotlib)")
    plt.ylabel("Values")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[column_to_plot], color='blue')
    plt.title(f"Box Plot of {column_to_plot} (Seaborn)")
    plt.xlabel("Values")
    plt.grid(True)
    plt.show()
else:
    print(f"Column '{column_to_plot}' not found in the dataset. Please check the column name.")
