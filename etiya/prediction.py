import json
import pickle
import numpy as np
from celery import Celery

MODEL_PATH = "model.pickle"

papp = Celery(
    "predict",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)


def load_model(path: str):
    with open(path,"rb") as f:
        return pickle.load(f)
    

def get_predictions(model,data):
    preds = model.predict_proba(data)
    return preds

@papp.task
def predict(input_data: text):
    model = load_model(MODEL_PATH)
    data = transform_data(input_data)
    preds = get_predictions(model,data)
    return preds