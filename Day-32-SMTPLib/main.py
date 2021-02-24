import smtplib
import datetime as dt
from random import choice
#
my_email = 'sender@email.com'
password = 'senderemailpassword'
#
# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs='thereciever@gmail.com',
#     msg=f'Subject:Trying SMTP\n\nThis msg is sent using SMTP library of Python.\n{dt.datetime.now().date()}')
# connection.close()

# import datetime as dt
# currentdatetime = dt.datetime.now()
# date = currentdatetime.date()
# time = currentdatetime.time()
# randomdate = dt.datetime(year=1994, month=5, day=25, hour=19, minute=15)
# print(randomdate)
# print(f'{date}, {time}')

with open('quotes.txt', mode="r") as quotes_file:
    content = quotes_file.readlines()
    content_list = []
    for quote in content:
        content_list.append(quote[:-1])

currentdatetime = dt.datetime.now()
day = currentdatetime.weekday()
if day == 2:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='recieveremail@gmail.com',
            msg=f"Subject:Motivational Wednesday\n\n{choice(content_list)}")