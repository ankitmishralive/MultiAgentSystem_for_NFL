



from crewai import Agent , LLM


# from tools import calculator_tool,serper_tool,Web_tool_scoring ,Web_tool_rushing ,Web_tool_passing,serper_injury_tool,standing_serper_tool


from tools import serper_tool,serper_injury_tool,standing_serper_tool,calculator_tool

from dotenv import load_dotenv
import os 





load_dotenv()
# from langchain.llms import Ollama


# Initialize Ollama model
llm = LLM(
    model="ollama/llama3.1:latest",
    base_url="http://localhost:11434"
)


# from langchain_google_genai import ChatGoogleGenerativeAI

# llm = LLM(model="groq/distil-whisper-large-v3-en")

# llm = LLM(model="groq/llama-3.1-8b-instant")

# HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# # from crewai import LLM

# llm = LLM(
#     model="Qwen/Qwen2.5-7B-Instruct",
#     api_key=HUGGINGFACE_API_KEY,
# )


# llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=os.getenv("GOOGLE_API_KEY"))


## Senior Research Agent 

nfl_data_collector = Agent(
    name="Agent 1",  # Added the missing comma here
    role="Examiniting the current momentum and form of both teams",
    goal=(
        "Efficiently scrape and compile high-quality NFL data from various "
        "online sources, ensuring accuracy  "
        "Examine the current Form and momentum of both teams by reviewing their last three games & also their form in overall league"
    
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a meticulous researcher with a keen eye for extracting "
        "relevant information from the web. Driven by curiosity, you thrive "
        "on collecting and curating data of both the teams of last 3 games that forms the backbone of analysis, "

    ),
    tools=[serper_tool,standing_serper_tool],  # Replace with the actual tool for scraping.
    llm=llm,
    allow_delegation=True , # Communicates with other agents for data processing.
       max_iter=1,
     max_execution_time=60,
    respect_context_window=True,
        system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",

)





# - Agent 2: Investigate any significant roster changes or trades that have occurred recently which might impact team dynamics.
# - Agent 3: Review the performance of both teams in away and home games respectively, as the location can influence the outcome.
# - Agent 4: Collect and analyze injury reports for key players on both teams leading up to the game on Dec 15.
# - Agent 5: Analyze head-to-head matchups between the Jets and Jaguars over the past five years to identify any patterns or trends.
# - Agent 6: Gather historical performance data of both the Jets and Jaguars for the current season, focusing on win/loss records, points scored, and points allowed.
# - Agent 7: Analyze the coaching strategies and decisions made by both teams in recent games to understand potential tactical advantages.
# - Agent 8: Evaluate the performance of both teams in similar weather conditions expected on game day, as weather can impact gameplay.




# Assuming `llm` and necessary tools are defined earlier

# Agent 2: Investigate significant roster changes or trades
nfl_roster_changes = Agent(
    name="Agent 2",
    role="Roster Analysis Specialist",
    goal=(
        "Investigate any significant roster changes or trades that have occurred recently which "
        "might impact team dynamics for the upcoming game "
        "Provide an analysis on how these changes might affect the team performance."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in tracking and analyzing roster changes, trades, and player transfers, "
        "understanding their impact on team performance and dynamics."
    ),
    tools=[serper_tool],  # Replace with tool for scraping relevant data
    llm=llm,
    allow_delegation=False,  # Can communicate with other agents if necessary
        max_iter=1,
     max_execution_time=60,
     respect_context_window=True,
         system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",

)

# Agent 3: Review performance in home and away games
nfl_home_away_performance = Agent(
    name="Agent 3",
    role="Performance Analyst",
    goal=(
        "Review the performance of both teams in away and home games respectively, "
        "as the location can influence the outcome of the game between the 2 Teams. "
        "Analyze team statistics for home/away games to identify potential advantages."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "As a performance analyst, you evaluate how home and away game locations affect team performance, "
        "providing insights based on past game data based on NFl Website"
    ),
    tools=[serper_tool],  # Replace with relevant data scraping or analysis tool
    llm=llm,
    allow_delegation=False,
        max_iter=1,
     max_execution_time=60,
     respect_context_window=True,
         system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",

)

# Agent 4: Collect and analyze injury reports
nfl_injury_reports = Agent(
    name="Agent 4",
    role="Injury Report Specialist",
    goal=(
        "Collect and analyze injury reports for key players on both teams  "
        "Assess how injuries might impact the teams' performance in the upcoming game."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in collecting and analyzing injury reports, assessing their potential impact on team performance."
    ),
    tools=[serper_tool,serper_injury_tool],  # Replace with a tool for gathering injury data
    llm=llm,
    allow_delegation=False,
            max_iter=1,
     max_execution_time=60,
     respect_context_window=True,
         system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",

)

# Agent 5: Analyze head-to-head matchups over the past five years
nfl_head_to_head = Agent(
    name="Agent 5",
    role="Head-to-Head Analyst",
    goal=(
        "Analyze the head-to-head matchups between both the teams over the past five years. "
        "Identify any patterns, trends, or significant observations that could influence the outcome of the game."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in analyzing head-to-head matchups and identifying trends from past games to provide insights for future matchups."
    ),
    tools=[serper_tool],  # Replace with a tool for scraping historical matchup data
    llm=llm,
      allow_delegation=False,
         max_iter=1,
     max_execution_time=60,
     respect_context_window=True,
         system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",

)

# Agent 6: Gather historical performance data for the current season
nfl_season_performance = Agent(
    name="Agent 6",
    role="Season Performance Analyst",
    goal=(
        "Gather historical performance data of both the teams for the current season. "
        "Focus on win/loss records, points scored, and points allowed to provide a comparative analysis for the {user_input}."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in gathering and analyzing seasonal performance data, comparing teams based on their win/loss records, scoring patterns, and defensive performance."
    ),
    tools=[serper_tool],  # Replace with a tool for fetching performance data for the season
    llm=llm,
      allow_delegation=False,
         max_iter=1,
     max_execution_time=60,
     respect_context_window=True,
         system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",

)

# Agent 7: Analyze coaching strategies
nfl_coaching_strategies = Agent(
    name="Agent 7",
    role="Coaching Strategy Analyst",
    goal=(
        "Analyze the coaching strategies and decisions made by both teams in recent games. "
        "Assess potential tactical advantages that could impact the outcome of the  game between both teams ."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in analyzing coaching decisions and strategies, evaluating how coaching choices influence team performance."
    ),
    tools=[serper_tool],  # Replace with relevant data scraping or analysis tool for coaching strategies
    llm=llm,
     allow_delegation=False,
          max_iter=1,
     max_execution_time=60,
     respect_context_window=True,
         system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",

)

# Agent 8: Evaluate performance in similar weather conditions
nfl_weather_performance = Agent(
    name="Agent 8",
    role="Weather Impact Analyst",
    goal=(
        "Evaluate the performance of both teams in similar weather conditions expected on the match day. "
        "Analyze past games played in similar weather to predict how weather may impact the gameplay."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in assessing how different weather conditions affect team performance, using past weather data and game results."
    ),
    tools=[serper_tool],  # Replace with a tool for gathering weather data and analyzing performance in similar conditions
    llm=llm,
     allow_delegation=False,
            max_iter=1,
     max_execution_time=60,
     respect_context_window=True,
         system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",

)




# Consolidated Agent: Game Outcome Predictor
nfl_game_outcome_predictor = Agent(
    name="Agent 9",
    role="Game Outcome Predictor",
    goal=(
        "Integrate insights from all specialized agents to provide a comprehensive analysis of the game. "
        "Calculate a winning probability score for each team based on key factors like roster changes, form, injuries, head-to-head stats, coaching strategies, and weather conditions. "
        "Summarize key insights and implications for the user."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in combining multi-agent insights to generate a holistic analysis, presenting a clear narrative and probability score for game outcomes.Answer with winning percentage of both teams"
    ),
    tools=[calculator_tool],
    llm=llm,
    allow_delegation=True,
    max_iter=1,
    max_execution_time=60,
    respect_context_window=True,
        system_template="""<|start_header_id|>system<|end_header_id|>
                        {{ .System }}<|eot_id|>""",
    prompt_template="""<|start_header_id|>user<|end_header_id|>
                        {{ .Prompt }}<|eot_id|>""",
    response_template="""<|start_header_id|>assistant<|end_header_id|>
                        {{ .Response }}<|eot_id|>""",
)



