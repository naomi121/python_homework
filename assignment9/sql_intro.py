import os
import sqlite3

# Task 1: Create connection and ensure directory exists
os.makedirs("../db", exist_ok=True)

try:
    conn = sqlite3.connect("../db/magazines.db")
    # Task 3: Enable foreign key enforcement
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Task 2: Define Database Structure
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        )
    """)
    conn.commit()
except sqlite3.Error as e:
    print(f"Database setup error: {e}")

# Task 3: Functions to populate tables
def add_publisher(name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

def add_magazine(name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

def add_subscriber(name, address):
    try:
        cursor.execute(
            "SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", 
            (name, address)
        )
        if not cursor.fetchone():
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding subscriber: {e}")

def add_subscription(subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute(
            "SELECT subscription_id FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
            (subscriber_id, magazine_id)
        )
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                (subscriber_id, magazine_id, expiration_date)
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding subscription: {e}")

# Task 3: Populate each table with at least 3 entries
add_publisher("Penguin Publishing")
add_publisher("National Geographic Partners")
add_publisher("Hearst Communications")

add_magazine("Tech Monthly", 1)
add_magazine("Nature World", 2)
add_magazine("Style & Home", 3)

add_subscriber("Alice Smith", "123 Main St")
add_subscriber("Bob Jones", "456 Oak Ave")
add_subscriber("Charlie Brown", "789 Pine Rd")

add_subscription(1, 1, "2026-12-31")
add_subscription(2, 2, "2027-06-30")
add_subscription(3, 3, "2026-10-15")

# Task 4: Write SQL Queries
print("--- Query 1: All Subscribers ---")
try:
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Query error: {e}")

print("\n--- Query 2: Magazines Sorted by Name ---")
try:
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Query error: {e}")

print("\n--- Query 3: Magazines for a Particular Publisher ---")
try:
    cursor.execute("""
        SELECT magazines.name, publishers.name 
        FROM magazines 
        JOIN publishers ON magazines.publisher_id = publishers.publisher_id 
        WHERE publishers.name = 'Penguin Publishing'
    """)
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Query error: {e}")

# Task 1: Close connection
conn.close()