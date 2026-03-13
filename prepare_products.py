import pandas as pd

print("Loading dataset...")

df = pd.read_csv("data/train.tsv", sep="\t")

print("Original rows:", len(df))

# Use subset so your Mac doesn't struggle
df = df.sample(50000, random_state=42)

products = df[[
    "train_id",
    "name",
    "category_name",
    "brand_name",
    "item_description",
    "price"
]]

products.columns = [
    "product_id",
    "title",
    "category",
    "brand",
    "description",
    "price"
]

products.to_csv("data/products.csv", index=False)

print("products.csv created successfully")
print("Rows:", len(products))