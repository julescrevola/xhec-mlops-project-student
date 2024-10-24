import os
import opendatasets as od
import pandas as pd

def download_data(force: bool = False) -> str:
    od.download("https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset", force=force)
    data_folder = "abalone-dataset"
    return os.path.join(data_folder, "abalone.csv")


def load_data(PATH: str) -> pd.DataFrame:
    return pd.read_csv(PATH)