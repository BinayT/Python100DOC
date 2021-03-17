import os
from twilio.rest import Client
from keys_endpoints import TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER, TWILIO_MSG_TO


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self, message):
        account_sid = TWILIO_ACC_SID
        auth_token = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=message,
                from_=TWILIO_NUMBER,
                to=TWILIO_MSG_TO
        )