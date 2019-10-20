def banner():
    print(
    """
    
██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗      █████╗ ██████╗ ██████╗ 
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗
██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝    ███████║██████╔╝██████╔╝
██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗    ██╔══██║██╔═══╝ ██╔═══╝ 
╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║    ██║  ██║██║     ██║     
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝     
                                                                                       
    """)

banner()


import requests
city=input("Enter the City: ")
url='https://api.openweathermap.org/data/2.5/weather?appid=20689b2be145969d78f3bf4ab0a9ff58&q={}&units=metric'.format(city)

res=requests.get(url)
data=res.json()

def temperature():
    temp=data['main']['temp']
    print('The temperature of {} is'.format(city),temp,'degree celcius')

def wind_speed():
    wind_speed=data['wind']['speed']
    print('The wind speed of {} is '.format(city),wind_speed,'m/s')

def latitude():
    latitude=data['coord']['lat']
    print('The latitude of {} is'.format(city),latitude,'degree')

def longitude():
    longitude=data['coord']['lon']
    print('The longitude of {} is'.format(city),longitude,'degree')
    
def description():
    description=data['weather'][0]['description']
    print(description)

def humidity():
    humidity=data['main']['humidity']
    print('The humidity of {} is'.format(city),humidity,'%')

def country():
    country=data['sys']['country']
    print(country)



def statements():
    print("Make Choice: ")
    print()
    print('1.Temperature: ')
    print('2.Wind Speed: ')
    print('3.Latitude: ')
    print('4.Longitude: ')
    print('5.Description: ')
    print('6.Humidity: ')
    print('7.Country: ')
    print('8.All')




def main_menu():
    if choices=='1':
        temperature()
    elif choices=='2':
        wind_speed()
    elif choices=='3':
        latitude()
    elif choices=='4':
        longitude()
    elif choices=='5':
        description()
    elif choices=='6':
        humidity()
    elif choices=='7':
        country()
    elif choices=='8':
        temperature()
        wind_speed()
        latitude()
        longitude()
        description()
        humidity()
        country()        

       
print()
statements()
print()
choices=input("Enter the choice: ")
print()
main_menu()



                                                                      
                                               
    