import os

import pytest

from extract import extract_data
from transform import transform_data


def run_etl():
    # Paths to the data files
    """./config.yaml"""
    input_data_path = './input_data.csv'
    transformed_data_path = './transformed_data.csv'

    # 1. Extract Data
    print("Starting Data Extraction...")
    df = extract_data(input_data_path)
    print("Data Extraction Complete.")

    # 2. Transform Data
    print("Starting Data Transformation...")
    transformed_df = transform_data(df)
    transformed_df.to_csv(transformed_data_path, index=False)
    print("Data Transformation Complete.")

    # 3. Load Data (Simulated)
    print("Starting Data Loading...")
    # Load to DB (Here we skip actual DB load, you can enable it as needed)
    # load_data_to_db(transformed_df, config)
    print("Data Loading Complete.")

def clean_up():
    # Remove generated files
    transformed_data_path = './transformed_data.csv'
    if os.path.exists(transformed_data_path):
        os.remove(transformed_data_path)
    print("Clean up complete.")

def run_tests():
    print("Starting Tests...")
    pytest.main(["-v", "--disable-warnings", "./"])
    print("Tests Complete.")

if __name__ == "__main__":
    try:
        # Run the ETL process
        run_etl()

        # Run the tests
        run_tests()
    finally:
        # Clean up generated files after testing
        clean_up()
