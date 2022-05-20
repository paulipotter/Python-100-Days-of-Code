import requests
from datetime import datetime
from smtplib import SMTP
import time, os

MY_LAT = 32.715736  # Your latitude
MY_LONG = -117.161087  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # If it's nighttime, return true
    if sunset <= time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
    if is_iss_overhead() and is_night():
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=os.environ.get('TEST_SENDER_ADDR'), password=os.environ.get('TEST_RECIPIENT_ADDR'))
            connection.sendmail(from_addr=os.environ.get('TEST_SENDER_ADDR'),
                                to_addrs=os.environ.get('TEST_RECIPIENT_ADDR'),
                                msg=f"Subject: Look up!\n\nISS is above you <3")
