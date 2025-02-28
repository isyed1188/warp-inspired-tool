# ai_integration/openai.py
# ai_integration/openai.py
# OpenAI API integration
import openai
from config import OPENAI_API_KEY, OPENAI_MODEL
import time
import logging

openai.api_key = OPENAI_API_KEY

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_suggestion(prompt):
    max_retries = 3
    retry_delay = 1  # seconds

    for attempt in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": f"Suggest a terminal command for: {prompt}"}],
                max_tokens=50
            )
            return response.choices[0].message['content'].strip()
        except openai.error.RateLimitError as e:
            logging.warning(f"Rate limit exceeded: {e}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retry_delay *= 2  # Exponential backoff
        except openai.error.APIError as e:
            logging.error(f"OpenAI API error: {e}")
            return "An error occurred while communicating with the OpenAI API."
        except openai.error.AuthenticationError as e:
            logging.error(f"OpenAI Authentication Error: {e}. Check your API Key")
            return "Authentication error. Please check your OpenAI API key."
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return "An unexpected error occurred."

    logging.error(f"Failed to get suggestion after {max_retries} attempts.")
    return "Failed to get suggestion from OpenAI after multiple retries."
