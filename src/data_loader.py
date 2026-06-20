import pandas as pd

def load_data(path: str):
    df = pd.read_csv(path)
    # basic cleaning
    df = df.dropna(subset=["latitude", "longitude"])
    df["event_date"] = pd.to_datetime(df["event_date"])
    return df
