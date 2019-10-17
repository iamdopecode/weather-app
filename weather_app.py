# importing modules

import requests
from pprint import pprint

city=input("Enter the City: ")

url='https://api.openweathermap.org/data/2.5/weather?appid=20689b2be145969d78f3bf4ab0a9ff58&q={}&units=metric'.format(city)



res=requests.get(url)

data=res.json()

pprint(data)

