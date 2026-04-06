import pandas as pd
import os
import logging
from typing import Union

logger = logging.getLogger(__name__)

def extract_data(file_path: str) -> pd.DataFrame:
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")

        # Check if the file is empty
        if os.path.getsize(file_path) == 0:
            logger.warning(f"Input file is empty: {file_path}")
            return pd.DataFrame()  # Return an empty DataFrame

        df = pd.read_csv(file_path)
        logger.info(f"Successfully extracted {len(df)} rows from {file_path}")
        return df

    except Exception as e:
        logger.error(f"Failed to extract data from {file_path}: {e}")
        raise
