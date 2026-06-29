import pandas as pd
from transform import transform_data

def test_transform_data_complex_logic():
    df = pd.DataFrame({"existing_column": [10, 20, 30, 40, 50]})

    transformed_df = transform_data(df)

    assert "new_column" in transformed_df.columns, "new_column is missing after transformation"
    assert all(transformed_df["new_column"] == df["existing_column"] * 2), "new_column values are incorrect"

    assert "status" in transformed_df.columns, "status column is missing after transformation"
    expected_status = ["Low", "Low", "High", "High", "High"]
    assert list(transformed_df["status"]) == expected_status, "status column values are incorrect"
