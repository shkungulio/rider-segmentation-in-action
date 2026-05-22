from pathlib import Path
import pandas as pd
from config import RAW_DATA_DIR

def get_trip_files():
    return sorted(RAW_DATA_DIR.glob("*-divvy-tripdata.csv"))

def load_all_data():
    frames = []
    for file_path in get_trip_files():
        df = pd.read_csv(file_path)
        df["file_month"] = file_path.name[:6]
        frames.append(df)

    if not frames:
        raise ValueError("No CSV files found in data/raw")

    return pd.concat(frames, ignore_index=True)