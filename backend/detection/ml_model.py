import os
import pickle
from config import settings

model = None
vectorizer = None

def load_model():
    global model, vectorizer

    if model is None or vectorizer is None:
        model_path = settings.MODEL_PATH

        if not os.path.exists(model_path):
            return None, None

        with open(model_path, "rb") as f:
            model, vectorizer = pickle.load(f)

    return model, vectorizer


def ml_detection(payload: str):
    model, vectorizer = load_model()

    if model is None or vectorizer is None:
        return "Benign"

    X = vectorizer.transform([payload])
    prediction = model.predict(X)[0]

    return prediction
