import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def detect_ai(text):
    api_key = os.getenv("SAPLING_API_KEY")

    url = "https://api.sapling.ai/api/v1/aidetect"

    payload = {
        "key": api_key,
        "text": text
    }

    response = requests.post(url, json=payload)

    result = response.json()

    score = result.get("score", 0)  # 0 = human, 1 = AI

    return {
        "score": round(score * 100, 2),  # convert to percentage
        "label": "AI Generated" if score > 0.5 else "Human Written"
    }
if __name__ == "__main__":
    test = "Artificial intelligence is transforming education and industry."
    print(detect_ai(test))