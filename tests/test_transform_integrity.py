import pandas as pd
from transform import transform_data

def test_transform_data_integrity():
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "existing_column": [10, 20, 30],
    })

    transformed_df = transform_data(df.copy())

    assert transformed_df["id"].is_unique, "ID column should remain unique after transformation"
    assert len(transformed_df) == len(df), "Row count should remain unchanged"
    assert transformed_df["id"].tolist() == df["id"].tolist(), "ID values should remain unchanged"
    assert transformed_df.duplicated().sum() == 0, "No duplicate rows should be introduced"
    assert "new_column" in transformed_df.columns, "Transformation should add new_column"
