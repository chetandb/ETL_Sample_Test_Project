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


def test_extract_data_whitespace_only_csv(tmp_path: Path):
    whitespace_file = tmp_path / "whitespace.csv"
    whitespace_file.write_text("   \n   \n")
    # This file has size > 0 but contains no valid CSV data
    df = extract_data(str(whitespace_file))
    assert df.empty, "DataFrame should be empty for whitespace-only file"


def test_extract_data_malformed_csv(tmp_path: Path):
    malformed_file = tmp_path / "malformed.csv"
    # Row 2 has more elements than headers, causing ParserError
    malformed_file.write_text("col1,col2\n1,2\n3,4,5\n")
    import pandas as pd
    with pytest.raises(pd.errors.ParserError):
        extract_data(str(malformed_file))


def test_extract_data_path_input(csv_dir: Path):
    # Pass Path object instead of string
    path_obj = csv_dir / "input_data.csv"
    df = extract_data(path_obj)
    assert not df.empty, "Extracted data should not be empty when using Path input"
    assert "existing_column" in df.columns, "Required column is missing"

