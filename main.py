import requests 
from pprint import pprint 

API_Key = '1099890aea4ca9e0f32ffac9f76b6747' 

city = input("Enter a city: ") 

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q=" +city 

weather_data = requests.get(base_url).json() 

pprint(weather_data)
