from fastapi import FastAPI, HTTPException
from typing import Optional, Literal
from pydantic import BaseModel
from predict.prediction import predict

class Property(BaseModel):
    region: Literal["Brussels", "Flanders", "Wallonie"]
    property_type: Literal["APARTMENT", "HOUSE"]
    habitable_surface: int 
    number_of_rooms: int  
    has_terrace: bool  
    has_garden: bool 
    is_furnished: bool
    has_swimming_pool: bool
    has_open_fire: bool

    class Config:
        schema_extra = {
            "example": {
                "region": "Flanders",
                "property_type": "HOUSE",
                "habitable_surface": 65,
                "number_of_rooms": 2,
                "has_terrace" : "true",
                "has_garden" : "false",
                "is_furnished" : "false",
                "has_swimming_pool" : "false",
                "has_open_fire" : "false"
            }
        }

    
app = FastAPI()

@app.get("/")
def status():
    return "alive" 

how_to_dict = { 
    "region" : "Required, accepted values are: Brussels, Flanders and Wallonie",
    "property_type" : "Required, accepted values are: APARTMENT and HOUSE",
    "habitable_surface" : "Required, Integer",
    "number_of_rooms" : "Required, Integer",
    "has_terrace" : "Required, boolean",
    "has_garden" : "Required, boolean",
    "is_furnished" : "Required, boolean",
    "has_swimming_pool" : "Required, boolean",
    "has_open_fire" : "Required, boolean"
}

@app.get("/predict")
def how_to_use():
    return how_to_dict

@app.post("/predict")
def price_prediction(property: Property) -> dict:
    try:
        prediction = predict(property)
        return {"prediction" : prediction }
    except KeyError as e:
        raise HTTPException(status_code=500, detail=str(e))     
        

   







  