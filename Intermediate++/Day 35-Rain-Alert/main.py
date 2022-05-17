import requests
from twilio.rest import Client


account_sid = 'ACdac30f54c815432d902a0e3e73e21dd3'
auth_token = 'd3d911939aba1e64dd6f9f05e346001e'

API_KEY = "df232f945dd09f8403317f43c5f46d2a"
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
        from_='+16014016076',
        to='+17853172060'
    )
    print(message.status)


