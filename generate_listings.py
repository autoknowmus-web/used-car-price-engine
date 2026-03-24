import sqlite3
import random

conn = sqlite3.connect("cars.db")
cursor = conn.cursor()

city = "Bangalore"

cars = {
    "Maruti Suzuki": {
        "Swift": 800000,
        "Baleno": 900000,
        "WagonR": 650000,
        "Brezza": 1100000
    },
    "Hyundai": {
        "i20": 950000,
        "Creta": 1400000,
        "Venue": 1100000
    },
    "Honda": {
        "City": 1400000,
        "Amaze": 900000
    },
    "Toyota": {
        "Innova": 2200000,
        "Fortuner": 4200000,
        "Glanza": 900000
    },
    "Tata": {
        "Nexon": 1100000,
        "Punch": 700000,
        "Harrier": 1900000
    },
    "Mahindra": {
        "Thar": 1700000,
        "Scorpio": 1800000,
        "XUV700": 2200000
    }
}

fuels = ["Petrol", "Diesel"]

for brand in cars:

    for model in cars[brand]:

        base_price = cars[brand][model]

        for i in range(60):

            year = random.randint(2016, 2026)

            km = random.randint(5000, 120000)

            fuel = random.choice(fuels)

            age = 2026 - year

            price = base_price

            # age depreciation
            price -= age * (base_price * 0.08)

            # km impact
            price -= (km / 1000) * 700

            # random market variation
            price += random.randint(-30000, 30000)

            price = max(price, base_price * 0.25)

            cursor.execute("""
            INSERT INTO car_listings
            (brand, model, year, km, fuel, city, price)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (brand, model, year, km, fuel, city, int(price)))

conn.commit()
conn.close()

print("Synthetic Bangalore dataset created successfully")