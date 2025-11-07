# Source - https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6
# Posted by leenremm
# Retrieved 11/4/2025, License - CC-BY-SA 4.0

import plotly.express as px
import pandas as pd

from parseSelectedData import getSelectedData

def spread_to_zoom(spread):
    if spread > 10:
        return 7  # country level
    elif spread > 5:
        return 9  # regional view
    elif spread > 2:
        return 11  # city-level
    elif spread > 1:
        return 13  # neighborhood
    else:
        return 15  # street view

def createFig(df, cityDict, propDict, bedDict, bathDict):
    df = getSelectedData(df, cityDict, propDict, bedDict, bathDict)

    # prevent empty map:
    if df.empty:
        return {
            'layout': {
                'title': 'No Data Points Match Selection',
                'height': 600,
                'width': 600,
                'xaxis': {'visible': False},
                'yaxis': {'visible': False}
            }
        }

    color_scale = [(0, 'yellow'), (1,'green')]

    fig = px.scatter_map(df,
                            lat="latitude",
                            lon="longitude",
                            hover_name="property_id",
                            hover_data=["property_id", "price"],
                            color="price",
                            color_continuous_scale=color_scale,
                            size="price",
                            height=600,
                            width=600)

    center_lat = df['latitude'].mean()
    center_lon = df['longitude'].mean()

    lat_range = df['latitude'].max() - df['latitude'].min()
    lon_range = df['longitude'].max() - df['longitude'].min()

    fig.update_layout(mapbox_style="open-street-map",
                        mapbox_center={"lat": center_lat, "lon": center_lon}, # Selected Data
                        mapbox_zoom=spread_to_zoom(max(lat_range, lon_range)),
                        margin={"r":0,"t":0,"l":0,"b":0})
    return fig