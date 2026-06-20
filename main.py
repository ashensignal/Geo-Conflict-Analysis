import yaml
from src.data_loader import load_data
from src.preprocess import filter_country, filter_date, clean_data
from src.geo_analysis import severity_score
from src.visualization import create_map, plot_time_series

# load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# load dataset (Make sure you have data in this path later)
try:
    df = load_data("data/raw/conflict_data.csv")
    
    # preprocessing
    df = clean_data(df)
    df = filter_country(df, config["country_filter"])
    df = filter_date(df, config["date_range"]["start"], config["date_range"]["end"])

    # analysis
    df = severity_score(df)

    # visualization
    print("Generating visualizations...")
    # create_map(df) # Uncomment when outputs directory is ready
    # plot_time_series(df)
    print("Analysis Completed ✔")
except FileNotFoundError:
    print("Setup completed successfully. Please add 'conflict_data.csv' inside data/raw/ to run the full pipeline.")
