import pandas as pd
from transform import transform_data
import pandas as pd

from transform import transform_data


def test_transform_data_integrity():
    # Sample input data
    input_data = {'existing_column': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(input_data)

    # Apply transformation
    transformed_df = transform_data(df)

    # Ensure row count remains the same
    assert len(df) == len(transformed_df), "Row count should not change after transformation"
