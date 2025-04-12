import pandas as pd

def load_subtitles_dataset(file_path):
    """
    Loads subtitles from a CSV file with a 'script' column.
    """
    df = pd.read_csv(file_path)
    if 'script' not in df.columns:
        raise ValueError("CSV must contain a 'script' column.")
    return df
