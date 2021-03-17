import os
from twilio.rest import Client
import smtplib
from keys_endpoints import TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER, TWILIO_MSG_TO, MY_EMAIL, PASSWORD


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_sms_to_me(self, message):
        account_sid = TWILIO_ACC_SID
        auth_token = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=message,
                from_=TWILIO_NUMBER,
                to=TWILIO_MSG_TO
        )

    def send_message_to_users(self, email, message):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=message
        )
        connection.close()
