# ai_integration/openrouter.py
import openrouter
from openrouter import ChatCompletion
from config import OPENROUTER_API_KEY, OPENROUTER_MODEL

openrouter.api_key = OPENROUTER_API_KEY

def chat_with_model(user_input):
    response = ChatCompletion.create(
        model=OPENROUTER_MODEL,
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message['content'].strip()

if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_model(user_input)
        print(f"Model: {response}")
