from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Rectangle(BaseModel):
    width: float
    length: float

@app.post("/calculate-area/")
def calculate_area(rect: Rectangle):
    area = rect.width * rect.length
    return {"width": rect.width, "length": rect.length, "area": area}
