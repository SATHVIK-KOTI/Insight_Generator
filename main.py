from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from web_search import get_web_data
from llm_handler import generate_insights_and_ideas

app = FastAPI()

# Enable CORS to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update with your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class TopicInput(BaseModel):
    query: str

# Root endpoint (optional health check)
@app.get("/")
def root():
    return {"message": "LLM Insight Generator API is running."}

# Main API route
@app.post("/generate_insights")
async def generate_insights(data: TopicInput):
    # Step 1: Get real-time news content
    web_content = get_web_data(data.query)
    print(f"🔎 News Content for '{data.query}':\n{web_content[:500]}...\n")  # Print trimmed for clarity

    # Step 2: Generate insights and content ideas
    response = await generate_insights_and_ideas(data.query, web_content)

    # Step 3: Return the result
    return {
        "query": data.query,
        "insights": response.get("insights"),
        "content_ideas": response.get("content_ideas"),
    }
