import requests
import os
from twilio.rest import Client


account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

API_KEY = os.environ.get("OWM_API_KEY")
OMW_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'

weather_params = {
    "appid": API_KEY,
    "lat": 6.244203,
    "lon": -75.581215,
    "exclude": 'current,alerts,daily,minutely'
}

response = requests.get(OMW_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()

hourly_weather = data['hourly'][:12]
weather_data = []
rain = False
for hour in hourly_weather:
    weather_id = hour['weather'][0]['id']
    if int(weather_id) < 700:
        rain = True

print("It is raining" if rain == True else "It is not raining")
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain today. Don't forget to use an umbrella ☔️",
        from_='',
        to=''
    )
    print(message.status)


