# NFL Game Prediction System

An AI-powered system that predicts NFL game outcomes using a multi-agent approach with comprehensive data analysis.

##  Overview

This system uses a crew of specialized AI agents to analyze various aspects of NFL games and provide detailed predictions. Each agent focuses on specific factors like team performance, injuries, weather conditions, and historical matchups to generate accurate predictions.

##  System Architecture


```mermaid
graph TD
    %% Define styles
    classDef external fill:#ffebeb,stroke:#ff0000,stroke-width:2px,color:black
    classDef tools fill:#ebffeb,stroke:#00aa00,stroke-width:2px,color:black
    classDef agents fill:#ebebff,stroke:#0000ff,stroke-width:2px,color:black
    classDef tasks fill:#ffffeb,stroke:#aaaa00,stroke-width:2px,color:black
    classDef management fill:#ffebff,stroke:#aa00aa,stroke-width:2px,color:black
    classDef env fill:#ebffff,stroke:#00aaaa,stroke-width:2px,color:black

    subgraph External["External Services Layer"]
        style External fill:#ffebeb,stroke:#ff0000,color:black
        API1["Serper API<br/>Web Search Service"]
        API2["Calculator API<br/>Mathematical Operations"]
    end

    subgraph Tools["Tools Integration Layer"]
        style Tools fill:#ebffeb,stroke:#00aa00,color:black
        T1["SerperDevTool<br/>Web Search Handler"]
        T2["CalculatorTool<br/>Math Operations Handler"]
        T3["SerperInjuryTool<br/>Injury Data Handler"]
        T4["StandingSerperTool<br/>Team Rankings Handler"]
    end

    subgraph Agents["Specialized Agents Layer"]
        style Agents fill:#ebebff,stroke:#0000ff,color:black
        
        subgraph DataAgents["Data Collection Agents"]
            style DataAgents fill:#f0f0ff,stroke:#0000ff,color:black
            A1["Data Collector<br/>Team Performance & Form"]
            A2["Roster Changes<br/>Team Composition"]
            A4["Injury Reports<br/>Player Status"]
        end
        
        subgraph AnalysisAgents["Analysis Agents"]
            style AnalysisAgents fill:#f0f0ff,stroke:#0000ff,color:black
            A3["Home/Away Performance<br/>Location Impact"]
            A5["Head-to-Head<br/>Historical Matchups"]
            A6["Season Performance<br/>Current Season Stats"]
        end
        
        subgraph StrategyAgents["Strategy Agents"]
            style StrategyAgents fill:#f0f0ff,stroke:#0000ff,color:black
            A7["Coaching Strategies<br/>Tactical Analysis"]
            A8["Weather Performance<br/>Environmental Impact"]
            A9["Game Outcome Predictor<br/>Final Analysis"]
        end
    end

    subgraph Tasks["Task Orchestration Layer"]
        style Tasks fill:#ffffeb,stroke:#aaaa00,color:black
        TK1["Data Collection Task<br/>Gather & Organize Data"]
        TK2["Data Analysis Task<br/>Process & Analyze"]
        TK3["Game Analysis Task<br/>Comprehensive Evaluation"]
        TK4["Probability Calculation<br/>Win Probability"]
    end

    subgraph Management["Crew Management Layer"]
        style Management fill:#ffebff,stroke:#aa00aa,color:black
        CM1["Project Manager Agent<br/>Oversight & Coordination"]
        CM2["Sequential Process Handler<br/>Task Execution Flow"]
    end

    subgraph Environment["Environment Configuration"]
        style Environment fill:#ebffff,stroke:#00aaaa,color:black
        ENV["Environment Variables<br/>API Keys & Configuration"]
    end

    %% Define relationships
    API1 ==>|"Provides Data"| T1
    API2 ==>|"Provides Calculations"| T2

    T1 -->|"Search Capability"| A1 & A2 & A3 & A5 & A6 & A7 & A8
    T2 -->|"Math Operations"| A9
    T3 -->|"Injury Data"| A4
    T4 -->|"Rankings Data"| A1

    A1 & A2 & A4 -->|"Raw Data"| TK1
    A3 & A5 & A6 -->|"Analysis Input"| TK2
    A7 & A8 -->|"Strategic Input"| TK2
    A9 -->|"Final Analysis"| TK3
    A9 -->|"Probability Data"| TK4

    TK1 -->|"Sequential Flow"| CM2
    TK2 -->|"Sequential Flow"| CM2
    TK3 -->|"Sequential Flow"| CM2
    TK4 -->|"Sequential Flow"| CM2

    CM1 -->|"Manages"| CM2

    ENV -->|"Configuration"| T1 & T2 & T3 & T4

    %% Apply styles
    class API1,API2 external
    class T1,T2,T3,T4 tools
    class A1,A2,A3,A4,A5,A6,A7,A8,A9 agents
    class TK1,TK2,TK3,TK4 tasks
    class CM1,CM2 management
    class ENV env
```

### System Components

1. **External Services Layer**
   - Serper API for web data collection
   - Calculator API for probability computations

2. **Tools Layer**
   - SerperDevTool: Handles web searches
   - CalculatorTool: Manages mathematical operations
   - SerperInjuryTool: Processes injury data
   - StandingSerperTool: Analyzes team rankings

3. **Specialized Agents**

   Data Collection Agents:
   - Data Collector: Analyzes team performance and form
   - Roster Changes: Tracks team composition changes
   - Injury Reports: Monitors player status

   Analysis Agents:
   - Home/Away Performance: Studies location impact
   - Head-to-Head: Analyzes historical matchups
   - Season Performance: Evaluates current season stats

   Strategy Agents:
   - Coaching Strategies: Examines tactical approaches
   - Weather Performance: Assesses environmental impact
   - Game Outcome Predictor: Generates final analysis

4. **Task Orchestration**
   - Data Collection Task
   - Data Analysis Task
   - Game Analysis Task
   - Probability Calculation Task

## 🚀 Getting Started

### Prerequisites
```bash
# Install required packages
pip install crewai
pip install python-dotenv
pip install crewai_tools
```

### Environment Setup
Create a `.env` file in your project root:
```env
SERPER_API_KEY=your_serper_api_key
GOOGLE_API_KEY=your_google_api_key
```

### Running the System
1. Clone the repository:
```bash
git clone https://github.com/ankitmishralive/MultiAgentSystem_for_NFL
cd nfl-prediction-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the prediction system:
```bash
python crew.py
```

##  Sample Output

Here's an example of the system's prediction output:


 ![sample_output](sample_output.jpeg)



##  System Components

### Agents
Each agent is specialized in analyzing specific aspects of the game:
- `nfl_data_collector`: Gathers current team performance data
- `nfl_roster_changes`: Analyzes recent team composition changes
- `nfl_injury_reports`: Tracks player availability
- And more...

### Tasks
The system executes tasks in sequence:
1. Data Collection
2. Data Analysis
3. Game Analysis
4. Probability Calculation

##  Usage Notes

1. **Input Format**
   - Use the following format for queries:
   ```python
   result = crew.kickoff(inputs={"user_input": "Who will win the game on [DATE], [TEAM A] vs. [TEAM B]?"})
   ```

2. **Interpreting Results**
   - Win probabilities are based on comprehensive analysis
   - Consider all factors mentioned in the analysis
   - Weather and injury reports are real-time when available

