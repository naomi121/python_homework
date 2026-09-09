import os
import sqlite3

# Define relative path to lesson.db
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.abspath(os.path.join(script_dir, "..", "db", "lesson.db"))

conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

print("=" * 60)
print("TASK 1: Complex JOINs with Aggregation")
print("=" * 60)

# Task 1: Find total price for each of the first 5 orders
task1_query = """
    SELECT orders.order_id, SUM(products.price * line_items.quantity) AS total_price
    FROM orders
    JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON line_items.product_id = products.product_id
    GROUP BY orders.order_id
    ORDER BY orders.order_id
    LIMIT 5;
"""

cursor.execute(task1_query)
rows = cursor.fetchall()
for row in rows:
    print(f"Order ID: {row[0]} | Total Price: ${row[1]:.2f}")


print("\n" + "=" * 60)
print("TASK 2: Understanding Subqueries")
print("=" * 60)

# Task 2: Find average order price per customer using a subquery
task2_query = """
    SELECT customers.customer_name, AVG(sub.total_price) AS average_total_price
    FROM customers
    LEFT JOIN (
        SELECT orders.customer_id AS customer_id_b, orders.order_id, 
               SUM(products.price * line_items.quantity) AS total_price
        FROM orders
        JOIN line_items ON orders.order_id = line_items.order_id
        JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
    ) AS sub ON customers.customer_id = sub.customer_id_b
    GROUP BY customers.customer_id;
"""

cursor.execute(task2_query)
rows = cursor.fetchall()
for row in rows:
    avg_price = f"${row[1]:.2f}" if row[1] is not None else "N/A"
    print(f"Customer Name: {row[0]} | Avg Order Price: {avg_price}")


print("\n" + "=" * 60)
print("TASK 3: An Insert Transaction Based on Data")
print("=" * 60)

try:
    # 1. Fetch customer_id for 'Perez and Sons'
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';")
    customer_res = cursor.fetchone()
    if not customer_res:
        raise ValueError("Customer 'Perez and Sons' not found.")
    customer_id = customer_res[0]

    # 2. Fetch employee_id for 'Miranda Harris'
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
    employee_res = cursor.fetchone()
    if not employee_res:
        raise ValueError("Employee 'Miranda Harris' not found.")
    employee_id = employee_res[0]

    # 3. Fetch product_ids of 5 least expensive products
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
    products_res = cursor.fetchall()
    product_ids = [p[0] for p in products_res]

    # 4. Perform transaction
    conn.execute("BEGIN TRANSACTION;")

    # Insert order record and return generated order_id
    cursor.execute(
        "INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id;",
        (customer_id, employee_id)
    )
    new_order_id = cursor.fetchone()[0]

    # Insert line items (10 units for each of the 5 least expensive products)
    for p_id in product_ids:
        cursor.execute(
            "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);",
            (new_order_id, p_id, 10)
        )

    conn.commit()
    print(f"Successfully created Order #{new_order_id} in a single transaction.")

    # 5. Query and display the newly created line items
    task3_select = """
        SELECT line_items.line_item_id, line_items.quantity, products.product_name
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
        WHERE line_items.order_id = ?;
    """
    cursor.execute(task3_select, (new_order_id,))
    line_item_rows = cursor.fetchall()

    print("\nCreated Order Line Items:")
    for item in line_item_rows:
        print(f"Line Item ID: {item[0]} | Quantity: {item[1]} | Product Name: {item[2]}")

except Exception as e:
    conn.rollback()
    print(f"Transaction failed and rolled back: {e}")


print("\n" + "=" * 60)
print("TASK 4: Aggregation with HAVING")
print("=" * 60)

# Task 4: Find employees associated with more than 5 orders
task4_query = """
    SELECT employees.employee_id, employees.first_name, employees.last_name, COUNT(orders.order_id) AS order_count
    FROM employees
    JOIN orders ON employees.employee_id = orders.employee_id
    GROUP BY employees.employee_id
    HAVING COUNT(orders.order_id) > 5;
"""

cursor.execute(task4_query)
rows = cursor.fetchall()
for row in rows:
    print(f"Employee ID: {row[0]} | Name: {row[1]} {row[2]} | Total Orders: {row[3]}")

# Close database connection
conn.close()