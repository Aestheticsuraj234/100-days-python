# Few Shot Prompting

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("GOOGLE_API"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
# Few Shot Prompting : Directly Giving the inst to the model and few examples to the model
SYSTEM_PROMPT = """You should only and only ans the coding related questions. do not ans anythign else. your name is alex if user ask something other than coding just say sorry.

Rule:
- Structly follow the output in JSON format

Output Format:
{{
    "code": "string" or null,
    "isCodingQuestion": boolean
}}

Examples:
Q: Can You explain the a + b whole suare?
A: Sorry , I can only help with coding related questions

Q: Hey , Write a code in python to adding two numbers?.
A: def add_numbers(a, b):
    return a + b
    
    
"""



response = client.chat.completions.create(
    model="gemini-1.5-flash",
    n=1,
    messages=[
        # System Prompt
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey , Can You explain a + b whole suare?",
        }
    ]
)

print(response.choices[0].message.content)

# Few Shot Prompting : Directly Giving the inst to the model and few examples to the model