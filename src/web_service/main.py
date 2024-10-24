"""FastAPI web service for predicting the age of abalones."""

import pickle

import pandas as pd
from fastapi import FastAPI, HTTPException
from lib.inference import predict
from lib.models import AbaloneData
from lib.preprocessing import (  # noqa
    compute_target,
    fit_random_forest,
    get_preprocessing_pipeline,
    split_data,
)

app = FastAPI()

# Load the pre-trained model and preprocessor using pickle
with open("local_objects/random_forest.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("local_objects/preprocessor.pkl", "rb") as preprocessor_file:
    preprocessor = pickle.load(preprocessor_file)


@app.get("/")
def home() -> dict:
    """Health check endpoint."""
    return {"health_check": "App up and running!"}


@app.post("/retrain")
async def retrain():
    """Train the Random Forest regression model."""
    try:
        # Load the dataset
        df = pd.read_csv("abalone-dataset/abalone.csv")

        # Preprocess the data
        x, y = compute_target(df, "Rings")

        x_train, x_test, y_train, y_test = split_data(x, y)
        preprocessor = get_preprocessing_pipeline(x_train)

        x_train = preprocessor.fit_transform(x_train)

        # Save the preprocessor
        with open("local_objects/preprocessor.pkl", "wb") as preprocessor_file:
            pickle.dump(preprocessor, preprocessor_file)

        # Train the model
        model = fit_random_forest(x_train, y_train)

        # Save the model
        with open("local_objects/random_forest.pkl", "wb") as model_file:
            pickle.dump(model, model_file)

        return {"message": "Model retrained and saved successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/predict")
async def make_prediction(data: AbaloneData):
    """Make predictions using the Random Forest regression model."""
    try:
        # Convert input data to a DataFrame
        input_data = pd.DataFrame([data.dict()])

        input_data.columns = [i.replace("_", " ") for i in input_data.columns]
        print(f"Input data: {input_data}")

        # log the input data
        # print(f"Input data: {input_data}")
        # print(f'Preprocessor: {preprocessor}')
        # Preprocess the input data
        input_data_preprocessed = preprocessor.transform(input_data)
        print(f"Preprocessed data: {input_data_preprocessed}")
        # Make prediction
        prediction = predict(model, input_data_preprocessed)

        return {"predicted_age": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
