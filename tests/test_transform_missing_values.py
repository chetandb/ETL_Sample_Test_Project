import pandas as pd
from src.transform import transform_data

def test_transform_data_with_missing_values():
    # Sample data with missing values
    df = pd.DataFrame({'existing_column': [10, None, 30, None, 50]})

    # Apply transformation
    transformed_df = transform_data(df)

    # Check if missing values are filled with 0
    assert transformed_df['existing_column'].isna().sum() == 0, "Missing values should be handled"

    # Check if new_column is correctly calculated
    assert 'new_column' in transformed_df.columns, "Transformation should add new_column"
    expected_new_column = [20, 0, 60, 0, 100]
    assert all(transformed_df['new_column'] == expected_new_column), "Transformation logic is incorrect"
