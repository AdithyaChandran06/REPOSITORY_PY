import requests
import json

API_KEY = "9697cf1caf577323964e49e5b8dbc449"

def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def display_weather_info(weather_data):
    print("City:", weather_data["name"])
    print("Temperature:", weather_data["main"]["temp"], "°C")
    print("Humidity:", weather_data["main"]["humidity"], "%")
    print("Weather Conditions:", weather_data["weather"][0]["description"])

def main():
    city = input("Enter city name: ")
    weather_data = get_weather_data(city, API_KEY)
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()