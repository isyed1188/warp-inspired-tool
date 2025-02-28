# ai_integration/claude.py
# Claude API integration
from anthropic import Anthropic
from config import CLAUDE_API_KEY

client = Anthropic(api_key=CLAUDE_API_KEY)

from config import CLAUDE_MODEL

def get_suggestion(prompt):
    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=50,
        messages=[{"role": "user", "content": f"Suggest a terminal command for: {prompt}"}]
    )
    return response.content[0].text.strip()
