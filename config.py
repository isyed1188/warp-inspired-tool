# config.py
# Settings for the AI providers
AI_PROVIDER = "ollama"  # Options: "ollama", "openai", "grok", "claude", "openrouter"
OLLAMA_MODEL = "llama3"  # Local Ollama model (requires local Ollama installation)
# OpenAI API Key - Set as environment variable: OPENAI_API_KEY
OPENAI_MODEL = "gpt-4"  # Default OpenAI model
# Grok API Key - Set as environment variable: GROK_API_KEY
# Claude API Key - Set as environment variable: CLAUDE_API_KEY
# OpenRouter API Key - Set as environment variable: OPENROUTER_API_KEY
OPENROUTER_MODEL = "openrouter/auto"  # Default OpenRouter model
CLAUDE_MODEL = "claude-3-opus-20240229"  # Default Claude model

# Instructions:
# 1. Set the above environment variables in your shell.
#    For example, in bash or zsh:
#    export OPENAI_API_KEY=your_actual_api_key
#    export GROK_API_KEY=your_actual_api_key
#    export CLAUDE_API_KEY=your_actual_api_key
#    export OPENROUTER_API_KEY=your_actual_api_key
# 2.  You may need to restart your terminal or source your profile
#     (e.g., source ~/.zshrc) for the changes to take effect.
