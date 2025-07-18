import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pandas as pd
from transform import transform_data

def test_conditional_transformation():
    # Sample input data
    df = pd.DataFrame({'existing_column': [5, 15, 25, 35, 45]})
    transformed_df = transform_data(df)
    # Example: If value in existing_column > 20, new_column should be 'High', otherwise 'Low'
    expected_new_column = [10, 30, 50, 70, 90]
    assert list(transformed_df['new_column']) == expected_new_column, "Conditional logic in transformation is incorrect"
