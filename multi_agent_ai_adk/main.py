from agents.planner_agent import PlannerAgent
from agents.spacex_agent import SpaceXAgent
from agents.weather_agent import WeatherAgent
from agents.summary_agent import SummaryAgent
import json
import os
from utils.env_helpers import load_env_safely
load_env_safely()

class MultiAgentSystem:
    def __init__(self):
        # Initialize all agents
        self.planner = PlannerAgent()
        self.agents = {
            "spacex_agent": SpaceXAgent(),
            "weather_agent": WeatherAgent(),
            "summary_agent": SummaryAgent()
        }
    
    def process_goal(self, goal, max_iterations=3):
        """Process a user goal through the multi-agent system"""
        print(f"Processing goal: {goal}")
        
        # Step 1: Create plan
        plan = self.planner.create_plan(goal)
        print(f"Plan: {plan}")
        
        # Step 2: Execute plan
        result = None
        for i in range(max_iterations):
            print(f"\nIteration {i+1}:")
            
            # Execute each agent in the plan
            for agent_name in plan:
                if agent_name in self.agents:
                    print(f"Running {agent_name}...")
                    agent = self.agents[agent_name]
                    result = agent.process(result)
                else:
                    print(f"Warning: Agent {agent_name} not found")
            
            # Check if goal is satisfied
            if self._is_goal_satisfied(goal, result):
                print("Goal satisfied!")
                break
            
            print(f"Goal not yet satisfied. Refining plan...")
        
        return result
    
    def _is_goal_satisfied(self, goal, result):
        """Check if the goal has been satisfied by the result"""
        # Basic check: If we have a summary, we consider the goal satisfied
        if result and "summary" in result and result["summary"]:
            return True
        return False

def main():
    system = MultiAgentSystem()
    
    # Example goal
    goal = "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."
    
    # Process the goal
    result = system.process_goal(goal)
    
    # Print the final result
    print("\n==== FINAL RESULT ====")
    print(json.dumps(result, indent=2))
    
    # Save the result to the evals directory
    os.makedirs("evals", exist_ok=True)
    with open("evals/result.json", "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()