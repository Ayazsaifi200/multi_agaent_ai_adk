import sys
import os
import json
from utils.env_helpers import load_env_safely  # Changed import

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the multi-agent system 
from main import MultiAgentSystem

def evaluate_goal_satisfaction(goals):
    """Evaluate if the system satisfies various goals"""
    load_env_safely()  # Changed to use the safe loading function
    
    system = MultiAgentSystem()
    results = []
    
    for i, goal in enumerate(goals):
        print(f"\n==== EVALUATING GOAL {i+1}: {goal} ====")
        
        # Process the goal
        result = system.process_goal(goal)
        
        # Check if goal was satisfied
        satisfied = "summary" in result and len(result.get("summary", "")) > 50
        
        # Store evaluation result
        eval_result = {
            "goal": goal,
            "satisfied": satisfied,
            "summary_length": len(result.get("summary", "")),
            "contains_weather": "weather" in result,
            "contains_launch_info": "mission_name" in result,
            "result": result
        }
        
        results.append(eval_result)
        
        # Print evaluation
        print(f"Goal satisfied: {satisfied}")
        print(f"Summary length: {eval_result['summary_length']} chars")
        print(f"Contains weather info: {eval_result['contains_weather']}")
        print(f"Contains launch info: {eval_result['contains_launch_info']}")
    
    # Save evaluation results
    with open("evaluation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    return results

if __name__ == "__main__":
    # Define test goals
    test_goals = [
        "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed.",
        "Tell me about the next SpaceX mission and if weather conditions look favorable."
    ]
    
    # Run evaluation
    evaluate_goal_satisfaction(test_goals)