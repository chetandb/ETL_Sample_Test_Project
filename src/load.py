import logging
import os
from typing import Any, Dict

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

logger = logging.getLogger(__name__)
REQUIRED_CONFIG_KEYS = {"host", "port", "user", "dbname"}


def _build_connection_string(config: Dict[str, Any]) -> str:
    """
    Build a PostgreSQL connection string using environment variables for sensitive data.
    
    Args:
        config: Dictionary containing host, port, user, and dbname keys.
                Password is retrieved from the DB_PASSWORD environment variable.
    
    Returns:
        A PostgreSQL connection string.
    
    Raises:
        ValueError: If DB_PASSWORD environment variable is not set.
    """
    password = os.environ.get("DB_PASSWORD")
    if not password:
        raise ValueError("DB_PASSWORD environment variable is not set")
    
    return (
        f"postgresql://{config['user']}:{password}@"
        f"{config['host']}:{config['port']}/{config['dbname']}"
    )


def _validate_db_config(config: Dict[str, Any]) -> None:
    """
    Validate that all required database configuration keys are present.
    
    Args:
        config: Dictionary to validate against required keys.
    
    Raises:
        ValueError: If any required keys are missing.
    """
    missing_keys = REQUIRED_CONFIG_KEYS - set(config.keys())
    if missing_keys:
        raise ValueError(f"Database config is missing required keys: {sorted(missing_keys)}")


def load_data_to_db(df: pd.DataFrame, config: Dict[str, Any]) -> None:
    """
    Load a pandas DataFrame to a PostgreSQL database table.
    
    Args:
        df: DataFrame to load into the database.
        config: Database configuration containing host, port, user, and dbname.
    
    Raises:
        ValueError: If config is missing required keys or DB_PASSWORD env var is not set.
        Exception: Any exception from the database operation is propagated after cleanup.
    """
    if df.empty:
        logger.info("DataFrame is empty; skipping database load.")
        return

    _validate_db_config(config)
    connection_string = _build_connection_string(config)
    engine: Engine = create_engine(connection_string)

    try:
        df.to_sql("target_table", engine, if_exists="replace", index=False)
        logger.info(f"Successfully loaded {len(df)} rows to database")
    except Exception as e:
        logger.error(f"Failed to load data to database: {e}")
        raise
    finally:
        engine.dispose()
