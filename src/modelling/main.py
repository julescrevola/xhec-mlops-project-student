"""Main module to run whole model."""
import argparse
import os
from pathlib import Path

from load_data import download_data, load_data
from predicting import evaluate_rmse, predict
from preprocessing import compute_target, get_preprocessing_pipeline, split_data  # noqa
from training import fit_random_forest
from utils import pickle_obj


def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path."""
    # Read data
    df = load_data(trainset_path)

    # Preprocess data
    x, y = compute_target(df, target_column="Rings")
    preprocessor = get_preprocessing_pipeline(x)

    x_train, x_test, y_train, y_test = split_data(x, y)
    x_train_preprocessed = preprocessor.fit_transform(x_train)
    x_test_preprocessed = preprocessor.transform(x_test)

    # Pickle encoder
    pickle_obj(obj=preprocessor, filepath="../web_service/local_objects/preprocessor.pkl")  # noqa

    # Train model
    model = fit_random_forest(x_train_preprocessed, y_train)

    pickle_obj(obj=model, filepath="../web_service/local_objects/random_forest.pkl")  # noqa

    # Predict
    y_pred = predict(model, x_test_preprocessed)

    # Compute RMSE and display it
    rmse = evaluate_rmse(y_test, y_pred)

    print(f"The RandomForest predicted age with an RMSE of {rmse}.")


if __name__ == "__main__":
    data_folder = "abalone-dataset"
    csv_file = os.path.join(data_folder, "abalone.csv")

    # Check if the data file exists, download if it doesn't
    if not os.path.exists(csv_file):
        download_data(force=False)
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")  # noqa
    parser.add_argument(
        "trainset_path",
        type=str,
        nargs="?",
        default="abalone-dataset/abalone.csv",
        help="Path to the training set",  # noqa
    )
    args = parser.parse_args()
    main(trainset_path=args.trainset_path)
