import pandas as pd
from transform import transform_data

def test_missing_values_transformation():
    df = pd.DataFrame({"existing_column": [10, None, 30, None, 50]})
    transformed_df = transform_data(df)

    assert transformed_df["existing_column"].isna().sum() == 0, "Missing values should be handled"
    assert "new_column" in transformed_df.columns, "Transformation should add new_column"
    expected_new_column = [20, 0, 60, 0, 100]
    assert all(transformed_df["new_column"] == expected_new_column), "Transformation logic is incorrect"
