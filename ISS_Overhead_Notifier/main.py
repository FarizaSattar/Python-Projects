# ISS Overhead Notifier

''' The script continuously checks if the International Space Station (ISS) is overhead and if it's nighttime 
at a specified latitude and longitude, sending an email notification when both conditions are met, requiring 
email, location, and SMTP server setup. '''

# ISS Overhead Notifier

import requests  # Importing the requests library for making HTTP requests
from datetime import datetime  # Importing datetime for handling date and time
import smtplib  # Importing smtplib for sending emails
import time  # Importing time for time-related functions

# Enter your email and password for sending notifications
MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"

# Set your latitude and longitude coordinates
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def is_iss_overhead():
    """
    Checks if the ISS (International Space Station) is overhead your location within +5 or -5 degrees.
    Makes a request to the ISS location API and compares the coordinates.
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raises an exception for unsuccessful HTTP requests
    data = response.json()  # Extracts JSON data from the response

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    """
    Checks if it is nighttime at your location using sunrise-sunset API.
    Compares the current hour with sunrise and sunset times obtained from the API response.
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Raises an exception for unsuccessful HTTP requests
    data = response.json()  # Extracts JSON data from the response

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # Checks if the current hour is after sunset or before sunrise
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)  # Pauses the program execution for 60 seconds
    if is_iss_overhead() and is_night():
        # Connects to the SMTP server, logs in with provided credentials, and sends an email notification
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
