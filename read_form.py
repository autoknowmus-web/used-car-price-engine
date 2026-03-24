import gspread
from oauth2client.service_account import ServiceAccountCredentials

# define scope
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive'
]

# load credentials
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# authorize client
client = gspread.authorize(creds)

# open your sheet
sheet = client.open_by_key("1-3eNphci2chZWbH9eOt-4mNx2NXrV41znZm4O43l2tk").sheet1

# read all rows
data = sheet.get_all_records()

from price_engine import get_price

from price_engine import get_price

# get latest form response
row = data[-1]

timestamp = row['Timestamp']

# read last processed timestamp
with open("last_processed.txt", "r") as f:
    last_timestamp = f.read()

# check if new form submitted
if str(timestamp) != last_timestamp:

    brand = row['Brand']
    model = row['Model']
    year = row['Year']
    km = row.get('KM Driven') or row.get('KM Driven ')
    city = row['City']
    phone = row['WhatsApp Number']

    get_price(brand, model, year, km, city, phone)

    # update last processed timestamp
    with open("last_processed.txt", "w") as f:
        f.write(str(timestamp))

else:
    print("No new form submission")