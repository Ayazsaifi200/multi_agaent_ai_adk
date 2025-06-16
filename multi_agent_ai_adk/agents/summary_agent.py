import google.generativeai as genai
import os
from utils.env_helpers import load_env_safely
load_env_safely()

# Configure Google API
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

class SummaryAgent:
    def __init__(self):
        # Initialize the generative model
       self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def process(self, input_data):
        """Create a summary based on the input data"""
        try:
            if not input_data:
                raise ValueError("No input data provided")
            
            # Check if we have SpaceX launch data
            has_launch_data = "mission_name" in input_data and "launch_date" in input_data
            
            # Check if we have weather data
            has_weather_data = "weather" in input_data and isinstance(input_data["weather"], dict)
            
            # Generate appropriate prompt based on available data
            if has_launch_data and has_weather_data:
                summary = self._generate_launch_weather_summary(input_data)
            elif has_launch_data:
                summary = self._generate_launch_summary(input_data)
            else:
                summary = "Insufficient data to generate a meaningful summary."
            
            # Combine with input data
            result = input_data.copy()
            result["summary"] = summary
            
            return result
            
        except Exception as e:
            print(f"Error in Summary Agent: {e}")
            result = input_data.copy() if input_data else {}
            result["summary"] = "Could not generate summary due to an error."
            return result
    
    def _generate_launch_weather_summary(self, data):
        """Generate a summary about the launch and weather conditions"""
        try:
            # Extract relevant data
            mission = data.get("mission_name", "Unknown")
            date = data.get("launch_date", "Unknown")
            location = data.get("launch_location", {}).get("name", "Unknown location")
            weather_cond = data.get("weather", {}).get("conditions", "Unknown")
            weather_desc = data.get("weather", {}).get("description", "Unknown")
            temp = data.get("weather", {}).get("temperature")
            wind = data.get("weather", {}).get("wind_speed")
            precip = data.get("weather", {}).get("precipitation")
            
            # Format temperature if available
            temp_str = f"{temp}°C" if temp is not None else "unknown temperature"
            
            # Format wind if available
            wind_str = f"{wind} m/s" if wind is not None else "unknown wind speed"
            
            # Create prompt for analysis
            prompt = f"""
            Analyze the following SpaceX launch and weather data:
            
            Mission: {mission}
            Launch Date: {date}
            Location: {location}
            Weather: {weather_cond} ({weather_desc})
            Temperature: {temp_str}
            Wind: {wind_str}
            Precipitation: {precip if precip is not None else "unknown"}
            
            Create a concise summary of the launch and whether the weather conditions might cause a delay.
            Focus on analyzing if the mission is likely to proceed based on the weather.
            """
            
            response = self.model.generate_content(prompt)
            return response.text.strip()
            
        except Exception as e:
            print(f"Error generating launch/weather summary: {e}")
            return self._generate_fallback_summary(data)
    
    def _generate_launch_summary(self, data):
        """Generate a summary about just the launch"""
        try:
            # Extract relevant data
            mission = data.get("mission_name", "Unknown")
            date = data.get("launch_date", "Unknown")
            location = data.get("launch_location", {}).get("name", "Unknown location")
            details = data.get("details", "No details available")
            
            # Create prompt
            prompt = f"""
            Summarize the following SpaceX launch information:
            
            Mission: {mission}
            Launch Date: {date}
            Location: {location}
            Details: {details}
            
            Create a concise summary about this upcoming launch.
            """
            
            response = self.model.generate_content(prompt)
            return response.text.strip()
            
        except Exception as e:
            print(f"Error generating launch summary: {e}")
            return self._generate_fallback_summary(data)
    
    def _generate_fallback_summary(self, data):
        """Generate a simple fallback summary when AI generation fails"""
        mission = data.get("mission_name", "Unknown mission")
        date = data.get("launch_date", "unknown date")
        location = data.get("launch_location", {}).get("name", "unknown location")
        
        if "weather" in data and isinstance(data["weather"], dict):
            weather_desc = data["weather"].get("description", "unknown weather conditions")
            return f"The SpaceX mission '{mission}' is scheduled for {date} at {location}. Weather conditions: {weather_desc}."
        else:
            return f"The SpaceX mission '{mission}' is scheduled for {date} at {location}."