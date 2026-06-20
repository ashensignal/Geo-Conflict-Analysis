def filter_country(df, country):
    return df[df["country"] == country]

def filter_date(df, start, end):
    return df[(df["event_date"] >= start) & (df["event_date"] <= end)]

def clean_data(df):
    df = df.copy()
    df = df.drop_duplicates()
    df = df[df["fatalities"] >= 0]
    return df
