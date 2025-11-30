from unittest import TestCase
from tools import getWeather

class TestWeatherIntegration(TestCase):
    def test_get_weather_valid_city(self):
        temp = getWeather("London")
        self.assertIsInstance(temp, (str))

    def test_get_weather_invalid_city(self):
        with self.assertRaises(ValueError) as sm:
            getWeather("InvalidCityName12345")
        self.assertIn("No matching location found", str(sm.exception))
        with self.assertRaises(ValueError) as sm:
            getWeather("")
        self.assertIn("City name cannot be empty", str(sm.exception))

