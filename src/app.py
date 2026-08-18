from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="MLOps Iris API")

# Loading the trained model
model = joblib.load('model.pkl')

class IrisData(BaseModel):
    sepal_length: float
    speal_width: float
    petal_length: float
    petal_width: float
    
@app.get("/")
def home():
    return {"message": "Welcome to the ML Model API. Go to /docs to test it out."}

@app.post("/predict")
def predict(data: IrisData):
    # Convertin input to numpy array
    features = np.array([data.sepal_length, data.sepal_width, data.petal_length, data.petal_width])
    prediction = model.predict(features)
    return {"predictions": int(prediction[0])}