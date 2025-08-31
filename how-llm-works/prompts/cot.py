# Few Shot Prompting

from dotenv import load_dotenv
import os
import json
# Load environment variables from .env file
load_dotenv()

from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("GOOGLE_API"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
# Few Shot Prompting : Directly Giving the inst to the model and few examples to the model
SYSTEM_PROMPT = """

You are an expert AI Assistant in resolving user queries using chain of thought.
You work on START , PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done , finally you can give an OUTPUT

Rules:
- Strictly follow the output in JSON format
-Only run one step at a time
- The sequence of steps is START ( Where you should start ) , PLAN ( What needs to be done ) , OUTPUT ( The final output ).

OUPUT Json Format.
{
    "step":"START" | "PLAN | "OUTPUT", "content": "string"
    
    Example:
    START: Hey , Can You solve 2 + 3 * 5 / 10
    PLAN:{"step": "PLAN" , "content": "Looking at the problem , we should solve this using BODMAS" }
    PLAN:{"step":"PLAN" , "content":"Yes , The BODMAS is correct thing to be done here"}
    PLAN:{"step":"PLAN" , "content":"First we must multiply 3 * 5 which is 15"}
    PLAN:{"step":"PLAN" , "content":"Now we must add 2 + 15 / 10 which is 2 + 1.5"}
    PLAN:{"step":"PLAN" , "content":"Now we must subtract 2 + 1.5 which is 3.5"}
    PLAN:{"step":"PLAN" , "content":"The final answer is 3.5"}
    OUTPUT:{"step":"OUTPUT" , "content":"3.5"}
}
    
    
"""


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]


user_query = input("👉🏻 ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-1.5-flash",
        response_format={"type":"json_object"},
        messages=message_history
    )
    
    raw_result = response.choices[0].message.content
    message_history.append({"role":"assistant" , "content": raw_result})
    parsed_result = json.loads(raw_result)
    
    if parsed_result.get("step") == "START":
        print("🔥 ", parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "PLAN":
        print("🧠 ", parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "OUTPUT":
        print("🤖 ", parsed_result.get("content"))
        break




# Few Shot Prompting : Directly Giving the inst to the model and few examples to the model