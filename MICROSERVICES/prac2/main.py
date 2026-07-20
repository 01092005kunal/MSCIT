from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage
water_data = []

class WaterIntake(BaseModel):
    date: str
    amount_liters: float

# Add water intake record
@app.post("/water/")
def add_water_intake(record: WaterIntake):
    water_data.append(record)
    return {"message": "Water intake logged successfully"}

# Get all water intake records
@app.get("/water/", response_model=List[WaterIntake])
def get_water_intake():
    return water_data

