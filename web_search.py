import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_web_data(query: str, max_results: int = 5) -> str:
    today = datetime.utcnow().date()
    seven_days_ago = today - timedelta(days=7)

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "searchIn": "title,description",
        "from": seven_days_ago.isoformat(),
        "to": today.isoformat(),
        "language": "en",
        "sortBy": "relevancy",  # Could also be 'publishedAt'
        "pageSize": max_results,
        "page": 1,
        "apiKey": NEWS_API_KEY,
        # Optional: restrict to certain domains
        # "domains": "techcrunch.com,theverge.com,forbes.com"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("status") != "ok":
            print("❌ NewsAPI Error:", data.get("message", "Unknown error"))
            return "Error: NewsAPI failed."

        articles = data.get("articles", [])
        if not articles:
            print("🔍 No articles found for:", query)
            return "No relevant news found."

        summaries = []
        for article in articles[:max_results]:
            title = article.get("title", "No title")
            description = article.get("description", "No description")
            url = article.get("url", "")
            source = article.get("source", {}).get("name", "Unknown source")
            date = article.get("publishedAt", "")[:10]
            summaries.append(
                f"Title: {title}\nDescription: {description}\nSource: {source}, Published: {date}\nLink: {url}"
            )

        print(f"✅ NewsAPI returned {len(summaries)} articles.")
        return "\n\n".join(summaries)

    except Exception as e:
        print(f"❌ Exception while calling NewsAPI: {e}")
        return "Error: Could not retrieve news data."
