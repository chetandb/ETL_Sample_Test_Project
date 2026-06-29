import logging
from typing import Any, Dict

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

logger = logging.getLogger(__name__)
REQUIRED_CONFIG_KEYS = {"host", "port", "user", "password", "dbname"}


def _build_connection_string(config: Dict[str, Any]) -> str:
    return (
        f"postgresql://{config['user']}:{config['password']}@"
        f"{config['host']}:{config['port']}/{config['dbname']}"
    )


def _validate_db_config(config: Dict[str, Any]) -> None:
    missing_keys = REQUIRED_CONFIG_KEYS - set(config.keys())
    if missing_keys:
        raise ValueError(f"Database config is missing required keys: {sorted(missing_keys)}")


def load_data_to_db(df: pd.DataFrame, config: Dict[str, Any]) -> None:
    if df.empty:
        logger.info("DataFrame is empty; skipping database load.")
        return

    _validate_db_config(config)
    connection_string = _build_connection_string(config)
    engine: Engine = create_engine(connection_string)

    try:
        df.to_sql("target_table", engine, if_exists="replace", index=False)
        logger.info(f"Successfully loaded {len(df)} rows to database")
    finally:
        engine.dispose()
