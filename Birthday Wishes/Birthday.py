import smtplib
from email.mime.text import MIMEText
from datetime import date
import os

password = os.getenv("EMAIL_PASSWORD")
today = date.today()
formatted_date = today.strftime("%d %B %Y")

sender = "senderemail@example.com"
receiver = "recievername@example.com"
receiver_name = input("Enter receiver name: ")

# password = "cauc wonc vgnj lfxg"

subject = f"Happy Birthday {receiver_name}! 🎂🎉"

body = f"""
Hey {receiver_name}! 🎉

Wishing you a very Happy Birthday! 🎂🎉

Today, {formatted_date}, is your special day,
so I just wanted to wish you lots of happiness,
success, and beautiful memories.

May this new year of your life bring you everything
you wish for. Have an amazing birthday! ❤️

Best wishes,
Aditya
"""

msg = MIMEText(body, "plain", "utf-8")
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())

print(f"Birthday wish sent successfully to {receiver_name}!")
