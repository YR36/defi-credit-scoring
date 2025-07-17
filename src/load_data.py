import json
import pandas as pd
import os

def load_transactions(path: str) -> pd.DataFrame:
    """
    Load the JSON transactions file into a pandas DataFrame and flatten nested structures.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")

    with open(path, 'r') as f:
        data = json.load(f)

    df = pd.json_normalize(data, sep='.')  # flatten using dot notation
    return df

