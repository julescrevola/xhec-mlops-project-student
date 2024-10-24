from pathlib import Path
from load_data import download_data, load_data
from preprocessing import get_preprocessing_pipeline, compute_target, split_data
from training import fit_random_forest
from utils import pickle_obj

import argparse

path = download_data()

def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Read data
    df = load_data(trainset_path)

    # Preprocess data
    preprocessor = get_preprocessing_pipeline(df)
    X, y = compute_target(df, target_column="Rings")
    X_train, X_test, y_train, y_test = split_data(X, y)

    X_train_preprocessed = preprocessor.fit_transform(X_train)
    X_test_preprocessed = preprocessor.transform(X_test)

    # Pickle encoder
    pickle_obj(obj=preprocessor, filepath="web_service/local_objects/preprocessor.pkl")

    # Train model
    model = fit_random_forest(X_train_preprocessed, y_train)

    # Pickle model --> The model should be saved in pkl format the `src/web_service/local_objects` folder
    pickle_obj(obj=model, filepath="web_service/local_objects/preprocessor.pkl")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
