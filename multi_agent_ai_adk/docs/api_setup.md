# API Setup Guide

This document explains how to set up the required API keys and endpoints for the multi-agent system.

## Required APIs

The system uses the following external APIs:

1. **Google Generative AI API (Gemini)** - For planning and summarization
2. **SpaceX API** - For retrieving launch information
3. **OpenWeatherMap API** - For weather forecasts

## API Key Setup

### Google API (Gemini)

1. Visit the [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key to your `.env` file as `GOOGLE_API_KEY=your_key_here`

### OpenWeatherMap API

1. Visit [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and create an account
2. Navigate to the "API Keys" tab in your account
3. Create a new API key (or use the default one)
4. Copy the API key to your `.env` file as `OPENWEATHERMAP_API_KEY=your_key_here`

### SpaceX API

The SpaceX API is public and does not require authentication. The system uses:
- Next launch endpoint: `https://api.spacexdata.com/v5/launches/next`

## Environment Configuration

Create a `.env` file in the `config` directory with the following content:

```
# API Keys
OPENWEATHERMAP_API_KEY=your_openweathermap_key
GOOGLE_API_KEY=your_google_api_key

# API Endpoints
SPACEX_API=https://api.spacexdata.com/v5/launches/next
WEATHER_API=https://api.openweathermap.org/data/2.5/weather
```

## API Response Formats

### SpaceX API

The SpaceX API returns launch information in this format:

```json
{
  "name": "Mission Name",
  "date_utc": "2023-01-01T00:00:00.000Z",
  "details": "Mission details...",
  "launchpad": "launchpad_id",
  "rocket": "rocket_id",
  ...
}
```

### OpenWeatherMap API

The OpenWeatherMap API returns weather data in this format:

```json
{
  "weather": [
    {
      "main": "Clear",
      "description": "clear sky"
    }
  ],
  "main": {
    "temp": 25.5,
    "humidity": 60
  },
  "wind": {
    "speed": 5.1
  },
  "visibility": 10000,
  "rain": {
    "1h": 0
  }
}
```

## API Rate Limits

- **OpenWeatherMap**: Free tier allows 60 calls/minute, 1,000,000 calls/month
- **SpaceX API**: No official rate limits, but be respectful with request frequency
- **Google Generative AI**: Check your quota in the Google AI Studio

## Troubleshooting

If you encounter API-related issues:

1. **Authentication errors**: Verify your API keys are correct in the `.env` file
2. **Rate limiting**: Ensure you're not exceeding the API's rate limits
3. **Endpoint changes**: Check if the API endpoints have changed
4. **Network issues**: Verify your internet connection and proxy settings

For persistent issues, check the respective API documentation:

- [OpenWeatherMap API Docs](https://openweathermap.org/api)
- [SpaceX API Docs](https://docs.spacexdata.com/docs/)
- [Google Generative AI Docs](https://developers.google.com/maker)