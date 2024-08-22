def transform_data(df):
    df['new_column'] = df['existing_column'].apply(lambda x: x * 2)
    return df
