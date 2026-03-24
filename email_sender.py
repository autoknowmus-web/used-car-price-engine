import smtplib
from email.mime.text import MIMEText

import os

sender_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")

def send_email(to_email, message_text):

    msg = MIMEText(message_text)
    msg["Subject"] = "Used Car Price Estimate"
    msg["From"] = sender_email
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    server.send_message(msg)
    server.quit()

    print("Email sent successfully")