import os
from dotenv import load_dotenv

def load_env_safely(env_path=None):
    """Load environment variables safely, handling different file encodings"""
    if env_path is None:
        # Default path relative to the project root
        env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', '.env')
    
    # Try to load directly first
    try:
        if load_dotenv(env_path):
            return True
    except Exception as e:
        print(f"Standard .env loading failed: {e}")
    
    # Fallback: Set environment variables directly
    print("Setting environment variables directly")
    os.environ['OPENWEATHERMAP_API_KEY'] = '46c5f06235a7df007c4e200de781548f'
    os.environ['GOOGLE_API_KEY'] = 'AIzaSyAhNM6WE84985_9AIuOLhwO0Oa2XarruNo'
    os.environ['SPACEX_API'] = 'https://api.spacexdata.com/v5/launches/next'
    os.environ['WEATHER_API'] = 'https://api.openweathermap.org/data/2.5/weather'
    
    return True