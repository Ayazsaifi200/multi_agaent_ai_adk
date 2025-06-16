import google.generativeai as genai
import os
from utils.env_helpers import load_env_safely

load_env_safely()

# Configure API
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

try:
    # Try with a simpler model
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content("Hello, what is 2+2?")
    print("API Test Result:", response.text)
    print("API is working!")
except Exception as e:
    print(f"API Error: {e}")