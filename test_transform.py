import pytest
import pandas as pd
from transform import transform_data

def test_transform_data():
    df = pd.DataFrame({'existing_column': [1, 2, 3]})
    transformed_df = transform_data(df)

    assert 'new_column' in transformed_df.columns, "Transformation did not add new column"
    assert all(transformed_df['new_column'] == [2, 4, 6]), "Transformation logic is incorrect"
