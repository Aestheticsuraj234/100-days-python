from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client  = Client(
    host="http://localhost:11434",
)
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
async def chat(message: str = Body(..., description="Message")):
    response = client.chat(
        model="gpt-oss:20b",
        messages=[{"role": "user", "content": message}]
    )
    
    return {"response": response['message']['content']}