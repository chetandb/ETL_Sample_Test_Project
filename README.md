# ETL Sample Test Project

## Overview
This project is a sample implementation of an ETL (Extract, Transform, Load) pipeline. It includes Python scripts for extracting data from CSV files, transforming the data, and loading it into a database. The project also contains comprehensive unit tests to ensure the correctness of the ETL process.

## Features
- ✅ **Comprehensive ETL Pipeline**: Extract, Transform, and Load data processing
- ✅ **Robust Testing Suite**: 23 unit tests covering all components
- ✅ **HTML Test Reports**: Beautiful, detailed test reports with pytest-html
- ✅ **Logging Support**: Comprehensive logging for debugging and monitoring
- ✅ **Mock Database Integration**: Safe testing without real database connections

## Project Structure
```
ETL_Sample_Test_Project/
├── pytest_output.log          # Log file for pytest output
├── pytest.ini                 # Pytest configuration file
├── requirements.txt           # Python dependencies
├── view_report.py             # Script to open HTML test report
├── csv/                       # Directory containing input and expected CSV files
│   ├── empty_input.csv
│   ├── expected_data.csv
│   └── input_data.csv
├── logs/                      # Directory for log files
│   └── etl_test.log
├── reports/                   # Directory for HTML test reports
│   └── test_report.html       # Generated HTML test report
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

## Test Coverage
This project includes comprehensive test coverage:

| Module | Tests | Coverage |
|--------|-------|----------|
| Extract | 6 tests | File validation, empty files, invalid paths, whitespace, parsing issues, path objects |
| Transform | 12 tests | Data transformation, missing values, constraints, boundaries, custom parameters, type error handling, nulls |
| Load | 5 tests | Database operations, empty data handling, error handling resource disposal, configuration verification |
| **Total** | **23 tests** | **100% pass rate** |

### Test Categories:
- ✅ **Basic Functionality**: Core ETL operations
- ✅ **Edge Cases**: Empty files, missing data, invalid inputs
- ✅ **Data Integrity**: Unique constraints, data validation
- ✅ **Complex Logic**: Conditional transformations, business rules
- ✅ **Error Handling**: Exception handling, graceful failures

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the ETL Process
```bash
python src/extract.py
python src/transform.py
python src/load.py
```

### 3. Run Tests with HTML Report
```bash
# Run all tests and generate HTML report
python tests/run_etl_tests.py

# Alternative: Run tests directly with pytest
pytest tests/ -v --html=reports/test_report.html --self-contained-html
```

### 4. View Test Results
After running tests, open the HTML report:
- **Location**: `reports/test_report.html`
- **Quick Open**: `python view_report.py` (opens in default browser)
- **Features**: 
  - ✅ Interactive test results
  - ✅ Detailed pass/fail status
  - ✅ Test execution time
  - ✅ Error details and stack traces
  - ✅ Test coverage summary
  - ✅ Self-contained (no external dependencies)

## Logging and Reporting

### Logging
Logs for the ETL process and tests are stored in the `logs/etl_test.log` file. The logging configuration is defined in `pytest.ini`.

### HTML Test Reports
The project generates beautiful HTML test reports using `pytest-html`:
- **Automatic Generation**: Reports are created every time tests run
- **Rich Content**: Includes test details, timing, and error information
- **Self-Contained**: Single HTML file with embedded CSS and JavaScript
- **Browser Compatible**: Works in any modern web browser

### Report Contents
- 📈 **Test Summary**: Pass/fail statistics and execution time
- 🔍 **Detailed Results**: Individual test outcomes with descriptions
- ⚠️ **Error Analysis**: Stack traces and failure details
- 📅 **Timestamps**: Execution times for performance analysis
- 🎨 **Visual Indicators**: Color-coded results for quick assessment

## License
This project is for educational purposes and does not include a specific license.