import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def virtual_therapy(session_input):
    system_prompt = "You are a compassionate virtual therapist providing gentle, non-judgmental support."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": session_input}
        ],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("Welcome to your Virtual Therapist. Type 'exit' to end the session.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        reply = virtual_therapy(user_input)
        print("Therapist:", reply)
