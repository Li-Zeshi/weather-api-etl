from weather_fetcher import fetch_all
from cleaner import clean_weather_data

def main():
    raw = fetch_all()
    df = clean_weather_data(raw)
    df.to_csv('weather_data.csv', index=False)
    print("Weather data has been saved to weather_data.csv")

if __name__ == "__main__":
    main()
