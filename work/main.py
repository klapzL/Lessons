import requests as rq
import json
from dotenv import load_dotenv
import os

city = input()
load_dotenv()
key = os.environ.get('OPENWEATHER_API_KEY')
print(key)
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric&lang=ru'

respone = rq.get(url)
dict_response = json.loads(respone.text)
print(dict_response)
weather = dict_response.get('main')
print(weather)

