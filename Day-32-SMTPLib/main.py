# import smtplib
# import datetime as dt
#
# my_email = 'mail@gmail.com'
# password = 'thepassword'
#
# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs='thereciever@gmail.com',
#     msg=f'Subject:Trying SMTP\n\nThis msg is sent using SMTP library of Python.\n{dt.datetime.now().date()}')
# connection.close()

import datetime as dt
currentdatetime = dt.datetime.now()
date = currentdatetime.date()
time = currentdatetime.time()
print(f'{date}, {time}')