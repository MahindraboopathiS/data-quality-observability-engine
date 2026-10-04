import pandas as pd
import sqlite3

# Load both sheets
df1 = pd.read_excel("data/online_retail_II.xlsx", sheet_name="Year 2009-2010")
df2 = pd.read_excel("data/online_retail_II.xlsx", sheet_name="Year 2010-2011")

# Combine
df = pd.concat([df1, df2], ignore_index=True)

# Rename columns
df.columns = [
    "invoice_no",
    "stock_code",
    "description",
    "quantity",
    "invoice_date",
    "unit_price",
    "customer_id",
    "country"
]

# Save to SQLite
conn = sqlite3.connect("data/pipeline.db")
df.to_sql("raw_transactions", conn, if_exists="replace", index=False)
conn.close()

print("Raw data loaded successfully!")