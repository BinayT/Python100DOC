# -*- coding: utf-8 -*-
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TEXT_TO_WRITE = ''

data_alphavantage = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA'
                                 f'&apikey={ALPHAVANTAGE_API_KEY}').json()
data_newsapi = requests.get(f'https://newsapi.org/v2/everything?q=tesla&apiKey={NEWSAPI_API}').json()

daily_data = data_alphavantage['Time Series (Daily)']
daily_data_list = list(daily_data.keys())
yesterday_close = float(daily_data[daily_data_list[0]]['4. close'])
before_yesterday_close = float(daily_data[daily_data_list[1]]['4. close'])
variation = yesterday_close - before_yesterday_close
yesterday_win_percentage = round((variation/before_yesterday_close) * 100, 2)
before_yesterday_win_percentage = round((-variation/before_yesterday_close) * 100, 2)


def get_news(boolean):
    global TEXT_TO_WRITE
    if boolean:
        TEXT_TO_WRITE += f"Tesla went UP {yesterday_win_percentage}%!!!. Here are some hottest news.\n"
    else:
        TEXT_TO_WRITE += f"Tesla's went DOWN {before_yesterday_win_percentage}%. Here are some news.\n"

    for data in data_newsapi['articles'][:3]:
        TEXT_TO_WRITE += f"Headline: {data['title']}\nBrief: {data['description']}\n"


if variation > 0:
    get_news(True)
else:
    get_news(False)



client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
client.messages \
        .create(
            body=TEXT_TO_WRITE,
            from_=MY_FAKE_NUM,
            to=MY_REAL_NUM
        )