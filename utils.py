import pandas as pd
import os
import pysubs2
import pandas as pd

def load_subtitles_dataset(file_path):
    """
    Loads subtitles from a CSV file with a 'script' column.
    """
    df = pd.read_csv(file_path)
    if 'script' not in df.columns:
        raise ValueError("CSV must contain a 'script' column.")
    return df


def load_subtitles_datasetnew(folder_path):
    data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".ass"):
            file_path = os.path.join(folder_path, filename)
            subs = pysubs2.load(file_path)
            for line in subs:
                data.append({
                    "episode": filename,
                    "start": line.start,
                    "end": line.end,
                    "text": line.text
                })

    return pd.DataFrame(data)