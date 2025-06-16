# Multi-Agent AI System Using Google ADK

This project implements a multi-agent system that orchestrates multiple specialized AI agents to achieve complex user goals. The system uses Google's Generative AI and public APIs to plan and execute multi-step tasks.

## Features

- **Dynamic Planning**: System analyzes user goals and creates optimal agent execution plans
- **Modular Agent Architecture**: Specialized agents for different tasks
- **Data Enrichment**: Each agent builds upon the previous agent's output
- **Iterative Refinement**: System iterates until the goal is satisfied

## Example Use Case

The system can process goals like:
- "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."

## Components

1. **Planner Agent**: Determines which agents to use and in what order
2. **SpaceX Agent**: Retrieves information about upcoming SpaceX launches
3. **Weather Agent**: Gets weather data for specific locations
4. **Summary Agent**: Analyzes and summarizes information, making predictions

## Setup

### Prerequisites
- Python 3.9+
- API keys for:
  - Google API (Gemini)
  - OpenWeatherMap

### Installation
1. Clone the repository 

2. Create a virtual environment

3. Install dependencies

4. Create a `.env` file in the `config` directory with your API keys


## Usage

Run the main script:


To evaluate the system:

## System Flow

1. User provides a goal
2. Planner agent analyzes the goal and creates an execution plan
3. System executes each agent in order, passing data between them
4. If the goal isn't satisfied, the system iterates with refinements
5. Final result is returned to the user

## Extending the System

To add a new agent:
1. Create a new agent file in the `agents` directory
2. Implement the `process` method
3. Add the agent to the `agents` dictionary in `main.py`

## Evaluation

The system includes evaluation scripts to test:
- Goal satisfaction across different queries
- Agent trajectory and planning logic
- System adaptability to different scenarios

## License

MIT