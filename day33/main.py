import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
EMAIL = "MYEMAIL"
PASSWORD = "123"

def is_iss_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LONG -5 <= iss_longitude <= MY_LONG +5:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_over_head() or is_night():
        with smtplib.SMTP("your_email_server.com") as connection:
            connection.starttls()
            connection.login(user="your_email@gmail.com", password="your_password")
            
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="subject: ISS IS OVER HEAD\n\n WAKE UP PRO AND WOTCH THE FUCKING ISS")
    



