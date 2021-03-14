import smtplib
MY_EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, cheap_flights_list):
        self.cheap_flights_list = cheap_flights_list

    def send_msg(self):
        msg_to_send = ''
        for deals in self.cheap_flights_list:
            msg_to_send += f'{deals}\n'

        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='email@gmail.com',
            msg=f'Subject:Cheap Deals Awaiting\n\n'
                f'Here are the lists of cheap deals found for the cities.\n'
                f'{msg_to_send}')
        connection.close()

