from twilio.rest import Client  # Importing necessary module

# Twilio credentials (replace with your actual Twilio account details)
TWILIO_SID = 'YOUR TWILIO ACCOUNT SID'
TWILIO_AUTH_TOKEN = 'YOUR TWILIO AUTH TOKEN'
TWILIO_VIRTUAL_NUMBER = 'YOUR TWILIO VIRTUAL NUMBER'
TWILIO_VERIFIED_NUMBER = 'YOUR TWILIO VERIFIED NUMBER'

class NotificationManager:
    def __init__(self):
        # Initializing Twilio Client with provided credentials
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        # Sending an SMS using the Twilio client
        message = self.client.messages.create(
            body=message,  # Message content to be sent
            from_=TWILIO_VIRTUAL_NUMBER,  # Your Twilio virtual number
            to=TWILIO_VERIFIED_NUMBER,  # Your verified recipient number
        )
        # Printing the unique message SID if the message is successfully sent
        print(message.sid)
