# Stock News

''' The code checks for significant changes in stock prices, retrieve news articles related to the specified
company's stocks, and sends the user an message. '''

'''
Values to change in code
  1) "your virtual twilio number" in line 18 with your virtual Twilio number
  2) "your own phone number verified with Twilio" in line 19 with your verified phone number
  3) "YOUR TWILIO ACCOUNT SID" in line 20 with your Twilio account SID
  4) "YOUR TWILIO AUTH TOKEN" in line 21 with your auth token
'''

import requests
from twilio.rest import Client

# Your Twilio numbers and API credentials
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

# Constants for the stock and news data
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"

# Obtain stock data from Alpha Vantage
# Fetch yesterday's and day before yesterday's closing stock prices
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Calculate price difference and percentage change
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

# Fetch news articles if there's a significant price change
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Get the first 3 articles related to the company
    three_articles = articles[:3]

    # Send formatted articles via Twilio
    # Prepare article headlines and descriptions in a formatted manner
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]

    # Send each article as a separate message via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
