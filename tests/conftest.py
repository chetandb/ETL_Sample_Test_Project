from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture(scope="session")
def project_root() -> Path:
    return Path(__file__).resolve().parent.parent


@pytest.fixture
def csv_dir(project_root: Path) -> Path:
    return project_root / "csv"


@pytest.fixture
def sample_transform_df() -> pd.DataFrame:
    return pd.DataFrame({"existing_column": [10, 20, 30]})


@pytest.fixture
def db_config() -> dict:
    return {
        "host": "localhost",
        "port": 5432,
        "user": "etl_user",
        "password": "password",
        "dbname": "etl_db",
    }


@pytest.fixture
def empty_csv_file(tmp_path: Path) -> Path:
    empty_file = tmp_path / "empty_input.csv"
    empty_file.write_text("")
    return empty_file
