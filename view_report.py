#!/usr/bin/env python3
"""
Simple script to open the HTML test report in the default browser.
"""

import os
import webbrowser
from pathlib import Path

def open_test_report():
    """Open the HTML test report in the default browser."""
    # Get the absolute path to the report
    script_dir = Path(__file__).parent
    report_path = script_dir / "reports" / "test_report.html"
    
    if report_path.exists():
        # Convert to absolute path and open in browser
        absolute_path = report_path.absolute()
        file_url = f"file:///{absolute_path.as_posix()}"
        
        print(f"Opening test report: {absolute_path}")
        webbrowser.open(file_url)
        print("✅ Test report opened in your default browser!")
    else:
        print("❌ Test report not found!")
        print("Please run the tests first: python tests/run_etl_tests.py")
        print(f"Expected location: {report_path}")

if __name__ == "__main__":
    open_test_report()