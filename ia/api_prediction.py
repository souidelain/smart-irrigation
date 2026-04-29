from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
    moisture: float
    temperature: float

@app.post("/predict")
def predict_irrigation(data: SensorData):
    # Logic simple: Ila moisture < 30% w hrara > 25°C -> S9i (ON)
    if data.moisture < 35.0:
        decision = "ON"
        reason = "Soil is too dry"
    else:
        decision = "OFF"
        reason = "Moisture level is sufficient"
    
    return {"pump_action": decision, "reason": reason}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)