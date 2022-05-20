##################### Extra Hard Starting Project ######################
from datetime import datetime
import pandas as pd
from random import randint
from smtplib import SMTP
import os

PLACEHOLDER = '[NAME]'
letters = []

now = datetime.now()
today = (now.month, now.day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
birthdays = data.to_dict(orient='records')


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    print(f"it's {birthday_person['name']}'s birthday!")

    with open(file_path) as letter_file:
        letter = letter_file.read()

    name = birthday_person['name'].strip().title()
    new_letter = letter.replace(PLACEHOLDER, name)

    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=os.environ.get('TEST_SENDER_ADDR'), password=os.environ.get('TEST_SENDER_PW'))
        connection.sendmail(from_addr=os.environ.get('TEST_SENDER_ADDR'),
                            to_addrs=os.environ.get('RECIPIENT_PHONE_NUMBER'),
                            msg=f"Subject: It is your birthday!!\n\n{new_letter}")





