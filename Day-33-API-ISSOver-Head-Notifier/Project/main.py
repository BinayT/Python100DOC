import requests
from datetime import datetime
import smtplib

MY_LAT = 0.000000
MY_LONG = 0.000000

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

hour_now = datetime.now().hour


if MY_LAT-5 < iss_latitude < MY_LAT + 5 and MY_LONG-5 < iss_longitude < MY_LONG + 5 \
        and sunset < hour_now or hour_now > sunrise:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='my@email.com', password='mypassword')
        connection.sendmail(
            from_addr='my@email.com',
            to_addrs='recieveremail@gmail.com',
            msg=f"Subject:Watch Up Over the Sky\n\nThe ISS is crossing over your home. Watch up ;)")



