import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = SECRET_ENV_G
PASSWORD = SECRET_ENV_P
TO_EMAIL = SECRET_ENV_ToG
MY_LAT = 60.143879
MY_LONG = 11.174980

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # ISS position +5 or -5 degrees from my degree
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
        #it's dark

while True:
    time.sleep(1)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject:Look Up☝️🛰️\n\nThe ISS (International Space Station) is above you in the sky 🛰️🚀🌍",
        )

