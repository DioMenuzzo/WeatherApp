import requests


API_KEY = "0ff981148bc03fb4474e952c96822900"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


def kelvin_to_celsius_fahrenheit(kelvin: float) -> tuple[float, float]:
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


def fetch_data_from_api(city: str) -> dict:
    url = f'{BASE_URL}appid={API_KEY}&q={city}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as err:
        print("Failed to fetch weather information.")
    return {}


def print_weather_info(city: str) -> None:
    weather_data = fetch_data_from_api(city)

    if not weather_data:
        return

    description = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp)
    feels_like = weather_data["main"]["feels_like"]
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(
        feels_like)
    humidity = weather_data["main"]["humidity"]

    print(f"Weather in {city.capitalize()}:")
    print(f"Description: {description}")
    print(f"Temperature: {temp_celsius:.2f} C째, {temp_fahrenheit:.2f} F째:")
    print(
        f"Feels like: {feels_like_celsius:.2f} C째, {feels_like_fahrenheit:.2f} F째")
    print(f"Humidity: {humidity}%")


if __name__ == '__main__':
    print("Weather Forecast")
    city = input("Enter a city name: ")
    print_weather_info(city)
