import pandas as pd

def transform_data(df):
    # Fill missing values in 'existing_column' with 0
    df['existing_column'] = df['existing_column'].fillna(0)

    # Add a 'new_column' which is double the existing column
    df['new_column'] = df['existing_column'] * 2

    # Add a 'status' column based on value thresholds
    df['status'] = df['existing_column'].apply(lambda x: 'High' if x > 25 else 'Low')

    return df
