import folium
import plotly.express as px

def create_map(df, output_path="outputs/maps/conflict_map.html"):
    m = folium.Map(location=[28, 2], zoom_start=5)
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=3,
            color="red",
            fill=True
        ).add_to(m)
    m.save(output_path)

def plot_time_series(df):
    fig = px.line(
        df.groupby("event_date").size().reset_index(name="events"),
        x="event_date",
        y="events",
        title="Conflict Events Over Time"
    )
    fig.show()
