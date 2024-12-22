

from crewai_tools import BaseTool, WebsiteSearchTool
from dotenv import load_dotenv
import os 
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool
load_dotenv()

import os 
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

os.environ['SERPER_API_KEY'] = os.environ.get('SERPER_API_KEY')



class CalculatorTool(BaseTool):
    name: str = "Calculator tool"
    description: str = (
        "Useful for performing mathematical calculations, including probability-related "
        "computations for NFL match predictions. Example inputs include mathematical expressions "
        "like `200*7` or `5000/2*10`. Specifically, it can calculate winning probabilities based on "
        "data inputs, such as team performance metrics, average scores, or head-to-head statistics."
   
    )

    def _run(self, operation: str) -> int:
        # Implementation goes here
        return eval(operation)


calculator_tool = CalculatorTool()





# Initialize the tool for internet searching capabilities
serper_tool = SerperDevTool(
    n_result=3
    )

serper_tool_nfl_scores = SerperDevTool(
    n_result=3,
    search_url="https://www.nfl.com/scores/",

    )


serper_injury_tool= SerperDevTool(
    n_result=3,
    search_url="https://www.nfl.com/injuries/",

    )



standing_serper_tool = SerperDevTool(
    n_results=3,
    search_url="https://www.nfl.com/standings/",

    )




























# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# from crewai_tools import ScrapeWebsiteTool


# # Initialize the tool with the website URL, 
# # so the agent can only scrap the content of the specified website
# tool = ScrapeWebsiteTool(website_url='https://www.pro-football-reference.com/years/2024/')

# # Extract the text from the site
# text = tool.run()
# print(text)



# Web_tool_passing = ScrapeWebsiteTool(website_url='https://www.nfl.com/stats/team-stats/offense/passing/2024/reg/all')

# # Extract the text from the site
# Web_tool_passing = Web_tool_passing.run()

# # print(text)
# Web_tool_rushing  = ScrapeWebsiteTool(website_url='https://www.nfl.com/stats/team-stats/offense/rushing/2024/reg/all')

# # Extract the text from the site
# Web_tool_rushing  = Web_tool_rushing.run()

# Web_tool_scoring = ScrapeWebsiteTool(website_url='https://www.nfl.com/stats/team-stats/offense/scoring/2024/reg/all')

# # Extract the text from the site
# Web_tool_scoring = Web_tool_scoring.run()


# Web_tool_passing  = WebsiteSearchTool(
#     website="https://www.nfl.com/stats/team-stats/offense/passing/2024/reg/all",
#     config=dict(
#         llm=dict(
#             provider="groq", # or google, openai, anthropic, llama2, ...
#             config=dict(
#                 model="gemma2-9b-it",
#                 # temperature=0.5,
#                 # top_p=1,
#                 # stream=true,
#             ),
#         ),
#         # embedder=dict(
#         #     provider="google", # or openai, ollama, ...
#         #     config=dict(
#         #         model="models/embedding-001",
#         #         task_type="retrieval_document",
#         #         # title="Embeddings",
#         #     ),
#         # ),
#     )
# )




# Web_tool_rushing =  WebsiteSearchTool(
#     website="https://www.nfl.com/stats/team-stats/offense/rushing/2024/reg/all",
#     config=dict(
#         llm=dict(
#             provider="groq", # or google, openai, anthropic, llama2, ...
#             config=dict(
#                 model="gemini-1.5-flash",
#                 # temperature=0.5,
#                 # top_p=1,
#                 # stream=true,
#             ),
#         ),
#       embedder=dict(
#             provider="google",
#             config=dict(
#                 model="models/text-embedding-004",
#                 # Uncomment if needed
#                 # task_type="retrieval_document",
#                 # title="Embeddings",
#             ),
#         ),
#     )
# )




# Web_tool_scoring =  WebsiteSearchTool(
#     website="https://www.nfl.com/stats/team-stats/offense/scoring/2024/reg/all",
#     config=dict(
#         llm=dict(
#             provider="groq", # or google, openai, anthropic, llama2, ...
#             config=dict(
#                 model="gemma2-9b-it",
#                 # temperature=0.5,
#                 # top_p=1,
#                 # stream=true,
#             ),
#         ),
#         # embedder=dict(
#         #     provider="google", # or openai, ollama, ...
#         #     config=dict(
#         #         model="models/embedding-001",
#         #         task_type="retrieval_document",
#         #         # title="Embeddings",
#         #     ),
#         # ),
#     )
# )
