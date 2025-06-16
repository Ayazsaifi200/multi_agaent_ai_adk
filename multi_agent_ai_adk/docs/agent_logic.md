
# Agent Logic

This document explains the logic and responsibility of each agent in the multi-agent system.

## Planner Agent

**Purpose**: Determine which agents to use and in what order based on the user goal.

**Logic**:
1. Analyzes the user goal using Google's Generative AI
2. Identifies key tasks needed to achieve the goal
3. Maps tasks to available specialized agents
4. Determines optimal execution order
5. Returns an ordered list of agent names

**Input**: User goal as natural language
**Output**: Ordered list of agent names to execute

## SpaceX Agent

**Purpose**: Retrieve information about upcoming SpaceX launches.

**Logic**:
1. Makes API requests to SpaceX's public API
2. Parses launch data (mission name, date, details)
3. Extracts location information for the launch site
4. Returns structured launch information

**Input**: None or minimal context from previous steps
**Output**: Structured launch data including:
- Mission name
- Launch date
- Launch site details (name, coordinates)
- Mission details

## Weather Agent

**Purpose**: Get weather forecasts for specific locations.

**Logic**:
1. Extracts location coordinates from input data
2. Makes API requests to OpenWeatherMap API
3. Parses weather data (conditions, temperature, wind, etc.)
4. Combines weather data with the original input data

**Input**: Data containing location information (latitude/longitude)
**Output**: Original data enriched with weather information:
- Weather conditions
- Temperature
- Wind speed
- Precipitation
- Humidity
- Visibility

## Summary Agent

**Purpose**: Analyze combined information and create meaningful summaries.

**Logic**:
1. Examines all data collected by previous agents
2. Uses Google's Generative AI to analyze patterns and relationships
3. Generates insights about launch viability based on weather
4. Creates a natural language summary of findings

**Input**: Enriched data from all previous agents
**Output**: All previous data plus:
- Natural language summary
- Analysis of how weather might impact the launch
- Prediction of potential delays

## Agent Interaction Patterns

The agents follow these interaction patterns:

1. **Sequential Processing**:
   - Each agent processes the output of the previous agent
   - Data is progressively enriched at each step

2. **Contextual Awareness**:
   - Later agents have access to all data gathered earlier
   - Each agent can make decisions based on the full context

3. **Fallback Mechanisms**:
   - If an agent encounters errors, it provides reasonable defaults
   - System can continue functioning with partial data

4. **Self-contained Logic**:
   - Each agent handles its own API requests and error handling
   - Agents are independent modules that can be replaced or updated
