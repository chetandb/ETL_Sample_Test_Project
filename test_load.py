import pytest
import pandas as pd

import load
from load import load_data_to_db

@pytest.fixture
def config():
    return {
        'host': 'localhost',
        'port': 5432,
        'user': 'etl_user',
        'password': 'password',
        'dbname': 'etl_db'
    }

def test_load_data_to_db(config, mocker):
    mocker.patch('load.create_engine')
    df = pd.DataFrame({'existing_column': [1, 2, 3]})
    load_data_to_db(df, config)

    # Assuming load_data_to_db has proper logging
    # Here, we mock and verify if the SQLAlchemy's engine.connect was called.
    load.create_engine.assert_called_once()
