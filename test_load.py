import pytest
import pandas as pd
from load import load_data_to_db
from unittest.mock import patch

@pytest.fixture
def config():
    return {
        'host': 'localhost',
        'port': 5432,
        'user': 'etl_user',
        'password': 'password',
        'dbname': 'etl_db'
    }

def test_load_data_to_db_success(config, mocker):
    df = pd.DataFrame({'existing_column': [1, 2, 3], 'new_column': [2, 4, 6]})

    with patch('load.create_engine') as mock_create_engine:
        load_data_to_db(df, config)
        mock_create_engine.assert_called_once()

def test_load_data_to_db_empty(config, mocker):
    df = pd.DataFrame()

    with patch('load.create_engine') as mock_create_engine:
        load_data_to_db(df, config)
        mock_create_engine.assert_called_once()
