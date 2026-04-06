import pandas as pd
import numpy as np
from typing import Dict, Any

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Fill missing values in 'existing_column' with 0
    df['existing_column'] = df['existing_column'].fillna(0)

    # Add a 'new_column' which is double the existing column
    df['new_column'] = df['existing_column'] * 2

    # Add a 'status' column based on value thresholds (vectorized for performance)
    df['status'] = np.where(df['existing_column'] > 25, 'High', 'Low')

    return df
