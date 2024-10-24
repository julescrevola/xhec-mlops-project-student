"""Utility functions for the modelling module."""

import pickle
from typing import Any

from prefect import task


@task(name="Create pickle")
def pickle_obj(obj, filepath: str) -> None:
    """Pickle an object to a file."""
    with open(filepath, "wb") as f:
        pickle.dump(obj, f)


@task(name="Save pickle")
def save_pickle(path: str, obj: Any):
    with open(path, "wb") as f:
        pickle.dump(obj, f)


@task(name="Save pickle")
def load_pickle(filepath: str):
    """Load a pickled object from a file."""
    with open(filepath, "rb") as f:
        model = pickle.load(f)
    return model
