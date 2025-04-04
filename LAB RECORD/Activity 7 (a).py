import pandas as pd
product_data = [
    {"Product Name": "Laptop", "Category": "Electronics", "Price": 80000},
    {"Product Name": "T-shirt", "Category": "Clothing", "Price": 1000},
    {"Product Name": "Book", "Category": "Books", "Price": 500},
    {"Product Name": "Smartphone", "Category": "Electronics", "Price": 60000},
    {"Product Name": "Coffee Maker", "Category": "Home Appliances", "Price": 3000}
]
df = pd.DataFrame(product_data)
df["Discounted Price"] = df["Price"] * 0.90

print(df)
