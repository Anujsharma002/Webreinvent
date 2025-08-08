from crewai import Task

def create_search_task(keyword: str, agent) -> Task:
    return Task(
        description=f"""
Your task is to search Google for the keyword: "{keyword}" using the tool: **Search the internet with Serper**.

You MUST extract the top 20 search results and return the following details for each result:
- Position (1-20)
- Title
- URL

Then, find if **WebReinvent Technologies Pvt. Ltd.** or **webreinvent.com** appears in any of these top 20 results.

Respond in this format:
[
  {{ "position": seo ranking, "title": "...", "url": "..." }},
  ...
]

Make sure the response is JSON-structured and only includes the results.
""",
        expected_output="Top 20 Google search results with title, URL, and position as structured list.",
        agent=agent
    )


def create_analysis_task(keyword: str, agent) -> Task:
    return Task(
        description=f"""
Your task is to perform SEO analysis for the keyword: "{keyword}" using ONLY the tool: **Search the internet with Serper**.

Steps:
1. Use the tool to search Google for the keyword.
   - Tool Input: `{{ "search_query": "{keyword}" }}`

2. From the top 10 results:
   - Check if any URL includes "webreinvent.com".
     - If yes, record its position, title, and URL.
     - If not, return: `"Not found:seo ranking"`

3. Choose the top 2 competitors from the results (excluding WebReinvent):
   For each, analyze:
   - Title
   - URL
   - Meta description (if available)
   - Assumed Domain Authority: Low / Medium / High (based on brand presence)
   - Visible SEO tactics (e.g., use of keyword, schema, location terms, etc.)

4. Provide SEO recommendations for WebReinvent:
   - Suggestions for content, meta titles/descriptions
   - Backlink strategies
   - Technical optimizations (e.g., structured data, page speed)

**IMPORTANT RULES**:
- Use only ONE tool at a time.
- After receiving search results, analyze them in memory.
- Do NOT use multiple tools simultaneously.

Return the final answer in this JSON format:
```json
{{
  "keyword": "{keyword}",
  "webreinvent": {{
    "found": true,
    "position": seo ranking,
    "title": "...",
    "url": "..."
  }},
  "competitors": [
    {{
      "position": seo ranking,
      "title": "...",
      "url": "...",
      "meta_description": "...",
      "domain_authority": "High",
      "seo_notes": "Used location keyword and structured data"
    }},
    ...
  ],
  "seo_recommendations": [
    "Add location-based keywords to the title",
    "Improve meta description with USP",
    "Add more internal links and schema markup"
  ]
}}
""",
expected_output="JSON output showing analysis of keyword rankings and SEO suggestions for WebReinvent.",
agent=agent
)