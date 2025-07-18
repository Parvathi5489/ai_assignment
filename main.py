from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class StoreData(BaseModel):
    date: str
    total_sales: float
    visitors: int
    conversion_rate: float
    top_product: str

@app.get("/insights")
def get_insights(date: Optional[str] = None):
    try:
        with open("users.json", "r") as f:
            data = json.load(f)
        if date:
            result = [item for item in data if item["date"] == date]
            if not result:
                raise HTTPException(status_code=404, detail="Data not found for given date")
            return result[0]
        return data[-1]
    except Exception:
        raise HTTPException(status_code=500, detail="Error reading data")

@app.post("/insights")
def add_insight(new_data: StoreData):
    try:
        with open("users.json", "r") as f:
            data = json.load(f)
        data.append(new_data.dict())
        with open("users.json", "w") as f:
            json.dump(data, f)
        return {"message": "Insight added successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to add insight")
