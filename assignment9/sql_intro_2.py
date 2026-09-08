import sqlite3
import pandas as pd

# Task 5: Connect to lesson.db
conn = sqlite3.connect("../db/lesson.db")

query = """
    SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, 
           products.product_name, products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, conn)
conn.close()

print("--- First 5 lines of raw query result ---")
print(df.head())

# Task 5: Calculate total column
df['total'] = df['quantity'] * df['price']
print("\n--- First 5 lines with total column ---")
print(df.head())

# Task 5: Group by product_id with specified aggregations
summary_df = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
})

print("\n--- First 5 lines of aggregated data ---")
print(summary_df.head())

# Task 5: Sort by product_name
summary_df = summary_df.sort_values(by='product_name')

# Task 5: Write out order_summary.csv
summary_df.to_csv("order_summary.csv", index=False)
print("\nSuccessfully wrote order_summary.csv")


#