import sqlite3
import pandas as pd

conn = sqlite3.connect("data/pipeline.db")

df = pd.read_sql("SELECT * FROM raw_transactions", conn)

# Create products table
products = df[["stock_code", "description"]].drop_duplicates()
products.to_sql("products", conn, if_exists="replace", index=False)

# Create customers table
customers = df[["customer_id", "country"]].drop_duplicates()
customers.to_sql("customers", conn, if_exists="replace", index=False)

# Create transactions table
transactions = df[[
    "invoice_no",
    "stock_code",
    "quantity",
    "invoice_date",
    "unit_price",
    "customer_id"
]]
transactions.to_sql("transactions", conn, if_exists="replace", index=False)

conn.close()

print("Data transformed into structured tables!")