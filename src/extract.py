import logging
from pathlib import Path
from typing import Union

import pandas as pd

logger = logging.getLogger(__name__)
PathLike = Union[str, Path]


def extract_data(file_path: PathLike) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    if path.stat().st_size == 0:
        logger.warning(f"Input file is empty: {path}")
        return pd.DataFrame()

    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        logger.warning(f"CSV file contains no data: {path}")
        return pd.DataFrame()

    logger.info(f"Successfully extracted {len(df)} rows from {path}")
    return df
