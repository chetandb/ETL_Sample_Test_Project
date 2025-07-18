# ETL Sample Test Project

## Overview
This project is a sample implementation of an ETL (Extract, Transform, Load) pipeline. It includes Python scripts for extracting data from CSV files, transforming the data, and loading it into a database. The project also contains unit tests to ensure the correctness of the ETL process.

## Project Structure
```
ETL_Sample_Test_Project/
├── pytest_output.log          # Log file for pytest output
├── pytest.ini                 # Pytest configuration file
├── requirements.txt           # Python dependencies
├── csv/                       # Directory containing input and expected CSV files
│   ├── empty_input.csv
│   ├── expected_data.csv
│   └── input_data.csv
├── logs/                      # Directory for log files
│   └── etl_test.log
├── src/                       # Source code for the ETL pipeline
│   ├── __init__.py
│   ├── extract.py             # Script for data extraction
│   ├── load.py                # Script for data loading
│   └── transform.py           # Script for data transformation
├── tests/                     # Unit tests for the ETL pipeline
│   ├── run_etl_tests.py       # Script to run all tests
│   ├── test_extract.py        # Tests for data extraction
│   ├── test_load.py           # Tests for data loading
│   ├── test_transform.py      # Tests for basic data transformation
│   ├── test_transform_complex.py
│   ├── test_transform_conditional.py
│   ├── test_transform_integrity.py
│   ├── test_transform_missing_values.py
│   └── test_transform_unique_constraints.py
```

## Prerequisites
- Python 3.8 or higher
- Install dependencies using `pip install -r requirements.txt`

## How to Run
1. **Run the ETL Process**:
   ```bash
   python src/extract.py
   python src/transform.py
   python src/load.py
   ```

2. **Run Tests**:
   ```bash
   python tests/run_etl_tests.py
   ```

## Logging
Logs for the ETL process and tests are stored in the `logs/etl_test.log` file. The logging configuration is defined in `pytest.ini`.

## License
This project is for educational purposes and does not include a specific license.