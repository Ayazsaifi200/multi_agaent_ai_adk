cat > docs/system_flow.md << 'EOL'
# System Flow

This document explains the flow of the multi-agent system and how data passes between components.

## High-Level Architecture
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │ User Goal │ --> │ Planner │ --> │ Agent Chain │ --> │ Result │ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ │ ↑ │ └────────────────────┘ │ Iteration │ ↓ ┌─────────────┐ │ Evaluation │ └─────────────┘

## Detailed Flow

1. **User Input**
   - User provides a natural language goal
   - Example: "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed"

2. **Planning Phase**
   - The Planner Agent analyzes the goal
   - Determines which specialized agents are needed
   - Creates an execution plan with proper agent ordering
   - Example plan: ["spacex_agent", "weather_agent", "summary_agent"]

3. **Execution Phase**
   - System executes each agent in the planned order
   - Each agent:
     - Receives the output from the previous agent
     - Processes this data and enriches it
     - Passes the enriched data to the next agent

4. **Data Flow Example**

SpaceX Agent → Retrieves launch data (location, date, etc.) ↓ Weather Agent → Adds weather forecast for the launch location ↓ Summary Agent → Analyzes combined data to predict launch viability

5. **Iteration**
- After executing all agents, system checks if the goal is satisfied
- If not satisfied, system may:
  - Modify the plan
  - Re-execute certain agents
  - Gather additional information

6. **Result Delivery**
- Final enriched data is returned to the user
- Data includes all information gathered plus summary/analysis

## Data Transformation

Each agent transforms and enriches the data:

1. **SpaceX Agent**
- Input: None or minimal context
- Output: Launch details (mission, date, location, etc.)

2. **Weather Agent**
- Input: Launch details with location
- Output: Launch details + weather forecast

3. **Summary Agent**
- Input: Launch details + weather forecast
- Output: All previous data + analysis of launch viability

## Error Handling

- If an agent fails, the system will:
  - Log the error
  - Attempt to continue with partial data
  - Inform the user about incomplete results

## Extensibility

The system is designed to be extensible:
- New agents can be added by implementing the standard agent interface
- The planner can incorporate new agents into its planning logic
- Agent behavior can be modified independently
