# ----------------------------------- Send an email usint SMTPLIB -----------------------------------#
import smtplib
from credentials import *

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=gmail_address, password=gmail_password)
    connection.sendmail(from_addr=gmail_address,
                        to_addrs=yahoo_address,
                        msg="Subject: This is a subject!\n\nThis is the body of the email")

#----------------------------------- Using datetime lib -----------------------------------#
import datetime as dt
now = dt.datetime.now()
year = now.year()
