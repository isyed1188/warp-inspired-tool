# Warp-Inspired Terminal Enhancer

Welcome to the **Warp-Inspired Terminal Enhancer**! This open-source project brings innovative features inspired by [Warp](https://github.com/warpdotdev/Warp) to your existing terminal, leveraging Python for scripting, automation, and AI-powered enhancements.

## 🚀 Features

*   **AI-Powered Command Suggestions**: Get smart command completions using local (Ollama, optional) or cloud-based AI (OpenAI, Claude, Grok, OpenRouter).
*   **Cross-Platform Compatibility**: Works on macOS, Linux, and Windows.
*   **Chat Mode (OpenRouter only)**: Interact with the AI in a conversational way.

## 📦 Installation

See the [INSTRUCTIONS.txt](INSTRUCTIONS.txt) file for detailed, platform-specific installation and usage instructions.

**Quick Start:**

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/warp-inspired-tool.git  # Replace with the actual repository URL
    cd warp-inspired-tool
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    # or
    pip3 install -r requirements.txt
    ```

3.  **Set up API Keys:**

    You need to set environment variables for the AI provider API keys (e.g., `OPENAI_API_KEY`). Refer to `INSTRUCTIONS.txt` for detailed instructions on setting environment variables on different operating systems.  Ollama is optional and requires a local installation.

4. **Configure (optional):**

    Edit `config.py` to choose your preferred AI provider and model.

5.  **Run:**

    ```bash
    python main.py
    # or
    python3 main.py
    ```

## 🎮 Usage

*   Type a command idea (e.g., "list files") to get a suggestion.
*   Edit `config.py` to switch AI providers ("ollama", "openai", "grok", "claude", "openrouter").  Note that Ollama requires a local installation.
* Type `chat` to enter chat mode (only available with the "openrouter" provider).
* Type `exit` to quit.

## 📄 License

MIT License

## Troubleshooting

Refer to the `INSTRUCTIONS.txt` file for troubleshooting tips.
