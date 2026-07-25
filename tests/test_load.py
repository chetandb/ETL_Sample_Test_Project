import os
import pandas as pd
import pytest
from unittest.mock import patch

from load import load_data_to_db


def test_load_data_to_db_success(db_config):
    df = pd.DataFrame({"existing_column": [1, 2, 3], "new_column": [2, 4, 6]})
    # Return a real SQLite in-memory engine so pandas.to_sql uses a supported engine
    from sqlalchemy import create_engine as sa_create_engine

    with patch.dict(os.environ, {"DB_PASSWORD": "password"}), \
         patch("load.create_engine") as mock_create_engine:
        engine = sa_create_engine("sqlite:///:memory:")
        mock_create_engine.return_value = engine
        load_data_to_db(df, db_config)
        mock_create_engine.assert_called_once()


def test_load_data_to_db_empty(db_config):
    df = pd.DataFrame()
    with patch.dict(os.environ, {"DB_PASSWORD": "password"}), \
         patch("load.create_engine") as mock_create_engine:
        load_data_to_db(df, db_config)
        mock_create_engine.assert_not_called()


def test_load_data_to_db_missing_config():
    df = pd.DataFrame({"existing_column": [1]})
    bad_config = {"host": "localhost", "port": 5432}

    with patch.dict(os.environ, {"DB_PASSWORD": "password"}):
        with pytest.raises(ValueError, match="Database config is missing required keys"):
            load_data_to_db(df, bad_config)


def test_load_data_to_db_missing_password(db_config):
    df = pd.DataFrame({"existing_column": [1, 2, 3]})
    
    # Ensure DB_PASSWORD is not set
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="DB_PASSWORD environment variable is not set"):
            load_data_to_db(df, db_config)


def test_load_data_to_db_failure_disposes_engine(db_config):
    df = pd.DataFrame({"existing_column": [1, 2, 3]})
    from unittest.mock import MagicMock

    with patch.dict(os.environ, {"DB_PASSWORD": "password"}), \
         patch("load.create_engine") as mock_create_engine, \
         patch("pandas.DataFrame.to_sql", side_effect=Exception("Database Write Error")) as mock_to_sql:
        
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        with pytest.raises(Exception, match="Database Write Error"):
            load_data_to_db(df, db_config)

        # Verify that even when to_sql fails, engine.dispose() is called
        mock_engine.dispose.assert_called_once()


def test_load_data_to_db_missing_config_details():
    df = pd.DataFrame({"existing_column": [1]})
    # REQUIRED_CONFIG_KEYS = {"host", "port", "user", "dbname"}
    # We supply user and dbname; missing: host, port
    bad_config = {"user": "etl_user", "dbname": "etl_db"}

    # Expected sorted missing keys: ['host', 'port']
    expected_error_msg = "Database config is missing required keys: \\['host', 'port'\\]"
    
    with patch.dict(os.environ, {"DB_PASSWORD": "password"}):
        with pytest.raises(ValueError, match=expected_error_msg):
            load_data_to_db(df, bad_config)

