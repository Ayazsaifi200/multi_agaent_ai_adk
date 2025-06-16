import sys
import os
import json
from utils.env_helpers import load_env_safely  # Changed import

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the planner agent
from agents.planner_agent import PlannerAgent

def evaluate_planner_consistency(test_cases):
    """Evaluate if the planner produces consistent and appropriate plans"""
    load_env_safely()  # Changed to use the safe loading function
    
    planner = PlannerAgent()
    results = []
    
    for case in test_cases:
        goal = case["goal"]
        expected_agents = case["expected_agents"]
        
        print(f"\n==== EVALUATING PLANNER FOR: {goal} ====")
        
        # Get the plan
        plan = planner.create_plan(goal)
        
        # Check if all expected agents are in the plan
        all_expected_included = all(agent in plan for agent in expected_agents)
        
        # Check correct order for specific agent pairs
        correct_order = True
        for i in range(len(expected_agents) - 1):
            agent1 = expected_agents[i]
            agent2 = expected_agents[i + 1]
            
            if agent1 in plan and agent2 in plan:
                idx1 = plan.index(agent1)
                idx2 = plan.index(agent2)
                if idx1 > idx2:  # Check if order is incorrect
                    correct_order = False
        
        # Store evaluation result
        eval_result = {
            "goal": goal,
            "expected_agents": expected_agents,
            "actual_plan": plan,
            "all_expected_included": all_expected_included,
            "correct_order": correct_order
        }
        
        results.append(eval_result)
        
        # Print evaluation
        print(f"Generated plan: {plan}")
        print(f"All expected agents included: {all_expected_included}")
        print(f"Correct agent ordering: {correct_order}")
    
    # Save evaluation results
    with open("planner_evaluation.json", "w") as f:
        json.dump(results, f, indent=2)
    
    return results

if __name__ == "__main__":
    # Define test cases
    test_cases = [
        {
            "goal": "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed.",
            "expected_agents": ["spacex_agent", "weather_agent", "summary_agent"]
        },
        {
            "goal": "Tell me about the next SpaceX mission.",
            "expected_agents": ["spacex_agent", "summary_agent"]
        },
        {
            "goal": "What's the weather like at the next rocket launch site?",
            "expected_agents": ["spacex_agent", "weather_agent"]
        }
    ]
    
    # Run evaluation
    evaluate_planner_consistency(test_cases)