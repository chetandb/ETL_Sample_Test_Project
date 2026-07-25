import pandas as pd
import pytest

from transform import transform_data


def test_transform_data_valid():
    df = pd.DataFrame({"existing_column": [10, 20, 30]})
    transformed_df = transform_data(df)

    assert "new_column" in transformed_df.columns, "Transformation did not add new column"
    assert all(transformed_df["new_column"] == [20, 40, 60]), "Transformation logic is incorrect"
    assert all(transformed_df["status"] == ["Low", "Low", "High"]), "Status values are incorrect"


def test_transform_data_empty():
    df = pd.DataFrame({"existing_column": []})
    transformed_df = transform_data(df)

    assert transformed_df.empty, "Transformed DataFrame should be empty for empty input"


def test_transform_data_missing_column():
    df = pd.DataFrame({"different_column": [10, 20, 30]})

    with pytest.raises(ValueError, match="Missing required column"):
        transform_data(df)


def test_transform_data_boundary_values():
    # threshold is 25 by default.
    # 24 -> Low, 25 -> Low (since condition is > threshold), 26 -> High
    df = pd.DataFrame({"existing_column": [24, 25, 26]})
    transformed_df = transform_data(df)
    assert list(transformed_df["status"]) == ["Low", "Low", "High"], "Boundary values status check failed"


def test_transform_data_custom_arguments():
    # Use custom column and threshold
    df = pd.DataFrame({"custom_col": [5, 10, 15]})
    transformed_df = transform_data(df, column_name="custom_col", threshold=10)
    
    assert "new_column" in transformed_df.columns
    # 5 * 2 = 10, 10 * 2 = 20, 15 * 2 = 30
    assert list(transformed_df["new_column"]) == [10, 20, 30]
    # threshold is 10. 5 > 10 (False -> Low), 10 > 10 (False -> Low), 15 > 10 (True -> High)
    assert list(transformed_df["status"]) == ["Low", "Low", "High"]


def test_transform_data_non_numeric():
    df = pd.DataFrame({"existing_column": ["a", "b", "c"]})
    # Comparing strings with integer threshold (e.g. "a" > 25) will raise TypeError
    with pytest.raises(TypeError):
        transform_data(df)


def test_transform_data_all_nulls():
    df = pd.DataFrame({"existing_column": [None, None, None]})
    transformed_df = transform_data(df)
    # Nulls filled with 0. 0 * 2 = 0. status should be "Low" since 0 <= 25.
    assert list(transformed_df["existing_column"]) == [0, 0, 0]
    assert list(transformed_df["new_column"]) == [0, 0, 0]
    assert list(transformed_df["status"]) == ["Low", "Low", "Low"]

