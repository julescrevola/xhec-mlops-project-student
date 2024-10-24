"""Run predictions using the fitted Random Forest regression model."""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def predict(model: RandomForestRegressor, x_new: pd.DataFrame) -> pd.Series:
    """Make predictions using the fitted Random Forest regression model.

    Parameters:
    ----------
    model : RandomForestRegressor
        The fitted Random Forest regression model.
    x_new : pd.DataFrame
        The new feature data for which predictions are to be made.

    Returns:
    -------
    pd.Series
        The predicted values for the new data.
    """
    return model.predict(x_new)


def evaluate_rmse(y_true: pd.Series, y_pred: pd.Series) -> float:
    """
    Evaluate the performance of the model using Root Mean Squared Error (RMSE).

    Parameters:
    ----------
    y_true : pd.Series
        The true values of the target variable.
    y_pred : pd.Series
        The predicted values from the model.

    Returns:
    -------
    float
        The RMSE value.
    """
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return rmse
