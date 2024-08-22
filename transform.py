def transform_data(df):
    # Example: Fill missing values with 0
    df['existing_column'].fillna(0, inplace=True)

    # Example transformation: doubling the values in 'existing_column'
    df['new_column'] = df['existing_column'] * 2

    return df
