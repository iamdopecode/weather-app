# importing modules

import requests

api_address='https://api.openweathermap.org/data/2.5/weather?appid=20689b2be145969d78f3bf4ab0a9ff58&='
city=input("Enter the City") # taking input from user
api_url=api_address+city
json_data=requests.get(formatted_url).json
formatted_data=json_data['weather'][0]['main']
print(formatted_data)
