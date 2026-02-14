import requests  # Library to make HTTP requests to APIs

API_KEY = "Insert API Key"  # Your unique key to authenticate with OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"  # The endpoint we're hitting




print("WEATHER FORECAST")
print("---------------")

city = input("Enter city name: ")

city = city.capitalize()

params = {
    "q": city,  # The city we want the weather for
    "appid": API_KEY,  # Our API key for authentication
    "units": "metric"  # Get temperature in Celsius( use "imperial" for Fahrenheit)

}

response = requests.get(BASE_URL, params=params)  # Make the API request with the specified parameters


#print(f"Status code: {response.status_code}")  # See what error code we got


if response.status_code == 200:  # Check if the request was successful
    data = response.json()  # Parse the JSON response from the API
    
    
    #print(data)
    
    print(f"Weather in {data["name"]},", end = "")
    print(f" Country: {data["sys"]["country"]}:")
    print(f"Temperature: {data["main"]["temp"]}°C")
    print(f"weather: {data["weather"][0]["description"]}")
else:
    print("Error fetching weather data. Please check the city name and try again.") 