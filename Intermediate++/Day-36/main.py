import requests
from twilio.rest import Client
from datetime import date, timedelta

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK = "MSFT"
COMPANY_NAME = "Microsoft"
account_sid = 'ACdac30f54c815432d902a0e3e73e21dd3'
auth_token = 'd8e22b84f5b0871822572e5330f401b1'


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
    diff = round(closing_yesterday - closing_day_before_yesterday, 2)

    percentage = round((diff / closing_yesterday) * 100, 1)  # calculate the percentage of such difference
    return percentage


def get_news_articles():
    news_key = 'f22ecbcb1a77458aab97a1654f08487e'
    news_params = {
        'apiKey': news_key,
        'qInTitle': 'Microsoft',
        'language': 'en',
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    data = response.json()['articles']
    return data[:3]


difference = get_stock_closing_difference()
up_down = None
if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"
if abs(difference) > 5:
    news = get_news_articles()
    formatted_article = [
        f"{STOCK}: {up_down} {difference}% \nHeadline: {article['title']}\bBrief: {article['description']}"
        for article in news]

    client = Client(account_sid, auth_token)
    for item in formatted_article:
        message = client.messages \
            .create(
            body=item,
            from_='+16014016076',
            to='+17853172060'
        )
        print(message.status)
