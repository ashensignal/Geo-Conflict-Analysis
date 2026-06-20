import pandas as pd
import numpy as np

def event_density(df):
    return df.groupby(["latitude", "longitude"]).size().reset_index(name="count")

def severity_score(df):
    df = df.copy()
    # calculated based on fatalities only to avoid structural data missing
    df["severity_score"] = df["fatalities"] * 2
    return df

def hotspot_detection(df, threshold=5):
    hotspots = df.groupby(["latitude", "longitude"]).size()
    return hotspots[hotspots > threshold]
