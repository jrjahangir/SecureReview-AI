from backend.app.ai.prompt_builder import build_prompt
def analyze_with_ai(source_code: str):

    prompt = build_prompt(source_code)

    print("========== AI Prompt ==========")
    print(prompt)

    return {
        "model": "simulation",
        "analysis": [
            "AI analysis will be connected in Lesson 16."
        ]
    }