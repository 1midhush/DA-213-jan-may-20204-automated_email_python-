# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:56:42 2024

@author: 
"""

import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("SENDER_EMAIL")
password_email = os.getenv("PASSWORD_EMAIL")

def send_email(subject, name, receiver_email, percent, invoice_no, amount):
    # create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("IIT Guwahati", sender_email))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email
    
    msg.set_content(
        f"""\
        Dear {name},
        We hope this email finds you well.
        We just wanted to drop you a quick note to remind you that out of 30 days you were present only {amount} days in class and you have {percent}% of total 100% attendance.
        We would be really grateful if you could contact us and give us a reason for your absence and from now onwards you have to come to class daily.
        Otherwise, you will have to face consequences.
        Best regards,
        Team MinTech
        Professor
        IIT Guwahati
        """
    )
    
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Dear {name},</p>
        <p>We hope this email finds you well.</p>
        <p>We just wanted to drop you a quick note to remind you that out of 30 days of classes you were present only in <strong>{amount} days</strong> of class and you have <strong>{percent}</strong> of total 100% attendance.</p>
        <p>We would be really grateful if you could contact us and give us a reason for your absence and from now onwards you have to come to class daily.</p>
        <p>Otherwise, you will have to face consequences.</p>
        <p>Best regards,</p>
        <p>Team MinTech</p>
        <p>Professor</p>
        <p>IIT Guwahati</p>
      </body>
    </html>
    """,
        subtype="html",
    )
    
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Mail Sent Successfully!!!!")
        
if __name__ == "__main__":
    send_email(
        subject="Attendance Reminder: 220150026",
        name="Sirigudi Midhush",
        receiver_email="sirigudimidhush@gmail.com",
        percent="90%",
        invoice_no="220150026",
        amount="27",
    )
