# importing modules

import requests

api_address='https://api.openweathermap.org/data/2.5/weather?appid=b6907d289e10d714a6e88b30761fae22&='
city=input("Enter the City") # taking input from user
api_url=api_address+city
json_data=requests.get(url).json
formatted_data=json_data['weather'][0]['main']
print(formatted_data)
