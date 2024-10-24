import pandas as pd 
from sklearn.ensemble import RandomForestRegressor

def fit_random_forest(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    n_estimators: int = 100,
    random_state: int = 42,
) -> RandomForestRegressor:
    """
    Fit a Random Forest regression model to the training data.

    Parameters:
    ----------
    X_train : pd.DataFrame
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

    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)

    return model