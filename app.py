from fastapi import FastAPI
from typing import Literal
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
            "region": "Flanders",
            "property_type": "HOUSE",
            "habitable_surface": 80,
            "number_of_rooms": 3,
            "has_terrace": True,
            "has_garden": False,
            "is_furnished": False,
            "has_swimming_pool": False,
            "has_open_fire": False,
        }


app = FastAPI()


@app.get("/")
async def status():
    return "alive"


how_to_dict = {
    "region": "Required, accepted values are: Brussels, Flanders and Wallonie",
    "property_type": "Required, accepted values are: APARTMENT and HOUSE",
    "habitable_surface": "Required, Integer",
    "number_of_rooms": "Required, Integer",
    "has_terrace": "Required, boolean",
    "has_garden": "Required, boolean",
    "is_furnished": "Required, boolean",
    "has_swimming_pool": "Required, boolean",
    "has_open_fire": "Required, boolean",
}


@app.get("/predict")
async def accepted_input_values_for_price_prediction_Post_route():
    """
    Demonstrates what are the accepted input values for the price prediction POST route.\n
    All fields are required.

    """
    return how_to_dict


@app.post("/predict")
async def predict_price_for_given_property(property: Property) -> dict:
    """
    Input values for a property using the given example schema.\n
    This will predict and return a sale price for the property.
    """
    prediction = predict(property)
    return {"prediction": prediction}
