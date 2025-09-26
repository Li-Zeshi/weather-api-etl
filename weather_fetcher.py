import requests
import config

def fetch_weather(city):
    params = {
        'q': city,
        'appid': config.API_KEY,
        'units': config.UNIT
    }
    response = requests.get(config.BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch weather for {city}. Status code: {response.status_code}")
        return None

def fetch_all():
    return [fetch_weather(city) for city in config.CITIES]
