import os
import pytest

# Ensure src directory is in PYTHONPATH
os.environ['PYTHONPATH'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Add src directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from extract import extract_data
from transform import transform_data


def run_etl():
    # Paths to the data files
    input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../csv/input_data.csv'))
    transformed_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'transformed_data.csv'))

    # 1. Extract Data
    print("Starting Data Extraction...")
    df = extract_data(input_data_path)
    print("Data Extraction Complete.")

    # 2. Transform Data
    print("Starting Data Transformation...")
    transformed_df = transform_data(df)
    transformed_df.to_csv(transformed_data_path, index=False)
    print("Data Transformation Complete.")

    # 3. Load Data (Mocked)
    print("Starting Data Loading...")
    # Mock the DB load step so no real connection is made
    try:
        from unittest.mock import patch
        with patch('src.load.create_engine') as mock_create_engine:
            mock_create_engine.return_value = None
            # If you want to call load_data_to_db, it will use the mock
            # from src.load import load_data_to_db
            # config = {...}  # Provide config if needed
            # load_data_to_db(transformed_df, config)
    except ImportError:
        print("unittest.mock not available, skipping DB mock.")
    print("Data Loading Complete.")


def clean_up():
    # Remove generated files
    transformed_data_path = './transformed_data.csv'
    if os.path.exists(transformed_data_path):
        os.remove(transformed_data_path)
    print("Clean up complete.")


def run_tests():
    print("Starting Tests...")
    print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
    test_files = [
        "../tests/test_extract.py",
        "../tests/test_transform.py",
        "../tests/test_load.py",
        "../tests/test_transform_complex.py",
        "../tests/test_transform_conditional.py",
        "../tests/test_transform_integrity.py",
        "../tests/test_transform_missing_values.py",
        "../tests/test_transform_unique_constraints.py"
    ]
    print("Resolved test file paths:", test_files)
    pytest_args = ["-v", "--disable-warnings"] + test_files
    pytest.main(pytest_args)
    print("Tests Complete.")


if __name__ == "__main__":
    try:
        # Run the ETL process
        # run_etl()  # Temporarily skip the ETL process

        # Run the tests
        run_tests()
    finally:
        # Clean up generated files after testing
        clean_up()
