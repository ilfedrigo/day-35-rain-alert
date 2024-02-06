import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "3506b40349a43cf2afb227acd20f97bf"

account_sid = "AC64da4cae31faf49ea3ba67162030c024"
auth_token = "c60503936afa5a365ff5ef22365cf3cd"

weather_params = {
    "lat": -15.826691,
    "lon": -47.921822,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_endpoint, params=weather_params,)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for item in weather_data["list"]:
    weather_forecast = item["weather"][0]["id"]
    if int(weather_forecast) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="☔️",
                     from_='+16592700962',
                     to='Trusted Phone Number'
                 )

    print(message.status)