from fastapi import APIRouter
import joblib
import pandas as pd

from src.api.schemas.predict import (
    HeartDiseaseRequest,
    PredictionResponse,
)

router = APIRouter()

# Load trained model and scaler
model = joblib.load("models/random_forest_model.pkl")
scaler = joblib.load("models/scaler.pkl")


@router.post("/predict", response_model=PredictionResponse)
def predict(request: HeartDiseaseRequest):

    # Convert request into DataFrame
    input_data = pd.DataFrame([request.model_dump()])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    label = "Disease" if prediction == 1 else "No Disease"

    return PredictionResponse(
        prediction=int(prediction),
        prediction_label=label,
    )