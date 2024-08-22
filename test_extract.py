from extract import extract_data

def test_extract_data():
    df = extract_data('./input_data.csv')
    assert not df.empty, "Extracted data should not be empty"
    assert 'existing_column' in df.columns, "Required column is missing"
