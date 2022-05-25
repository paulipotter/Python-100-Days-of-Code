import smtplib
from twilio.rest import Client

TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_VIRTUAL_NUMBER = ''
TWILIO_VERIFIED_NUMBER = ''
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = ''
MY_PASSWORD = ''
MESSAGE = 'The item you requested a notification on is now at $PRICE.'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_email(self, item_price, link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            NEW_MESSAGE = MESSAGE.replace('PRICE', item_price)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:New Low Price Alert!\n\n{NEW_MESSAGE}\n{link}".encode('utf-8')
            )