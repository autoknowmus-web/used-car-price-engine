import sqlite3

# connect to database
conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

# sample car data
brand = "Honda"
model = "City"
year = 2019
km = 45000
fuel = "Petrol"
city = "Bangalore"
price = 795000

# insert data
cursor.execute("""
INSERT INTO car_listings
(brand, model, year, km, fuel, city, price)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (brand, model, year, km, fuel, city, price))

conn.commit()
conn.close()

print("Car inserted successfully")