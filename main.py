import requests

def get_weather(city):
    api_key = "0ff981148bc03fb4474e952c96822900"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + api_key + "&q=" + city
    
    def kelvin_to_celsius_fahrenheit(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit
    
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
    
        description = weather_data["weather"][0]["description"]
        temp = weather_data["main"]["temp"]
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp)
        feels_like = weather_data["main"]["feels_like"]
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like)
        humidity = weather_data["main"]["humidity"]
        
        print(f"Weather in {city.capitalize()}:")
        print(f"Description: {description}")
        print(f"Temperature: {temp_celsius:.2f} C°, {temp_fahrenheit:.2f} F°:")
        print(f"Feels like: {feels_like_celsius:.2f} C°, {feels_like_fahrenheit:.2f} F°")
        print(f"Humidity: {humidity}%")
        
    else:
        print("Failed to fetch weather information.")
        
def weather_forecast():
    print("Weather Forecast")
    city = input("Enter a city name: ")
    
    get_weather(city)
    
weather_forecast()