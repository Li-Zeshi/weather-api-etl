import pandas as pd

def clean_weather_data(raw_data_list):
    records = []
    for data in raw_data_list:
        if data is None:
            continue
        record = {
            'city': data['name'],
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'weather': data['weather'][0]['description'],
            'time': pd.to_datetime(data['dt'], unit='s')
        }
        records.append(record)
    return pd.DataFrame(records)
