from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from dotenv import load_dotenv
from main import Main
import logging

# Load environment variables from .env (like SERPER_API_KEY)
load_dotenv()

# Setup logger
logging.basicConfig(level=logging.INFO)

# FastAPI app instance
app = FastAPI(
    title="WebReinvent SEO Rank Tracker API",
    description="Analyze Google search presence and SEO opportunities using CrewAI agents.",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)
# Request schema
class KeywordRequest(BaseModel):
    keyword: str

# Health check endpoint
@app.get("/")
def root():
    return {"status": "API running", "usage": "POST /analyze-keyword with JSON body: { 'keyword': '...' }"}

# Keyword analysis endpoint
@app.post("/analyze-keyword")
async def analyze_keyword(data: KeywordRequest):
    keyword = data.keyword
    print(keyword)
    if not keyword:
        raise HTTPException(status_code=400, detail="Keyword is required")

    try:
        # Create tasks
        result = Main(keywords=keyword)
        if hasattr(result, "output"):
            result_text = result.output
        elif hasattr(result, "raw_output"):
            result_text = result.raw_output
        else:
            result_text = str(result) 
        result_text = result_text.strip()[7:-3]

        return { "result": result_text }

    except Exception as e:
        logging.exception("Error in analyzing keyword")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("backend_api:app", host="127.0.0.1", port=8000, reload=True)
    