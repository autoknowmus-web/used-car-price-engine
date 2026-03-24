import sqlite3

conn = sqlite3.connect("cars.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM car_listings")

print(cursor.fetchone())

conn.close()