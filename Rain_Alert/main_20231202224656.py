# Rain Alert

''' The code fetches weather data using OpenWeatherMap API for a specific location and sends an SMS 
notification via Twilio if rain is expected within the next 4 hours. '''

import requests
from twilio.rest import Client

# OpenWeatherMap API endpoint and necessary parameters
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "__YOUR_OWM_API_KEY__"
account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"

weather_params = {
    "lat": 46.947975,  # Latitude
    "lon": 7.447447,   # Longitude
    "appid": api_key,
    "cnt": 4,  # Fetching weather data for the next 4 hours
}

# Fetching weather data from OpenWeatherMap API
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Checking if it will rain within the next 4 hours based on weather condition codes
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:  # Codes below 700 indicate rainy conditions
        will_rain = True

# Sending SMS notification via Twilio if rain is expected
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)  # Printing the status of the sent message
