while True:
    
    def banner():
        """ This is a attrartive banner for 
        our app, which has been made from ASCII code."""
        
        print(
        """
        
    ██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗      █████╗ ██████╗ ██████╗ 
    ██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗
    ██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝    ███████║██████╔╝██████╔╝
    ██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗    ██╔══██║██╔═══╝ ██╔═══╝ 
    ╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║    ██║  ██║██║     ██║     
     ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝     
                                                                                        
        """)

    banner() #calling the banner for function first so that the app looks attractive


    import requests     # importing necessary libraries
    import mysql.connector as sq
    
    # making connection with mysql
    con=sq.connect(host="localhost",user="root",passwd="kgp",database="weather",charset='utf8',buffered=True)
    cur=con.cursor()
    
    city=input("Enter the City: ")      # taking the city name as input from user
    url='https://api.openweathermap.org/data/2.5/weather?appid=20689b2be145969d78f3bf4ab0a9ff58&q={}&units=metric'.format(city)

    # the upper url is the main url which we get from the api provider and it also have a unique api key

    res=requests.get(url)      # we will fetch our data by making a HTTP request to our api
    data=res.json()            # now we will convert our raw data into json file

    def temperature():
        """ This function will tell us the temperature"""
        temp=data['main']['temp']
     
        inserting="insert into weathert(city,temperature)values('{}',{})".format(city,temp)
        cur.execute(inserting)
        con.commit()
        print(city)
        print('The temperature of {} is'.format(city),temp,'degree celcius')

    def wind_speed():
        """ This function will tell the wind speed"""
        wind_speed=data['wind']['speed']
        inserting="insert into weathert(city,wind_speed)values('{}',{})".format(city,wind_speed)
        cur.execute(inserting)
        con.commit()
        print('The wind speed of {} is '.format(city),wind_speed,'m/s')

    def latitude():
        """ This function will tell the latitude"""
        latitude=data['coord']['lat']
        inserting="insert into weathert(city,latitude)values('{}',{})".format(city,latitude)
        cur.execute(inserting)
        con.commit()
        print('The latitude of {} is'.format(city),latitude,'degree')

    def longitude():
        """ This function will tell the longitude"""
        longitude=data['coord']['lon']
        inserting="insert into weathert(city,longitude)values('{}',{})".format(city,longitude)
        cur.execute(inserting)
        con.commit()
        print('The longitude of {} is'.format(city),longitude,'degree')
        
    def description():
        """ This function will tell some description of the requested city"""
        description=data['weather'][0]['description']
        inserting="insert into weathert(city,description)values('{}','{}')".format(city,description)
        cur.execute(inserting)
        con.commit()
        print(description)

    def humidity():
        """ This function will tell the humidity level"""
        humidity=data['main']['humidity']
        inserting="insert into weathert(city,humidity)values('{}',{})".format(city,humidity)
        cur.execute(inserting)
        con.commit()
        print('The humidity of {} is'.format(city),humidity,'%')

    def country():
        """ This function will tell the country of requested country """
        country=data['sys']['country']
        inserting="insert into weathert(city,country)values('{}','{}')".format(city,country)
        cur.execute(inserting)
        con.commit()
        print(country)



    def statements(): # this are the print statements which will we our menu
        print("Make Choice: ")
        print()
        print('1.Temperature: ')
        print('2.Wind Speed: ')
        print('3.Latitude: ')
        print('4.Longitude: ')
        print('5.Description: ')
        print('6.Humidity: ')
        print('7.Country: ')
        print('8.All: ')



    def main_menu():
        """ This function comprises of if/elif statement for our menu"""
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
        elif choices== '8':
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
    choices=input("Enter the choice: ")             #taking choice for our menu as input from User
    print()                                     
    main_menu()                                     
                                    
    """ Code by Shubham Sharma """                            


                                                                      
                                               
    
