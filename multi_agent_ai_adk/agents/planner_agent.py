import google.generativeai as genai
import os
import time
import random
from utils.env_helpers import load_env_safely
load_env_safely()
# Configure Google API
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

def retry_with_backoff(func, max_retries=5):
    """Retry function with exponential backoff"""
    retries = 0
    while retries < max_retries:
        try:
            return func()
        except Exception as e:
            if "ResourceExhausted" in str(e) or "429" in str(e):
                wait_time = (2 ** retries) + random.uniform(0, 1)
                print(f"Rate limit hit. Retrying in {wait_time:.1f} seconds...")
                time.sleep(wait_time)
                retries += 1
            else:
                raise
    raise Exception("Maximum retries exceeded")

class PlannerAgent:
    def __init__(self):
        # Initialize the generative model
       self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def create_plan(self, goal):
        """Create a plan based on the user goal"""
        try:
            prompt = f"""
            Given the following user goal: "{goal}"
            Create a plan with the optimal sequence of agents to achieve this goal.
            Available agents:
            - spacex_agent: Gets information about SpaceX launches
            - weather_agent: Gets weather information for specific locations
            - summary_agent: Creates summaries and analyzes information
            
            Return the list of agent names in the correct execution order.
            """
            
            response = self.model.generate_content(prompt)
            agent_list = self._parse_agent_list(response.text)
            
            # Default plan if parsing fails
            if not agent_list:
                return self._rule_based_planning(goal)
            
            return agent_list
            
        except Exception as e:
            print(f"Error using AI planner: {e}")
            print("Falling back to rule-based planning...")
            return self._rule_based_planning(goal)
    
    def _rule_based_planning(self, goal):
        """Simple rule-based planning when AI is unavailable"""
        goal = goal.lower()
        
        # Check for different patterns in the goal
        if "spacex" in goal and "weather" in goal and "summarize" in goal:
            return ["spacex_agent", "weather_agent", "summary_agent"]
        elif "spacex" in goal and "weather" in goal:
            return ["spacex_agent", "weather_agent"]
        elif "spacex" in goal:
            return ["spacex_agent", "summary_agent"]
        else:
            # Default plan for unknown goals
            return ["spacex_agent", "summary_agent"]
    
    def _parse_agent_list(self, response_text):
        """Parse the agent list from the response text"""
        try:
            # Extract agent names from response
            lines = response_text.strip().split('\n')
            agent_list = []
            for line in lines:
                line = line.strip()
                if "spacex_agent" in line:
                    agent_list.append("spacex_agent")
                elif "weather_agent" in line:
                    agent_list.append("weather_agent")
                elif "summary_agent" in line:
                    agent_list.append("summary_agent")
            return agent_list
        except Exception as e:
            print(f"Error parsing agent list: {e}")
            return []