import os
import requests
from utils.env_helpers import load_env_safely

# Load environment variables
load_env_safely()

def get_spacex_next_launch():
    """Get the next SpaceX launch data"""
    url = os.getenv('SPACEX_API')
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch SpaceX data: {response.status_code}")

def get_weather(lat, lon):
    """Get weather data for a specific location"""
    url = os.getenv('WEATHER_API')
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch weather data: {response.status_code}")
