import pandas as pd
from src.transform import transform_data

def test_transform_data_complex_logic():
    # Sample input data
    df = pd.DataFrame({'existing_column': [10, 20, 30, 40, 50]})

    # Apply transformation
    transformed_df = transform_data(df)

    # Check if 'new_column' is double the existing column
    assert 'new_column' in transformed_df.columns, "new_column is missing after transformation"
    assert all(transformed_df['new_column'] == df['existing_column'] * 2), "new_column values are incorrect"

    # Check if 'status' column is correctly generated
    assert 'status' in transformed_df.columns, "status column is missing after transformation"
    expected_status = ['Low', 'Low', 'High', 'High', 'High']
    assert list(transformed_df['status']) == expected_status, "status column values are incorrect"
