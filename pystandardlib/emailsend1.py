from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "Sahana D."
message["to"] = "testuser@sgmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name":"John"})
message.attach(MIMEText(body,"html"))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@sgmail.com", "today1234")
    smtp.send_message(message)
    print("sent")
