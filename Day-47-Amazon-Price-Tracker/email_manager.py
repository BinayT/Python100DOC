import smtplib
MY_EMAIL = ''
MY_PASSWORD = ''
TO_EMAIL = ''


class EmailManager:
    def __init__(self, product_details):
        self.previous_price = product_details[0]
        self.deal_price = product_details[1]
        self.product_name = product_details[2].encode('utf-8')

    def send_message(self):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f'Subject:Deal for {self.product_name}\n\nThere is a great deal today for the mentioned product that '
                f'you wanted to buy.\nPrevious Price: {self.previous_price}EURO ---> Current Price: {self.deal_price}EURO')
        connection.close()
