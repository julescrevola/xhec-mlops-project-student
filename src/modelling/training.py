"""Functions for training machine learning models."""
import pandas as pd
from prefect import task
from sklearn.ensemble import RandomForestRegressor


@task(name="Train model")
def fit_random_forest(
    x_train: pd.DataFrame,
    y_train: pd.Series,
    n_estimators: int = 100,
    random_state: int = 42,
) -> RandomForestRegressor:
    """
    Fit a Random Forest regression model to the training data.

    Parameters:
    ----------
    x_train : pd.DataFrame
        The training feature DataFrame.
    y_train : pd.Series
        The training target variable.
    n_estimators : int, optional
        The number of trees in the forest. Default is 100.
    random_state : int, optional
        Random seed for reproducibility. Default is 42.

    Returns:
    -------
    RandomForestRegressor
        The fitted Random Forest regression model.
    """
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)  # noqa
    model.fit(x_train, y_train)

    return model
