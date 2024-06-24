import requests,json,datetime
from datetime import datetime

api_key = 'API_KEY'
location = input("City name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) -273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("Weather Stats for -{} || {}".format(location.upper(), datetime))

temp = print("Temperature: {:.2f} deg C".format(temp_city))
weather= print("Weather desc: ",weather_desc)
humid=print("Humidity: ",hmdt, '%')
wind_speed=print("Wind Speed: ",wind_spd ,'kmph') 
