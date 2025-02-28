# ai_integration/ollama.py
# Ollama API integration (optional)
from config import OLLAMA_MODEL

try:
    import ollama
except ImportError:
    ollama = None


def get_suggestion(prompt):
    if ollama:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": f"Suggest a terminal command for: {prompt}",
                }
            ],
        )
        return response.message.content.strip()
    else:
        return "Ollama is not installed. Please install it to use this feature or choose a different AI provider in config.py."
