# main.py
# Main script for the Warp-Inspired Terminal Enhancer
from prompt_toolkit import prompt
from config import AI_PROVIDER
from ai_integration import openai, grok, claude, openrouter
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_ai_suggestion(provider, user_input):
    try:
        if provider == "ollama":
            try:
                from ai_integration import ollama
                return ollama.get_suggestion(user_input)
            except ImportError:
                return "Ollama is selected as the AI provider but the 'ollama' package is not installed. Please install it or choose a different provider in config.py."
        elif provider == "openai":
            return openai.get_suggestion(user_input)
        elif provider == "grok":
            return grok.get_suggestion(user_input)
        elif provider == "claude":
            return claude.get_suggestion(user_input)
        elif provider == "openrouter":
            return openrouter.chat_with_model(user_input)
        else:
            return "Invalid AI provider"
    except Exception as e:
        logging.error(f"Error getting suggestion: {e}")
        return "An error occurred while getting the AI suggestion. Please try again later."


def main():
    print("Welcome to Warp-Inspired Terminal Enhancer!")
    while True:
        user_input = prompt("Enter command: ")
        if user_input.lower() == "exit":
            break
        if user_input.lower() == "chat":
            if AI_PROVIDER == "openrouter":
                while True:
                    chat_input = prompt("You: ")
                    if chat_input.lower() == "exit":
                        break
                    response = get_ai_suggestion(AI_PROVIDER, chat_input)
                    print(f"Model: {response}")
            else:
                print("Chat functionality is only available with OpenRouter. Please update your AI_PROVIDER to 'openrouter' in config.py")
        else:
            suggestion = get_ai_suggestion(AI_PROVIDER, user_input)
            print(f"Suggestion: {suggestion}")


if __name__ == "__main__":
    main()
