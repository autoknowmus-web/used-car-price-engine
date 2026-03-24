import sqlite3
import statistics
from whatsapp_sender import send_whatsapp


def get_price(brand, model, year, km, city, phone):

    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()

    year_low = year - 2
    year_high = year + 2

    km_low = km - 20000
    km_high = km + 20000

    cursor.execute("""
    SELECT price FROM car_listings
    WHERE brand = ?
    AND model = ?
    AND city = ?
    AND year BETWEEN ? AND ?
    AND km BETWEEN ? AND ?
    """,
    (brand, model, city, year_low, year_high, km_low, km_high))

    rows = cursor.fetchall()
    
    conn.close()

    if not rows:
        print("No comparable cars found")
        return

    prices = [r[0] for r in rows]

    median_price = statistics.median(prices)

    low_price = int(median_price * 0.95)
    high_price = int(median_price * 1.05)

    message = f"""
Used Car Price Estimate 🚗

Car: {brand} {model}
Year: {year}
KM Driven: {km}
City: {city}

Estimated Price Range:
₹{low_price} - ₹{high_price}

Average Market Price:
₹{int(median_price)}
"""

    print(message)

    send_whatsapp(phone, message)