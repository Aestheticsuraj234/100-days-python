# Few Shot Prompting - Fixed Version

from dotenv import load_dotenv
import os
import json
from typing import Optional, Literal

# Load environment variables from .env file
load_dotenv()

from openai import OpenAI
import requests
from pydantic import BaseModel, Field

# Initialize OpenAI client for Google's Gemini API
client = OpenAI(
    api_key=os.getenv("GOOGLE_API"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


def run_command(command: str) -> str:
    """
    Run a command and return the output.
    
    Args:
        command (str): The command to run
        
    Returns:
        str: The output of the command
    """
    return os.popen(command).read()

def get_weather(city: str) -> str:
    """
    Get weather information for a given city.
    
    Args:
        city (str): The name of the city
        
    Returns:
        str: Weather information or error message
    """
    try:
        url = f"http://wttr.in/{city.lower()}?format=%C+%t"
        response = requests.get(url, verify=False, timeout=10)
        response.raise_for_status()
        return f"The weather in {city} is {response.text.strip()}"
    except requests.RequestException as e:
        return f"Failed to get weather for {city}: {str(e)}"


# Pydantic model for structured output
class MyOutputFormat(BaseModel):
    step: Literal["START", "PLAN", "TOOL", "OUTPUT"] = Field(
        ..., 
        description="The type of step being executed"
    )
    content: str = Field(
        ..., 
        description="The content/description of the step"
    )
    tool_name: Optional[str] = Field(
        None, 
        description="Name of the tool to execute (only for TOOL steps)"
    )
    tool_input: Optional[str] = Field(
        None, 
        description="Input parameter for the tool (only for TOOL steps)"
    )


# Available tools mapping
AVAILABLE_TOOLS = {
    "get_weather": get_weather,
    "run_command": run_command
}


# System prompt with few-shot examples
SYSTEM_PROMPT = """
You are an expert AI Assistant that resolves user queries using chain of thought reasoning.
You work through START, PLAN, TOOL (if needed), and OUTPUT steps.

Rules:
- Follow the exact JSON format specified
- Only execute one step at a time
- Sequence: START → PLAN (multiple steps allowed) → TOOL (if needed) → OUTPUT
- For TOOL steps, specify tool_name and tool_input

Available Tools:
- get_weather(city: str): Returns weather information for the specified city
- run_command(command: str): Runs a command and returns the output

Examples:

User: "Can you solve 2 + 3 * 5 / 10?"

Step 1: {"step": "START", "content": "I need to solve the mathematical expression 2 + 3 * 5 / 10 using proper order of operations"}
Step 2: {"step": "PLAN", "content": "I'll use BODMAS/PEMDAS: First multiplication and division from left to right, then addition"}
Step 3: {"step": "PLAN", "content": "First: 3 * 5 = 15"}
Step 4: {"step": "PLAN", "content": "Then: 15 / 10 = 1.5"}
Step 5: {"step": "PLAN", "content": "Finally: 2 + 1.5 = 3.5"}
Step 6: {"step": "OUTPUT", "content": "The answer is 3.5"}

User: "What's the weather in Delhi?"

Step 1: {"step": "START", "content": "User wants to know the current weather in Delhi"}
Step 2: {"step": "PLAN", "content": "I need to use the get_weather tool to fetch current weather information for Delhi"}
Step 3: {"step": "TOOL", "content": "Calling weather tool for Delhi", "tool_name": "get_weather", "tool_input": "Delhi"}
Step 4: {"step": "PLAN", "content": "Weather data retrieved successfully, preparing response"}
Step 5: {"step": "OUTPUT", "content": "Based on the weather tool, [weather information will be inserted here]"}

Now process the user's query following this pattern.
"""


def execute_tool(tool_name: str, tool_input: str) -> str:
    """
    Execute a tool with the given input.
    
    Args:
        tool_name (str): Name of the tool to execute
        tool_input (str): Input parameter for the tool
        
    Returns:
        str: Result of tool execution
    """
    if tool_name in AVAILABLE_TOOLS:
        try:
            result = AVAILABLE_TOOLS[tool_name](tool_input)
            return result
        except Exception as e:
            return f"Error executing {tool_name}: {str(e)}"
    else:
        return f"Tool '{tool_name}' not found in available tools"


def main():
    """Main function to run the few-shot prompting system."""
    
    # Initialize message history
    message_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    
    # Get user input
    user_query = input("👉🏻 Enter your query: ").strip()
    if not user_query:
        print("❌ Please enter a valid query")
        return
    
    message_history.append({"role": "user", "content": user_query})
    
    tool_results = {}  # Store tool results for reference
    
    while True:
        try:
            # Make API call
            response = client.chat.completions.parse(
                model="gemini-1.5-flash",
                response_format=MyOutputFormat,
                messages=message_history,
                temperature=0.1  # Lower temperature for more consistent reasoning
            )
            
            # Parse response
            parsed_result = response.choices[0].message.parsed
            raw_content = response.choices[0].message.content
            
            # Add assistant response to history
            message_history.append({"role": "assistant", "content": raw_content})
            
            step = parsed_result.step
            content = parsed_result.content
            
            # Process different step types
            if step == "START":
                print(f"🔥 START: {content}")
                
            elif step == "PLAN":
                print(f"🧠 PLAN: {content}")
                
            elif step == "TOOL":
                print(f"🔧 TOOL: {content}")
                
                # Execute the tool if specified
                if parsed_result.tool_name and parsed_result.tool_input:
                    tool_result = execute_tool(parsed_result.tool_name, parsed_result.tool_input)
                    tool_results[parsed_result.tool_name] = tool_result
                    print(f"🛠️  Tool Result: {tool_result}")
                    
                    # Add tool result to message history for context
                    message_history.append({
                        "role": "user", 
                        "content": f"Tool '{parsed_result.tool_name}' returned: {tool_result}"
                    })
                else:
                    print("⚠️  Tool step specified but no tool details provided")
                
            elif step == "OUTPUT":
                # If the output references tool results, substitute them
                final_content = content
                for tool_name, result in tool_results.items():
                    if "[weather information will be inserted here]" in final_content:
                        final_content = final_content.replace(
                            "[weather information will be inserted here]", 
                            result
                        )
                
                print(f"🤖 OUTPUT: {final_content}")
                break
            
            else:
                print(f"❓ Unknown step type: {step}")
                break
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            print("💡 This might be due to API issues or malformed responses")
            break


if __name__ == "__main__":
    main()