import smtplib
from data import my_email, password


class SendEmail:
    def send_email(self, data):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f'Subject:User Contacted From Blog Site\n\n'
                f'Name : {data["name"]}\n\nEmail Address : {data["email"]}\n\nPhone Number : {data["phone"]}\n\n'
                f'Message : {data["message"]}\n')
        connection.close()