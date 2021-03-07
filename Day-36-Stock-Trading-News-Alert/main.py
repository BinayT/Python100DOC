import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


data_alphavantage = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA'
                                 f'&apikey={ALPHAVANTAGE_API_KEY}').json()
data_newsapi = requests.get(f'https://newsapi.org/v2/everything?q=tesla&apiKey={NEWSAPI_API}').json()

daily_data = data_alphavantage['Time Series (Daily)']
daily_data_list = list(daily_data.keys())
yesterday_close = float(daily_data[daily_data_list[0]]['4. close'])
before_yesterday_close = float(daily_data[daily_data_list[1]]['4. close'])
variation = yesterday_close - before_yesterday_close

def get_news():
    for data in data_newsapi['articles'][:3]:
        print(f"Title: {data['title']}\nDescription: {data['description']}\n")

get_news()

# if variation > 0:
#     if before_yesterday_close*0.02 < variation:
#         print("Positive. Get News")
# else:
#     if yesterday_close * 0.02 < -variation:
#         print("Negative. Get news")




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

