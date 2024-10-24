import os
from pathlib import Path
from typing import Optional

from load_data import download_data, load_data
from loguru import logger
from predicting import evaluate_rmse, predict
from prefect import flow
from preprocessing import compute_target, get_preprocessing_pipeline, split_data  # noqa
from training import fit_random_forest
from utils import save_pickle


@flow(name="Train model")
def train_model_workflow(
    trainset_path: Path,
    artifacts_filepath: Optional[str] = None,
) -> dict:
    """Train a model using the data at the given path."""
    logger.info("Load data...")
    df = load_data(trainset_path)
    logger.info("Compute target variable...")
    x, y = compute_target(df, target_column="Rings")
    logger.info("Retrieving preprocessor...")
    preprocessor = get_preprocessing_pipeline(x)
    logger.info("Split into train/test...")
    x_train, x_test, y_train, y_test = split_data(x, y)
    logger.info("Process train/test data...")
    x_train_preprocessed = preprocessor.fit_transform(x_train)
    x_test_preprocessed = preprocessor.transform(x_test)
    logger.info("Train model...")
    model = fit_random_forest(x_train_preprocessed, y_train)
    logger.info("Making predictions and evaluating...")
    y_pred = predict(model, x_test_preprocessed)
    rmse = evaluate_rmse(y_test, y_pred)

    if artifacts_filepath is not None:
        logger.info(f"Saving artifacts to {artifacts_filepath}...")
        save_pickle(os.path.join(artifacts_filepath, "preprocessor.pkl"), preprocessor)  # noqa
        save_pickle(os.path.join(artifacts_filepath, "random_forest.pkl"), model)  # noqa

    return {"model": model, "preprocessor": preprocessor, "rmse": rmse}  # noqa


if __name__ == "__main__":
    data_folder = "abalone-dataset"
    csv_file = os.path.join(data_folder, "abalone.csv")

    # Check if the data file exists, download if it doesn't
    if not os.path.exists(csv_file):
        download_data(force=False)
    train_model_workflow(trainset_path=Path(csv_file), artifacts_filepath="../web_service")  # noqa
