# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:42:29 2024

@author:
""" 

import pandas as pd
from send_email import send_email
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


SHEET_ID = "1qnAWraUMfVifNwauGRt4_vM_I8_acz3tJUBRSP4yyYU"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/1qnAWraUMfVifNwauGRt4_vM_I8_acz3tJUBRSP4yyYU/edit?usp=sharing"

def load_df(url):
    df = pd.read_csv(url)
    return df

def query_data_and_send_emails(df):
    email_counter = 0
    for _, row in df.iterrows():
        if row["greater_than_75_percent"] == "no":
            send_email(
                subject = f'Attendance Reminder (Roll No:{row["Roll_No"]})',
                name = row["name"],
                receiver_email=row["email"],
                percent=row["percentage_of_attendance"],
                invoice_no=row["Roll_No"],
                amount=row["present_at_working_day"],
                )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"        

# Manually sending mail
# df = load_df(URL)
# result = query_data_and_send_emails(df)
# print(result)

# Using schedule library
def job_function():
    print(f"Executing job_function at {datetime.now()}")
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    print(result)
    print("Email sending completed........")
    print("Press any key to continue..")

print("Scheduling started......")
scheduler = BackgroundScheduler(timezone='Asia/Kolkata')

scheduler.add_job(job_function, 'cron', hour=18, minute=40)

scheduler.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Scheduler stopped manually")    

# By Flask server
"""
from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def hello_world():
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    return result
 
if __name__ == '__main__':
    app.run()
"""
