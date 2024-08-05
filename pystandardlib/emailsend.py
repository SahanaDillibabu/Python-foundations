from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Sahana D."
message["to"] = "testuser@sgmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body", "html"))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@sgmail.com", "today1234")
    smtp.send_message(message)
    print("sent")
