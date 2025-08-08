from crewai import Crew
from CrewUtils.webreinvent_agents import search_agent, analysis_agent
from CrewUtils.webreinvent_tasks import create_analysis_task, create_search_task
import pydantic
# List of keywords to check


def Main(keywords):
    keyword = keywords

    # Run for each keyword
    # for keyword in keywords:
    print(f"\n🔍 Running crew for keyword: {keyword}\n")
    search_task = create_search_task(keyword, search_agent)
    analysis_task = create_analysis_task(keyword, analysis_agent)    
    crew = Crew(
            agents=[search_agent, analysis_agent],
            tasks=[search_task,analysis_task],
            verbose=True
        )

    result = crew.kickoff()
    return result

    