from utils.api_helpers import get_weather

class WeatherAgent:
    def __init__(self):
        pass
        
    def process(self, input_data):
        """Get weather data for the launch location"""
        try:
            if not input_data or "launch_location" not in input_data:
                raise ValueError("Missing launch location data")
            
            location = input_data["launch_location"]
            
            # Extract latitude and longitude
            lat = location.get("latitude")
            lon = location.get("longitude")
            
            if not lat or not lon:
                raise ValueError("Missing latitude or longitude in launch location")
            
            # Get weather data
            weather_data = get_weather(lat, lon)
            
            # Extract relevant weather information
            weather_info = {
                "temperature": weather_data.get("main", {}).get("temp"),
                "conditions": weather_data.get("weather", [{}])[0].get("main"),
                "description": weather_data.get("weather", [{}])[0].get("description"),
                "wind_speed": weather_data.get("wind", {}).get("speed"),
                "humidity": weather_data.get("main", {}).get("humidity"),
                "visibility": weather_data.get("visibility"),
                "precipitation": weather_data.get("rain", {}).get("1h", 0)
            }
            
            # Combine with input data
            result = input_data.copy()
            result["weather"] = weather_info
            
            return result
            
        except Exception as e:
            print(f"Error in Weather Agent: {e}")
            # Add default weather data in case of error
            result = input_data.copy() if input_data else {}
            result["weather"] = {
                "temperature": None,
                "conditions": "Unknown",
                "description": "Weather data unavailable",
                "wind_speed": None,
                "humidity": None,
                "visibility": None,
                "precipitation": None
            }
            return result