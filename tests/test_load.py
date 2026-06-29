import pandas as pd
import pytest
from unittest.mock import patch

from load import load_data_to_db


def test_load_data_to_db_success(db_config):
    df = pd.DataFrame({"existing_column": [1, 2, 3], "new_column": [2, 4, 6]})
    with patch("load.create_engine") as mock_create_engine:
        load_data_to_db(df, db_config)
        mock_create_engine.assert_called_once()


def test_load_data_to_db_empty(db_config):
    df = pd.DataFrame()
    with patch("load.create_engine") as mock_create_engine:
        load_data_to_db(df, db_config)
        mock_create_engine.assert_not_called()


def test_load_data_to_db_missing_config():
    df = pd.DataFrame({"existing_column": [1]})
    bad_config = {"host": "localhost", "port": 5432}

    with pytest.raises(ValueError, match="Database config is missing required keys"):
        load_data_to_db(df, bad_config)
