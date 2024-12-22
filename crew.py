
from crewai import Agent, Crew, Process
from agents import nfl_data_collector,nfl_roster_changes, nfl_home_away_performance, nfl_injury_reports, nfl_head_to_head, nfl_season_performance, nfl_coaching_strategies, nfl_weather_performance,nfl_game_outcome_predictor 


# nfl_game_probability


from task import data_collection_task, data_analysis_task, probability_calculation_task,game_analysis_task


manager = Agent(
    role="Project Manager",
    goal="Efficiently manage the crew and ensure high-quality task completion and everything must be in order",
    backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
    allow_delegation=True,
)


# Define the crew with updated agents and tasks
crew = Crew(
    agents=[
        nfl_data_collector,
        nfl_roster_changes, 
        nfl_home_away_performance, 
        nfl_injury_reports, 
        nfl_head_to_head, 
        nfl_season_performance, 
        nfl_coaching_strategies, 
        nfl_weather_performance, 
        nfl_game_outcome_predictor 
  
    ],
    tasks=[data_collection_task, data_analysis_task,game_analysis_task, probability_calculation_task],
    process=Process.sequential,  # Tasks will execute in sequence: collection -> analysis -> probability calculation.
     manager_agent=manager,
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={"user_input": "Who will win the game on 25 Dec, 2024  Wednesday, Kansas City Chiefs vs. Pittsburgh Steelers?"})

print(result)


crew = Crew(
    agents=[
        nfl_data_collector,
        nfl_roster_changes, 
        nfl_home_away_performance, 
        nfl_injury_reports, 
        nfl_head_to_head, 
        nfl_season_performance, 
        nfl_coaching_strategies, 
        nfl_weather_performance, 
        nfl_game_outcome_predictor 
  
    ],
    tasks=[data_collection_task, data_analysis_task, probability_calculation_task],
    process=Process.sequential,  # Tasks will execute in sequence: collection -> analysis -> probability calculation.
)

result = crew.kickoff(inputs={"user_input": "Who will win the game on 22 Dec, 2024  Sunday, Kansas City Chiefs vs. Houston Texans?"})

print(result)

