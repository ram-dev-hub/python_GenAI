from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: int

@app.get("/")
def add(a: int, b: int):
    return {"result": a + b}
@app.post("/addItem")
def create_item(item: Item):
    return {"item": item}
