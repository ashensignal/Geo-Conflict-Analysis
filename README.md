#  Geo-Conflict Analysis Project (Pro-Level Pipeline)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Data Source](https://img.shields.io/badge/Data-ACLED%20/%20Kaggle-orange)](https://acleddata.com/)

An advanced, production-ready geospatial data science pipeline designed to analyze global conflict events, detect spatial hotspots, and visualize temporal violence trends.

---

##  Project Structure

```text
Geo-Conflict-Analysis/
│
├── data/               # Conflict raw data (CSV)
├── notebooks/          # Interactive Jupyter Notebooks for exploration
├── src/                # Modular Python source code (Pipeline core)
│   ├── data_loader.py  # Loads and cleans timestamp/geolocations
│   ├── preprocess.py   # Country and date filtering
│   ├── geo_analysis.py # Core math: Severity scores & hotspots
│   └── visualization.py# Interactive Folium maps & Plotly charts
├── config.yaml         # Project configuration and filters
├── main.py             # Pipeline execution script
└── requirements.txt    # Production dependencies
