# deployment_agent.py
from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import logging

# Initialize FastAPI app
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
def load_model():
    global model
    try:
        model = joblib.load('model.pkl')
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise HTTPException(status_code=500, detail="Model could not be loaded")

@app.post("/predict")
async def predict(features: dict):
    try:
        features_df = pd.DataFrame([features])
        prediction = model.predict(features_df)
        return {"prediction": prediction[0]}
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=400, detail="Invalid input or prediction error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)