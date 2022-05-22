from twilio.rest import Client

TWILIO_SID = 'secret'
TWILIO_AUTH_TOKEN = 'secret'
TWILIO_VIRTUAL_NUMBER = 'secret'
TWILIO_VERIFIED_NUMBER = 'secret'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
