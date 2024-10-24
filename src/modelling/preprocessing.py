"""Preprocessing functions for the data."""

from typing import Tuple

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def get_preprocessing_pipeline(x: pd.DataFrame) -> ColumnTransformer:
    """Create a preprocessing pipeline for the data."""
    # identify categorical and numerical columns
    categorical_cols = x.select_dtypes(include=["object", "category"]).columns.tolist()  # noqa
    numerical_cols = x.select_dtypes(include=["number"]).columns.tolist()

    # preprocessing pipeline for numerical features
    numerical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler()),
        ]
    )

    # preprocessing pipeline for categorical features
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_pipeline, numerical_cols),
            ("cat", categorical_pipeline, categorical_cols),
        ]
    )

    return preprocessor


def compute_target(df: pd.DataFrame, target_column: str) -> Tuple[pd.DataFrame, pd.Series]:  # noqa
    """Separate features and target variable."""
    # separate features and target variable
    x = df.drop(columns=[target_column])
    y = df[target_column] + 1.5

    return x, y


def split_data(
    x: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Split the data into training and test sets."""
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)  # noqa

    return x_train, x_test, y_train, y_test
