import joblib
import pandas as pd


def test_model_prediction():

    model = joblib.load("models/random_forest_model.pkl")
    scaler = joblib.load("models/scaler.pkl")

    sample = pd.DataFrame([{
        "age": 63,
        "sex": 1,
        "cp": 3,
        "trestbps": 145,
        "chol": 233,
        "fbs": 1,
        "restecg": 0,
        "thalach": 150,
        "exang": 0,
        "oldpeak": 2.3,
        "slope": 0,
        "ca": 0,
        "thal": 1
    }])

    sample_scaled = scaler.transform(sample)

    prediction = model.predict(sample_scaled)

    assert prediction[0] in [0, 1]