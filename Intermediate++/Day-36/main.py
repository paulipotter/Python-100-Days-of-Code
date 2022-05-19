import requests
import os
from twilio.rest import Client
from datetime import date, timedelta
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK = "MSFT"
COMPANY_NAME = "Microsoft"
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

def get_stock_closing_difference():
    alpha_vantage_key = 'V4PSMGZ1Q77R5X27'
    stock_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'interval': '60min',
        'apikey': alpha_vantage_key,
        'outputsize': 'compact',
    }

    #  retrieve stock info
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    data = response.json()
    print(data)

    today = date.today()  # get today's date

    yesterday = today - timedelta(days=1)  # get yesterday's date
    closing_yesterday = float(data['Time Series (Daily)'][str(yesterday)]['4. close'])  # get yesterday's closing price

    day_before_yesterday = today - timedelta(days=2)
    closing_day_before_yesterday = float(data['Time Series (Daily)'][str(day_before_yesterday)]['4. close'])

    # get the absolute value difference of the closing price of both days
    difference = round(abs(closing_yesterday - closing_day_before_yesterday), 2)

    percentage = round((difference / closing_yesterday)*100, 2)  # calculate the percentage of such difference
    return percentage


def get_news_articles():
    news_key = 'f22ecbcb1a77458aab97a1654f08487e'
    news_params = {
        'apiKey': news_key,
        'q': 'Microsoft',
        'language': 'en',
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    data = response.json()
    return data['articles'][:3]


if get_stock_closing_difference > 5:
    news = get_news_articles()

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain today. Don't forget to use an umbrella ☔️",
        from_='+16014016076',
        to='+17853172060'
    )
    print(message.status)
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

