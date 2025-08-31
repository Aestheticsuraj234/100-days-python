from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("GOOGLE_API"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-1.5-flash",
    n=1,
    messages=[
        # System Prompt
        {"role": "system", "content": "You are an expert in maths and only and only answer maths related questions. if the query is related to maths. just say sorry and say i do not answer this questions. if the query is not related to maths, just answer the question"},
        {
            "role": "user",
            "content": "Explain Me to solve the integral of x^2",
        }
    ]
)

print(response.choices[0].message.content)

