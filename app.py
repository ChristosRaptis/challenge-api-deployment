from fastapi import FastAPI
from typing import Optional, Literal
from pydantic import BaseModel

class Item(BaseModel):
    area: int
    property_type: Literal["APARTMENT", "HOUSE", "OTHERS"]
    rooms_number: int
    zip_code: int
    land_area: Optional[int] 
    garden: Optional[bool] 
    garden_area: Optional[int] 
    equipped_kitchen: Optional[bool] 
    full_address: Optional[str]
    swimming_pool: Optional[bool] 
    furnished: Optional[bool] 
    open_fire: Optional[bool] 
    terrace: Optional[bool] 
    terrace_area: Optional[int] 
  
app = FastAPI()

@app.get("/")
def server_alive():
    return "alive" 

@app.post("/predict")
def property_data(item: Item):
    return item

@app.get("/predict")
def data_required():
    return {"data required and their format" : str(dict)}


dict ={
    'area': 'int',
    'property_type': 'APARTMENT or HOUSE or OTHERS',
    'rooms_number': 'int',
    'zip_code': 'int',
    'land_area': 'Optional[int]',
    'garden': 'Optional[bool]',
    'garden_area': 'Optional[int]',
    'equipped_kitchen': 'Optional[bool]',
    'full_address': 'Optional[str]',
    'swimming_pool': 'Optional[bool]',
    'furnished': 'Optional[bool]',
    'open_fire': 'Optional[bool]',
    'terrace': 'Optional[bool]',
    'terrace_area': 'Optional[int]',
     
}