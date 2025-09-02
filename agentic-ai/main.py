from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
load_dotenv()

client = OpenAI( api_key=os.getenv("GOOGLE_API"),
    base_url="https://generativelanguage.googleapis.com/v1beta/")


def get_weather(city:str):
    try:
        url = f"http://wttr.in/{city.lower()}?format=%C+%t"
        response = requests.get(url, verify=False)  # Disable SSL verification
        response.raise_for_status()  # Raise an exception for bad status codes
        return f"The weather in {city} is {response.text}"
    except requests.RequestException as e:
        return f"Failed to get weather for {city}: {str(e)}"
    
    
def main():
    user_query = input("👉🏻   ")
    response = client.chat.completions.create(
        model="gemini-1.5-flash",
        n=1,
        messages=[
            {
                "role":"user" , "content":user_query
            }
        ]
    )
    
    print(f"🤖 {response.choices[0].message.content}")


print(get_weather("noida"))

# if __name__ == "__main__":
#     main()
    
    