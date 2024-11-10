from typing import Union

from fastapi import FastAPI

app = FastAPI()

from fastapi.params import Query
from pydantic import BaseModel
class Order(BaseModel):
    order_id:str
    order_name:str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/order")
def process_order(order_name=Query(annotation=str)):
    new_order = Order(order_id="new",order_name=order_name)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}