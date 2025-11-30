# open-ai

## HW 37. Weather API

### Module tools.py with function getWeather(city) returning string of weather containing the following

- City name
- Temperature
- Condition
- Humidity
- Wind speed

#### API of https://www.weatherapi.com/docs/ is used to get real time weather data

##### To run the module .env file with the following content is required:
```
WEATHER_API_KEY=your_api_key
WEATHER_URL=weather_api_url
```

#### Module weather_integration_test.py contains integration tests for getWeather function for any existing and not existing city

To run the tests create .env.test file in the root directory of the project with the following content:
```
WEATHER_API_KEY=your_api_key
WEATHER_URL=weather_api_url
```
