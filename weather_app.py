# importing modules

import requests


city=input("Enter the City: ")

url='https://api.openweathermap.org/data/2.5/weather?appid=20689b2be145969d78f3bf4ab0a9ff58&q={}&units=metric'.format(city)



res=requests.get(url)

data=res.json()

temp=data['main']['temp']

wind_speed=data['wind']['speed']

description=data['weather'][0]['description']
print("The Temperature is: {} degree celcius".format(temp))
print("The Wind Speed is: {} m/s".format(wind_speed))
print("The Description is: {}".format(description))

