"""Load the data from Kaggle."""

import os

import opendatasets as od
import pandas as pd


def download_data(force: bool = False) -> str:
    """Download the data from Kaggle."""
    od.download("https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset", force=force)  # noqa
    data_folder = "abalone-dataset"
    return os.path.join(data_folder, "abalone.csv")


def load_data(path: str) -> pd.DataFrame:
    """Load the data from the given path."""
    return pd.read_csv(path)
