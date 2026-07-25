import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


def transform_data(
    df: pd.DataFrame,
    column_name: str = "existing_column",
    threshold: int = 25,
) -> pd.DataFrame:
    """
    Transform a DataFrame by performing data enrichment and categorization.
    
    This function:
    - Fills missing values in the specified column with 0
    - Creates a new column with doubled values
    - Categorizes rows as "High" or "Low" based on a threshold
    
    Args:
        df: Input DataFrame to transform.
        column_name: Name of the column to transform (default: "existing_column").
        threshold: Numeric threshold for categorization (default: 25).
                  Values > threshold are marked as "High", others as "Low".
    
    Returns:
        A new DataFrame with added columns 'new_column' and 'status'.
    
    Raises:
        ValueError: If the specified column_name is not in the DataFrame.
        TypeError: If the column contains non-numeric data (except NaN/None).
    
    Example:
        >>> df = pd.DataFrame({"existing_column": [10, 20, 30]})
        >>> result = transform_data(df)
        >>> result["new_column"].tolist()
        [20, 40, 60]
    """
    if column_name not in df.columns:
        logger.error(f"Column '{column_name}' not found in DataFrame")
        raise ValueError(f"Missing required column: {column_name}")

    logger.info(f"Starting transformation on column '{column_name}' with threshold {threshold}")
    
    transformed_df = df.copy()
    transformed_df[column_name] = transformed_df[column_name].fillna(0)
    
    logger.debug(f"Filled {(df[column_name].isna().sum())} NaN values with 0")
    
    transformed_df["new_column"] = transformed_df[column_name] * 2
    transformed_df["status"] = np.where(
        transformed_df[column_name] > threshold,
        "High",
        "Low",
    )
    
    high_count = (transformed_df["status"] == "High").sum()
    logger.info(f"Transformation complete: {high_count} rows marked as 'High', "
                f"{len(transformed_df) - high_count} rows marked as 'Low'")
    
    return transformed_df
