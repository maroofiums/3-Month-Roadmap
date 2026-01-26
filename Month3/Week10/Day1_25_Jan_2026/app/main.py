from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    x: int
    y: int

@app.post("/multiply")
def multiply(data: InputData):
    return {"result": data.x * data.y}

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"sum": a + b}

