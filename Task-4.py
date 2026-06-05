import pandas as pd

products = [
    ["Laptop", 50000, 4.5],
    ["Mobile", 20000, 4.2],
    ["Headphones", 1500, 4.0]
]

df = pd.DataFrame(products, columns=["Name", "Price", "Rating"])

df.to_csv("products.csv", index=False)

print("Product data saved to products.csv")
