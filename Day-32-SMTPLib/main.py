import smtplib

my_email = 'mail@gmail.com'
password = 'thepassword'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs='thereciever@gmail.com',
    msg='Subject:Trying SMTP\n\nThis msg is sent using SMTP library of Python.')
connection.close()