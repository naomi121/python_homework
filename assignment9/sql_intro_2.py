import os
import sqlite3
import pandas as pd

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Connect to lesson.db database dynamically
db_path = os.path.abspath(os.path.join(script_dir, "..", "db", "lesson.db"))

conn = sqlite3.connect(db_path)

# 2. Join line_items and products tables
query = """
    SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, 
           products.product_name, products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, conn)
conn.close()

# 3. Print first 5 rows of raw joined data
print("--- First 5 lines of raw query result ---")
print(df.head())

# 4. Add calculated 'total' column
df['total'] = df['quantity'] * df['price']
print("\n--- First 5 lines with total column ---")
print(df.head())

# 5. Group by product_id and aggregate count, sum, and product_name
summary_df = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
})

print("\n--- First 5 lines of aggregated data ---")
print(summary_df.head())

# 6. Sort by product_name
summary_df = summary_df.sort_values(by='product_name')

# 7. Write results to order_summary.csv in assignment9 folder
output_csv_path = os.path.join(script_dir, "order_summary.csv")
summary_df.to_csv(output_csv_path, index=False)
print("\nSuccessfully generated order_summary.csv")