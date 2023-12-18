import requests
from dotenv import load_dotenv
import os

load_dotenv()

lat=13.75
long=100.50
api_key = os.getenv('API_KEY')
city_name='bangkok'
print(api_key)


url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}"
url2=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

def get_weather(city_name, api_key):
    baseurl="https://api.openweathermap.org/data/2.5/weather?"
    additional="q="+city_name+"&appid="+api_key

    response = requests.get(baseurl+additional)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather = data['weather'][0]['description']
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature} Kelvin")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather}")
    else:
        print("Error in the HTTP request")


response = requests.get(url2)
print(response.json())
print(get_weather("bangkok",api_key))
# with open('response.json', 'a') as f:
#     f.write(response.text)


# Post Requests
# import requests

# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}

# x = requests.post(url, json = myobj)

# print(x.text)


## requests.post(url, data={key: value}, json={key: value}, args)
## requests.post(url, data = myobj, timeout=2.50)
