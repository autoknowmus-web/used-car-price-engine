from twilio.rest import Client

import os

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

client = Client(account_sid, auth_token)

def send_whatsapp(phone, message_text):

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_text,
        to=f'whatsapp:{phone}'
    )

    print("WhatsApp sent:", message.sid)