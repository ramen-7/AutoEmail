import pandas as pd
import smtplib as sm


df = pd.read_csv('emails.csv') #a csv file of all email ids
emails = df['emails'].values
print(emails)

server = sm.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your email id", "password")
msg = """Enter message body"""
subject = "Enter Subject"
body = "Subject: {}\n\n{}".format(subject, msg)
for email in emails:
    server.sendmail("email id used in login", email, body)
server.quit()