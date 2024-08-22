import pandas as pd
import os

def extract_data(file_path):
    # Check if the file is empty
    if os.path.getsize(file_path) == 0:
        return pd.DataFrame()  # Return an empty DataFrame

    return pd.read_csv(file_path)
