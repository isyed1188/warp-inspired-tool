# setup.py
from setuptools import setup

APP = ['main.py']
DATA_FILES = []  # Add any data files your app needs here, for example:  [('images', ['images/icon.png'])].
OPTIONS = {
    'argv_emulation': True,  # Emulates command-line arguments
    'packages': ['ai_integration'],  # Include the ai_integration package
    'includes': ['openai', 'ollama', 'anthropic', 'openrouter', 'prompt_toolkit', 'requests'],  # List all dependencies
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
