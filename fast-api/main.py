from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id:int
    name:str
    origin:str
    
teas:List[Tea] = []


@app.get("/")
def read_root():
    return {"Hello": "World"}  

@app.get("/teas")
def get_teas():
    return teas  

@app.post("/teas")
def add_tea(tea:Tea):
    teas.append(tea)
    return tea    

@app.put("/teas/{id}")
def update_tea(id:int , tea:Tea):
    for t in teas:
        if t.id == id:
            t.name = tea.name
            t.origin = tea.origin