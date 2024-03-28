import requests
from twilio.rest import Client
from credentials import *

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "outputsize": "compact",
    "datatype" : "json",
    "apikey" : STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
stock_data = [value for (key, value) in stock_data.items()]
yesterday = stock_data[-1]
yesterday_cp = float(yesterday["4. close"])

day_before_yesterday = stock_data[-2]
day_before_yesterday_cp = float(day_before_yesterday["4. close"])

difference = abs(yesterday_cp-day_before_yesterday_cp)
difference_per = difference/yesterday_cp*100
if(difference_per>5):
    news_parameters = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()["articles"][:3]
    articles = [f"Headline: {article['title']}, \n Brief: {article['description']}" for article in news]
    client = Client(TWILIO_SID, AUTH_TOKEN)
    for article in articles:
        if (yesterday_cp-day_before_yesterday_cp)>0:
            message = client.messages.create(
                body=f"{STOCK_NAME}: 🔺{difference_per}% \n {article}",
                from_="+15643330285",
                to="+919511179673"
            )
        else:
            message = client.messages.create(
                body=f"{STOCK_NAME}: 🔻{difference_per}% \n {article}",
                from_="+15643330285",
                to="+919511179673"
            )

