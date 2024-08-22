from sqlalchemy import create_engine

def load_data_to_db(df, config):
    engine = create_engine(f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['dbname']}")
    df.to_sql('target_table', engine, if_exists='replace', index=False)
