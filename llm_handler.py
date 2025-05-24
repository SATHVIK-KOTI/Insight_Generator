import httpx
import traceback
from models.prompts import INSIGHT_PROMPT, CONTENT_IDEAS_PROMPT

# Ollama API configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

# Number of tokens to predict (controls response length)
NUM_PREDICT = 768  # Good for ~500-600 word response

# Handles communication with the Ollama LLM API
async def call_ollama(prompt: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=600.0) as client:  # Timeout set to 300 seconds
            response = await client.post(
                OLLAMA_URL,
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "num_predict": NUM_PREDICT
                    }
                }
            )
            response.raise_for_status()
            return response.json().get("response", "").strip()
    except Exception as e:
        print("❌ Ollama request failed:")
        traceback.print_exc()
        return f"Error: Ollama could not process the prompt. Details: {str(e)}"

# Orchestrates the prompt pipeline: insights -> content ideas
async def generate_insights_and_ideas(query: str, content: str):
    # Step 1: Extract key insights from web content
    prompt1 = INSIGHT_PROMPT.format(query=query, content=content)
    insights = await call_ollama(prompt1)

    # Step 2: Generate content ideas based on those insights
    prompt2 = insights + "\n\n" + CONTENT_IDEAS_PROMPT
    ideas = await call_ollama(prompt2)

    return {
        "insights": insights,
        "content_ideas": ideas
    }
