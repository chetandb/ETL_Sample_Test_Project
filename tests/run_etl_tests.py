import os
from pathlib import Path

import pytest


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    reports_dir = project_root / "reports"
    reports_dir.mkdir(exist_ok=True)

    pytest_args = [
        "-v",
        "--disable-warnings",
        "--html=reports/test_report.html",
        "--self-contained-html",
    ]
    pytest.main(pytest_args)


if __name__ == "__main__":
    main()
