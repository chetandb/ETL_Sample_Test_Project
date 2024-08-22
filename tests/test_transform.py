import pytest
import pandas as pd
from src.transform import transform_data

def test_transform_data_valid():
    df = pd.DataFrame({'existing_column': [10, 20, 30]})
    transformed_df = transform_data(df)

    assert 'new_column' in transformed_df.columns, "Transformation did not add new column"
    assert all(transformed_df['new_column'] == [20, 40, 60]), "Transformation logic is incorrect"

def test_transform_data_empty():
    df = pd.DataFrame({'existing_column': []})
    transformed_df = transform_data(df)

    assert transformed_df.empty, "Transformed DataFrame should be empty for empty input"

def test_transform_data_missing_column():
    df = pd.DataFrame({'different_column': [10, 20, 30]})

    with pytest.raises(KeyError):
        transform_data(df)
