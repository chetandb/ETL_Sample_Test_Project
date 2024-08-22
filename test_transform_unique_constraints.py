import pandas as pd

from transform import transform_data


def test_transform_data_unique_constraints():
    # Sample input data
    df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'existing_column': [10, 20, 30, 40, 50]
    })

    # Apply transformation
    transformed_df = transform_data(df)

    # Ensure 'id' column remains unique
    assert transformed_df['id'].is_unique, "ID column should remain unique after transformation"

    # Ensure no duplicate rows are introduced
    assert transformed_df.duplicated().sum() == 0, "No duplicate rows should be introduced"
