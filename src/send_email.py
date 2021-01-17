from email.mime.text import MIMEText
import os
import smtplib


def send_email(email, height, avg, count):
    from_email = os.getenv("EMAIL")
    from_password = os.getenv("PASSWORD")
    to_email = email

    subject = "Height data"
    msg = f"Hey there, your height is <strong>{height}</strong>. Average height of {count} registered people is {avg}"
    body = MIMEText(msg, "html")
    body["Subject"] = subject
    body["To"] = to_email
    body["From"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(body)
