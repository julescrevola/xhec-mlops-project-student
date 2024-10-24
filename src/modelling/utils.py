from typing import Any 

import pickle

def pickle_obj(obj, filepath: str) -> None:
    with open(filepath, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(filepath: str):
    with open(filepath, "rb") as f:
        model = pickle.load(f)
    return model
