from sqlalchemy import create_engine
import logging
import pandas as pd
from typing import Dict, Any

logger = logging.getLogger(__name__)

def load_data_to_db(df: pd.DataFrame, config: Dict[str, Any]) -> None:
    try:
        engine = create_engine(f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['dbname']}")
        df.to_sql('target_table', engine, if_exists='replace', index=False)
        logger.info(f"Successfully loaded {len(df)} rows to database")
    except Exception as e:
        logger.error(f"Failed to load data to database: {e}")
        raise
