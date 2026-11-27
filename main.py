""" Base de nuestra API, primer endpoint """
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    edad:int

app = FastAPI()

""" Primer endpoint """

@app.get('/')

async def read_root(): 
    return {"message": "Hello World!"}


""" Segundo endpoint """
@app.post('/items')
async def create_item(item: Item):
    return {'item': {'name': item.name, 'edad': item.edad}}

