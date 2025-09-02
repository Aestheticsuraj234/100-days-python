# Few Shot Prompting

from dotenv import load_dotenv
import os
import json
# Load environment variables from .env file
load_dotenv()

from openai import OpenAI
import requests


client = OpenAI(
    api_key=os.getenv("GOOGLE_API"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


def get_weather(city:str):
    try:
        url = f"http://wttr.in/{city.lower()}?format=%C+%t"
        response = requests.get(url, verify=False)  
        response.raise_for_status() 
        return f"The weather in {city} is {response.text}"
    except requests.RequestException as e:
        return f"Failed to get weather for {city}: {str(e)}"

# Few Shot Prompting : Directly Giving the inst to the model and few examples to the model
SYSTEM_PROMPT = """

You are an expert AI Assistant in resolving user queries using chain of thought.
You work on START , PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done , finally you can give an OUTPUT.
You can also call a tool if required from the list of available tools.

Rules:
- Strictly follow the output in JSON format
-Only run one step at a time
- The sequence of steps is START ( Where you should start ) , PLAN ( What needs to be done ) , OUTPUT ( The final output ).

OUTPUT Json Format.
{
    "step":"START" | "PLAN | "OUTPUT" | "TOOL, "content": "string"
    
    Available Tools
    - get_weather(city:str): Takes city name as input and returns the weather in that city
    
    Example 1:
    START: Hey , Can You solve 2 + 3 * 5 / 10
    PLAN:{"step": "PLAN" , "content": "Looking at the problem , we should solve this using BODMAS" }
    PLAN:{"step":"PLAN" , "content":"Yes , The BODMAS is correct thing to be done here"}
    PLAN:{"step":"PLAN" , "content":"First we must multiply 3 * 5 which is 15"}
    PLAN:{"step":"PLAN" , "content":"Now we must add 2 + 15 / 10 which is 2 + 1.5"}
    PLAN:{"step":"PLAN" , "content":"Now we must subtract 2 + 1.5 which is 3.5"}
    PLAN:{"step":"PLAN" , "content":"The final answer is 3.5"}
    OUTPUT:{"step":"OUTPUT" , "content":"3.5"}

    Example 2:
      START: Hey , What is the weather in Delhi?
    PLAN:{"step": "PLAN" , "content": "Seems like you want to know the weather in Delhi" }
    PLAN:{"step":"PLAN" , "content":"Let's see if we have any available tools"}
    PLAN:{"step":"PLAN" , "content":"Great! We have the get_weather tool"}
    PLAN:{"step":"TOOL" , "content":"Using get_weather('Delhi') to fetch the current weather"}
    PLAN:{"step":"PLAN" , "content":"Weather information retrieved successfully"}
    OUTPUT:{"step":"OUTPUT" , "content":"The weather in Delhi is currently sunny and 32°C"}
}
    
    
"""


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]


user_query = input("👉🏻 ")
message_history.append({"role": "user", "content": user_query})

while True:
    try:
        response = client.chat.completions.create(
            model="gemini-1.5-flash",
            response_format={"type":"json_object"},
            messages=[
                {
                    "role":"user" , "content":user_query
                }
            ]
        )
        
        raw_result = response.choices[0].message.content
        if not raw_result:
            print("❌ Error: No response received")
            break
            
        message_history.append({"role":"assistant" , "content": raw_result})
        parsed_result = json.loads(raw_result)
        
        step = parsed_result.get("step", "")
        content = parsed_result.get("content", "")
        
        if step == "START":
            print("🔥 ", content)
            continue
        
        if step == "PLAN":
            print("🧠 ", content)
            continue
        
        if step == "TOOL":
            print("🔧 ", content)
            # Here you would actually call the tool
            continue
        
        if step == "OUTPUT":
            print("🤖 ", content)
            break
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        break




# Few Shot Prompting : Directly Giving the inst to the model and few examples to the model