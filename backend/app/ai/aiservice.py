import requests

from backend.app.ai.prompt_builder import build_prompt

def analyze_with_ai(source_code):

    prompt = build_prompt(source_code)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    result = response.json()

    return {
        "model": "llama3.2:3b",
        "analysis": result["response"]
    }