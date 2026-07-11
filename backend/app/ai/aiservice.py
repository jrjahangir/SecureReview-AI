import json
import requests

from backend.app.ai.prompt_builder import build_prompt
from backend.app.ai.validator import validate_ai_analysis


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

def analyze_with_ai(source_code):

    prompt = build_prompt(source_code)

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        ai_text = result.get("response", "").strip()

        # Try to parse AI JSON
        try:

            parsed = json.loads(ai_text)

            validated = validate_ai_analysis(parsed)

            return {
                "model": MODEL_NAME,
                "status": "success",
                "analysis": validated
            }

        except json.JSONDecodeError:

            return {
                "model": MODEL_NAME,
                "status": "text_response",
                "analysis": ai_text
            }

        except ValueError as validation_error:

            return {
                "model": MODEL_NAME,
                "status": "validation_error",
                "analysis": parsed,
                "error": str(validation_error)
            }

    except requests.exceptions.ConnectionError:

        return {
            "model": MODEL_NAME,
            "status": "connection_error",
            "analysis": None,
            "error": "Unable to connect to the Ollama server."
        }

    except requests.exceptions.Timeout:

        return {
            "model": MODEL_NAME,
            "status": "timeout",
            "analysis": None,
            "error": "AI request timed out."
        }

    except requests.exceptions.RequestException as e:

        return {
            "model": MODEL_NAME,
            "status": "request_error",
            "analysis": None,
            "error": str(e)
        }

    except Exception as e:

        return {
            "model": MODEL_NAME,
            "status": "unexpected_error",
            "analysis": None,
            "error": str(e)
        }