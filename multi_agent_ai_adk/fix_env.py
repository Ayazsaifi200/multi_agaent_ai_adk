import os

# Ensure config directory exists
os.makedirs("config", exist_ok=True)

# Create a properly UTF-8 encoded .env file
with open('config/.env', 'w', encoding='utf-8') as f:
    f.write('''# API Keys
OPENWEATHERMAP_API_KEY=46c5f06235a7df007c4e200de781548f
GOOGLE_API_KEY=AIzaSyAhNM6WE84985_9AIuOLhwO0Oa2XarruNo
# API Endpoints
SPACEX_API=https://api.spacexdata.com/v5/launches/next
WEATHER_API=https://api.openweathermap.org/data/2.5/weather
''')

print("Created new .env file with proper UTF-8 encoding")