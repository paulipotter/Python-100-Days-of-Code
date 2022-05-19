import requests
import os
from twilio.rest import Client
from datetime import date, timedelta


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_vantage_key = 'V4PSMGZ1Q77R5X27'
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'interval': '60min',
    'apikey': alpha_vantage_key,
    'outputsize': 'compact'
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()
print(data)

today = date.today()
yesterday = today - timedelta(days=1)
closing_yesterday = float(data['Time Series (Daily)'][str(yesterday)]['4. close'])

day_before_yesterday = today - timedelta(days=2)
closing_day_before_yesterday = float(data['Time Series (Daily)'][str(day_before_yesterday)]['4. close'])

difference = round(abs(closing_yesterday - closing_day_before_yesterday), 2)
print(difference)
percentage = round((difference / closing_yesterday)*100, 2)
print(percentage)

if percentage > 5:
    print('get news')



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



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

