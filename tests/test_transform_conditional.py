import pandas as pd
from src.transform import transform_data

def test_transform_data_conditional_logic():
    # Sample input data
    df = pd.DataFrame({'existing_column': [5, 15, 25, 35, 45]})

    # Apply transformation
    transformed_df = transform_data(df)

    # Example: If value in existing_column > 20, new_column should be 'High', otherwise 'Low'
    assert 'new_column' in transformed_df.columns, "new_column is missing after transformation"

    # Expected new_column based on the example logic
    expected_new_column = [10, 30, 50, 70, 90]
    assert list(transformed_df['new_column']) == expected_new_column, "Conditional logic in transformation is incorrect"
