from pathlib import Path

import pytest
from extract import extract_data


def test_extract_data(csv_dir: Path):
    df = extract_data(str(csv_dir / "input_data.csv"))
    assert not df.empty, "Extracted data should not be empty"
    assert "existing_column" in df.columns, "Required column is missing"


def test_extract_data_invalid_file(csv_dir: Path):
    with pytest.raises(FileNotFoundError):
        extract_data(str(csv_dir / "non_existent_file.csv"))


def test_extract_data_empty_file(empty_csv_file: Path):
    df = extract_data(str(empty_csv_file))
    assert df.empty, "Extracted data should be empty for an empty file"
