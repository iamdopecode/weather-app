# importing modules

import requests

def by_city():
    city=input("Enter the City: ")
    url='https://api.openweathermap.org/data/2.5/weather?appid=20689b2be145969d78f3bf4ab0a9ff58&q={}&units=metric'.format(city)
    res=requests.get(url)
    data=res.json()
    show_data(data)

def by_location():
    res=requests.get('https://ipinfo.io') 
    data=res.json()
    show_data(data)

def show_data(data):

    temp=data['main']['temp']
    wind_speed=data['wind']['speed']
    description=data['weather'][0]['description']
    print("The Temperature is: {} degree celcius".format(temp))
    print("The Wind Speed is: {} m/s".format(wind_speed))
    print("The Description is: {}".format(description))

def main_menu():
    print('1. Get Data by city')
    print('2. Get Data by current location')
    choice=input("Enter your choice: ")

    if choice=='1':
        by_city()
    else:
        by_location()

main_menu()

        
    

