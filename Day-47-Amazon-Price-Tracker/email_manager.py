import smtplib
MY_EMAIL = 'sender@email.com'
MY_PASSWORD = 'senderemailpassword'

class EmailManager:
    def __init__(self, list_of_prices):
        self.previous_price = list_of_prices[0]
        self.deal_price = list_of_prices[1]

    def send_message(self):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f'Subject:Deal for\n\nThis msg is sent using SMTP library of Python.\n{dt.datetime.now().date()}')
        connection.close()
