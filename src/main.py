from fastapi import FastAPI

from src.api.routes.predict import router as predict_router

app = FastAPI(
    title="Heart Disease Prediction API",
    description="MLOps Assignment - Heart Disease Prediction using Random Forest",
    version="1.0.0",
)

app.include_router(predict_router)


@app.get("/")
def home():
    return {
        "message": "Heart Disease Prediction API is running successfully!"
    }