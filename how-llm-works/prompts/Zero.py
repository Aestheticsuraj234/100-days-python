# Zero Shot Prompting
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("GOOGLE_API"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
# Zero Shot Prompting : Directly Giving the inst to the model
SYSTEM_PROMPT = "You should only and only ans the coding related questions. do not ans anythign else. your name is alex if user ask something other than coding just say sorry"



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

# Zero Shot prompting the model is given the inst to the model without any prior examples