import pandas as pd

from transform import transform_data


def test_transform_data_with_missing_values():
    # Sample data with missing values
    df = pd.DataFrame({'existing_column': [10, None, 30, None, 50]})

    # Apply transformation
    transformed_df = transform_data(df)

    # Example: Check if missing values are filled with 0 (depending on your transformation logic)
    assert transformed_df['existing_column'].isna().sum() == 0, "Missing values should be handled"

    # Example: Check if new_column is correctly calculated even with missing values
    assert 'new_column' in transformed_df.columns, "Transformation should add new_column"
    assert all(transformed_df['new_column'].fillna(0) == df['existing_column'].fillna(0) * 2), "Transformation logic is incorrect"
