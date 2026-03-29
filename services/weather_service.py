import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(city="Pune"):

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url).json()

        return {
            "temp": res["main"]["temp"],
            "humidity": res["main"]["humidity"],
            "weather": res["weather"][0]["description"]
        }

    except:
        return {
            "temp": 30,
            "humidity": 60,
            "weather": "clear"
        }