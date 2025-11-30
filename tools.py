import requests

API_KEY = "3586fe176fef4c9da0c82929253011"
URL = "https://api.weatherapi.com/v1/current.json"

def parseResponse(response: requests.Response) -> str:
    try:
        res = response.json()
        city = res.get("location").get("name")
        current = res.get("current")
        temp = current.get("temp_c")
        condition = current.get("condition").get("text")
        wind = current.get("wind_kph")
        humidity = current.get("humidity")
        result = f"Current temperature in {city} is {temp}°C, {condition}, wind speed is {wind} km/h, humidity is {humidity}%."
    except (ValueError, AttributeError):
        raise ValueError("Invalid response")
    return result
    
def getWeather(city: str):
    if not city:
        raise ValueError("City name cannot be empty")
    parameters = f"key={API_KEY}&q={city}"
    try:
        response = requests.get(URL, parameters)
    except requests.RequestException as e:
        raise ValueError("Network error occurred") from e
    if response.status_code != 200:
        raise ValueError(response.json().get("error").get("message"))
    return parseResponse(response)

if __name__ == "__main__":
    print(getWeather("New York"))