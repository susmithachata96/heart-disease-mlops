from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.middleware.logging_middleware import LoggingMiddleware
from src.api.routes.predict import router as predict_router
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="Heart Disease Prediction API",
    description="""
A production-ready FastAPI application for predicting the likelihood
of heart disease using a trained Machine Learning model.

Features:
- Heart Disease Prediction
- Interactive Swagger Documentation
- Health Check Endpoint
- Docker Support
- Kubernetes Deployment
- CI/CD using GitHub Actions
- Prometheus Monitoring
- Grafana Dashboard
""",
    version="1.1.0",
    contact={
        "name": "Susmitha Chatakondu",
        "url": "https://github.com/susmithachata96",
    },
    license_info={
        "name": "MIT License",
    },
)
app.add_middleware(LoggingMiddleware)
Instrumentator().instrument(app).expose(app)
app.include_router(predict_router, tags=["Prediction"])


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Heart Disease Prediction API is running successfully!",
        "version": "1.1.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["Health"])
def health():
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "Heart Disease Prediction API",
            "version": "1.1.0",
        },
    )
