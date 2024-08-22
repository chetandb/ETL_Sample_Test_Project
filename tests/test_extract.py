import pytest
from src.extract import extract_data

def test_extract_data():
    df = extract_data('../csv/input_data.csv')
    assert not df.empty, "Extracted data should not be empty"
    assert 'existing_column' in df.columns, "Required column is missing"

def test_extract_data_valid_file():
    df = extract_data('../csv/input_data.csv')
    assert not df.empty, "Extracted data should not be empty"
    assert 'existing_column' in df.columns, "Required column is missing"

def test_extract_data_invalid_file():
    with pytest.raises(FileNotFoundError):
        extract_data('./non_existent_file.csv')

def test_extract_data_empty_file():
    with open('../csv/empty_input.csv', 'w') as f:
        f.write("")

    df = extract_data('../csv/empty_input.csv')
    assert df.empty, "Extracted data should be empty for an empty file"
