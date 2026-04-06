import os
import sys
import pytest
from pathlib import Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from extract import extract_data
from transform import transform_data


def run_etl():
    # Use pathlib for better path handling
    base_dir = Path(__file__).parent.parent
    input_data_path = base_dir / 'csv' / 'input_data.csv'
    transformed_data_path = base_dir / 'tests' / 'transformed_data.csv'

    # 1. Extract Data
    print("Starting Data Extraction...")
    df = extract_data(str(input_data_path))
    print(f"Data Extraction Complete. Extracted {len(df)} rows.")

    # 2. Transform Data
    print("Starting Data Transformation...")
    transformed_df = transform_data(df)
    transformed_df.to_csv(transformed_data_path, index=False)
    print(f"Data Transformation Complete. Transformed {len(transformed_df)} rows.")

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
    # Remove generated files using pathlib
    base_dir = Path(__file__).parent.parent
    transformed_data_path = base_dir / 'tests' / 'transformed_data.csv'
    if transformed_data_path.exists():
        transformed_data_path.unlink()
    print("Clean up complete.")


def run_tests():
    print("Starting Tests...")
    test_files = [
        "tests/test_extract.py",
        "tests/test_transform.py",
        "tests/test_load.py",
        "tests/test_transform_complex.py",
        "tests/test_transform_conditional.py",
        "tests/test_transform_integrity.py",
        "tests/test_transform_missing_values.py",
        "tests/test_transform_unique_constraints.py"
    ]
    # Create reports directory if it doesn't exist
    import os
    os.makedirs("reports", exist_ok=True)
    
    pytest_args = [
        "-v", 
        "--disable-warnings", 
        "--html=reports/test_report.html", 
        "--self-contained-html"
    ] + test_files
    pytest.main(pytest_args)
    print("Tests Complete.")
    print("HTML report generated at: reports/test_report.html")


if __name__ == "__main__":
    try:
        # Run the ETL process
        run_etl()
        # Run the tests
        run_tests()
    finally:
        # Clean up generated files after testing
        clean_up()
