import sqlite3

# connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

# create table for car listings
cursor.execute("""
CREATE TABLE IF NOT EXISTS car_listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    model TEXT,
    year INTEGER,
    km INTEGER,
    fuel TEXT,
    city TEXT,
    price INTEGER
)
""")

conn.commit()
conn.close()

print("Database created successfully")