from datetime import datetime
from random import choice
import smtplib

from credentials import *

now = datetime.now()
current_day = now.weekday()

if current_day == 0:
    with open(file='quotes.txt', mode='r') as data:
        quotes = data.readlines()
        random_quote = choice(quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=gmail_address, password=gmail_password)
        connection.sendmail(from_addr=gmail_address,
                            to_addrs=yahoo_address,
                            msg=f"Subject: It is Monday!!\n\n{random_quote}")


