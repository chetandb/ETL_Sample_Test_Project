import logging
from pathlib import Path
from typing import Union

import pandas as pd

logger = logging.getLogger(__name__)
PathLike = Union[str, Path]


def extract_data(file_path: PathLike) -> pd.DataFrame:
    """
    Extract data from a CSV file into a pandas DataFrame.
    
    Handles various edge cases including empty files, whitespace-only files,
    and malformed CSV data. Returns an empty DataFrame for empty/whitespace files.
    
    Args:
        file_path: Path to the CSV file (str or pathlib.Path object).
    
    Returns:
        A pandas DataFrame containing the extracted data, or an empty DataFrame
        if the file is empty or contains no valid data.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.ParserError: If the CSV file is malformed and cannot be parsed.
    
    Example:
        >>> df = extract_data("data.csv")
        >>> print(f"Extracted {len(df)} rows")
    """
    path = Path(file_path)
    
    if not path.exists():
        logger.error(f"Input file not found: {path}")
        raise FileNotFoundError(f"Input file not found: {path}")

    if path.stat().st_size == 0:
        logger.warning(f"Input file is empty: {path}")
        return pd.DataFrame()

    try:
        df = pd.read_csv(path)
        logger.info(f"Successfully extracted {len(df)} rows from {path}")
        return df
    except pd.errors.EmptyDataError:
        logger.warning(f"CSV file contains no data: {path}")
        return pd.DataFrame()
    except pd.errors.ParserError as e:
        logger.error(f"Failed to parse CSV file {path}: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error reading file {path}: {e}")
        raise
