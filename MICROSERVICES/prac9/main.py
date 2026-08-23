from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np


# ---------------------------------------
# CREATE FASTAPI APP
# ---------------------------------------

app = FastAPI(
    title="AI Data Service",
    description="Campus Transaction AI Prediction Service",
    version="1.0"
)


# ---------------------------------------
# SIMPLE AI MODEL
# ---------------------------------------

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(3,)),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(4, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])


# ---------------------------------------
# INPUT DATA FORMAT
# ---------------------------------------

class PredictionInput(BaseModel):
    Total_Money_Spent: float
    Total_Transactions: int
    Average_Transaction: float


# ---------------------------------------
# HOME ROUTE
# ---------------------------------------

@app.get("/")
def home():

    return {
        "message": "AI Data Service is running"
    }


# ---------------------------------------
# PREDICTION ROUTE
# ---------------------------------------

@app.post("/predict")
def predict(data: PredictionInput):

    # Convert incoming data into NumPy array
    input_data = np.array([
        [
            data.Total_Money_Spent,
            data.Total_Transactions,
            data.Average_Transaction
        ]
    ], dtype=np.float32)


    # Send data through TensorFlow model
    prediction_result = model.predict(
        input_data,
        verbose=0
    )


    # Get prediction score
    # Sigmoid gives a value between 0 and 1
    score = float(prediction_result[0][0])


    # Convert score into prediction
    if score >= 0.7:
        prediction = "High"

    elif score >= 0.4:
        prediction = "Medium"

    else:
        prediction = "Low"


    # Return prediction response
    return {
        "prediction_score": round(score, 4),
        "prediction": prediction
    }