


from crewai import Task
from agents import nfl_data_collector,nfl_roster_changes, nfl_home_away_performance, nfl_injury_reports, nfl_head_to_head, nfl_season_performance, nfl_coaching_strategies, nfl_weather_performance,nfl_game_outcome_predictor

from crewai import Process
from tools import calculator_tool,serper_tool




data_collection_task = Task(
    description=(
        "Collect comprehensive NFL data necessary to answer queries like '{user_input}'. "
        "Focus on gathering team performance metrics, player statistics, venue details, recent game outcomes, "
        "and any other relevant information that may influence the game's result. Ensure the data is accurate, "
        "up-to-date, and well-organized for downstream tasks."
    ),
    expected_output=(
        "Structured Dataset: \n"
        "- Columns: ['Team', 'Player', 'Position', 'Metric_Type', 'Metric_Value', 'Game_Date', 'Venue', 'Opponent']\n"
        "- Includes key metrics such as team performance, player stats, recent trends, and venue details.\n"
        "- Data is formatted as a JSON or CSV file for further analysis."
    ),
    tools=[serper_tool],  # Replace with actual tools used for scraping.
    agent=nfl_data_collector,
)
data_analysis_task = Task(
    description=(
        "Analyze the collected NFL data to extract actionable insights about trends, patterns, team strengths, "
        "historical performances, injury impacts, and other factors that may influence the game's outcome. "
        "Answer queries like '{user_input}' by identifying correlations, anomalies, or significant patterns "
        "from the collected data."
    ),
    expected_output=(
        "Analysis Report: \n"
        "- Section 1: Overview of team and player performance trends.\n"
        "- Section 2: Summary of key statistics and patterns from historical games.\n"
        "- Section 3: Impacts of injuries, weather, and venue on the game.\n"
        "- Section 4: Predictions supported by the data analysis.\n"
    ),
    tools=[calculator_tool],  # Replace with actual tools used for data analysis.
    agent=nfl_head_to_head
)
game_analysis_task = Task(
    description=(
        "Perform a comprehensive analysis using insights from all agents to evaluate the winning probability scores "
        "for both teams. Consider historical matchups, recent performances, coaching strategies, injuries, and external factors. "
        "Generate a well-rounded narrative summarizing key insights, implications, and actionable conclusions."
    ),
    expected_output=(
        "Detailed Report:\n"
        "- Winning Probabilities: Clear percentage breakdown for each team.\n"
        "- Key Insights: Factors contributing to each team's strengths and weaknesses.\n"
        "- Implications: How data insights affect the expected game dynamics.\n"
        "- Narrative Summary: Easy-to-read conclusions for non-technical stakeholders."
    ),
    tools=[serper_tool],  # Replace with actual tools used for analysis.
    agent=nfl_game_outcome_predictor,
)
probability_calculation_task = Task(
    description=(
        "Calculate the winning probabilities for the teams specified in the user query '{user_input}' "
        "based on data insights and advanced probability algorithms. Use a data-driven approach to compute "
        "a clear breakdown of each team's likelihood of winning, incorporating contextual factors like venue, injuries, "
        "weather, and historical performance."
    ),
    expected_output=(
        "Probability Report:\n"
        "- Team A Probability: XX% (Rationale and supporting data points).\n"
        "- Team B Probability: XX% (Rationale and supporting data points).\n"
        "- Key Factors: List of metrics and insights used in the calculation.\n"
        "- Summary: Clear, concise reasoning for the calculated probabilities."
    ),
    tools=[calculator_tool],  # Replace with actual tools used for probability calculations.
    agent=nfl_game_outcome_predictor,
)
