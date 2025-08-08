from crewai import Crew, Agent, Task, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# --- Load environment variables early ---
load_dotenv()

# --- Custom Serper Tool Definition ---

class CustomSerperTool(SerperDevTool):
    name: str = "Search the internet with Serper"
    description: str = "Searches Google using Serper"

    def __init__(self):
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            raise ValueError("❌ SERPER_API_KEY not found in environment variables.")
        super().__init__(api_key=api_key)

# --- LLM Setup ---
llm = LLM(
    model="ollama/mistral",                  # Or "mistral" depending on your Ollama setup
    base_url="http://localhost:11434"        # Ensure Ollama is running and serving here
)

# --- Agent: Search Specialist ---
search_agent = Agent(
    role="Search Specialist",
    goal="Perform Google searches using Serper.dev",
    backstory=(
        "You are skilled at performing real-time searches to gather accurate search results. "
        "You use the Serper.dev API to get data directly from Google and structure it clearly."
    ),
    tools=[CustomSerperTool()],
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tool_choice="required"
)

# --- Agent: SEO Analyst ---
analysis_agent = Agent(
    role="SEO Analyst",
    goal="Analyze search results and find WebReinvent's rank and position",
    backstory=(
        "You're an experienced SEO analyst responsible for tracking how well a company ranks for various search keywords. "
        "You provide recommendations to improve search engine rankings."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Optional Debug Step
if __name__ == "__main__":
    print("✅ Setup complete. Agents are ready to be assigned tasks.")
