# Persona Shot Prompting
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("GOOGLE_API"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
# Persona  Prompting :
SYSTEM_PROMPT = """
You are an AI Persona Assistant. named Suraj Jha.
You are acting on behalf of piyush garg who is 25 year old tech enthusiast. and  principle engineer. your main tech stack is js and python you are learning genAI these days.


examples:

"""



response = client.chat.completions.create(
    model="gemini-1.5-flash",
    n=1,
    messages=[
        # System Prompt
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Can you write a python code to print hello world",
        }
    ]
)

print(response.choices[0].message.content)

# Persona Shot prompting the model is given the inst to the model without any prior examples