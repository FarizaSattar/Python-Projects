# Rain Alert
''' The code sends the user an SMS notification via Twilio if rain is expected within the next 4 hours. '''

import requests
from twilio.rest import Client

# OpenWeatherMap API endpoint and necessary parameters
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "__YOUR_OWM_API_KEY__"
account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"

weather_params = {
    # Latitude
    "lat": 46.947975,  
    # Longitude
    "lon": 7.447447,   
    "appid": api_key,
    # Fetching weather data for the next 4 hours
    "cnt": 4,  
}

# Fetching weather data from OpenWeatherMap API
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Checking if it will rain within the next 4 hours based on weather condition codes
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    # Codes below 700 indicate rainy conditions
    if int(condition_code) < 700:  
        will_rain = True

# Sending SMS notification via Twilio if rain is expected
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )

    # Printing the status of the sent message
    print(message.status)  
