import numpy as np
import pandas as pd


def transform_data(
    df: pd.DataFrame,
    column_name: str = "existing_column",
    threshold: int = 25,
) -> pd.DataFrame:
    if column_name not in df.columns:
        raise ValueError(f"Missing required column: {column_name}")

    transformed_df = df.copy()
    transformed_df[column_name] = transformed_df[column_name].fillna(0)
    transformed_df["new_column"] = transformed_df[column_name] * 2
    transformed_df["status"] = np.where(
        transformed_df[column_name] > threshold,
        "High",
        "Low",
    )
    return transformed_df
