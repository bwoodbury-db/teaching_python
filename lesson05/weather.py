"""
Assignment 
Print out the average temperature over the forecast
"""


import requests

r = requests.get(
    "https://api.open-meteo.com/v1/forecast?latitude=39.7392&longitude=-104.9847&hourly=temperature_2m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&past_days=7&forecast_days=1"
)

data = r.json()

print(data)
