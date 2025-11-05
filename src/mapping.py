# Source - https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6
# Posted by leenremm
# Retrieved 11/4/2025, License - CC-BY-SA 4.0

import plotly.express as px
import pandas as pd

def createFig():
    df = pd.read_csv("../pakistan-houses.csv", usecols=['location_id', 'latitude', 'longitude', 'price'])

    color_scale = [(0, 'yellow'), (1,'green')]

    fig = px.scatter_map(df,
                            lat="latitude",
                            lon="longitude",
                            hover_name="location_id",
                            hover_data=["location_id", "price"],
                            color="price",
                            color_continuous_scale=color_scale,
                            size="price",
                            zoom=4.5,
                            height=500,
                            width=500)

    fig.update_layout(mapbox_style="open-street-map",
                        mapbox_center={"lat": 30.3753, "lon": 69.3451}, # Pakistan
                        mapbox_zoom=4.5,
                        margin={"r":0,"t":0,"l":0,"b":0})
    return fig


def createFig1():
    df = pd.read_csv("../pakistan-houses.csv", usecols=['location_id', 'latitude', 'longitude', 'price'])
    color_scale = [(0, 'yellow'), (1, 'green')]
    fig1 = px.scatter_map(df,
                            lat="latitude",
                            lon="longitude",
                            hover_name="location_id",
                            hover_data=["location_id", "price"],
                            color="price",
                            color_continuous_scale=color_scale,
                            size="price",
                            zoom=10,
                            height=500,
                            width=500)

    fig1.update_layout(mapbox_style="open-street-map",
                        map_center={"lat": 24.89711, "lon": 67.05832}, # Karachi
                        map_zoom=10,
                        margin={"r":0,"t":0,"l":0,"b":0})
    return fig1

def createFig2():
    df = pd.read_csv("../pakistan-houses.csv", usecols=['location_id', 'latitude', 'longitude', 'price'])
    color_scale = [(0, 'yellow'), (1, 'green')]
    fig2 = px.scatter_map(df,
                            lat="latitude",
                            lon="longitude",
                            hover_name="location_id",
                            hover_data=["location_id", "price"],
                            color="price",
                            color_continuous_scale=color_scale,
                            size="price",
                            zoom=10,
                            height=500,
                            width=500)

    fig2.update_layout(mapbox_style="open-street-map",
                        map_center={"lat": 31.52236, "lon": 74.34717}, # Lahore
                        map_zoom=10,
                        margin={"r":0,"t":0,"l":0,"b":0})
    return fig2

def createFig3():
    df = pd.read_csv("../pakistan-houses.csv", usecols=['location_id', 'latitude', 'longitude', 'price'])
    color_scale = [(0, 'yellow'), (1, 'green')]
    fig3 = px.scatter_map(df,
                            lat="latitude",
                            lon="longitude",
                            hover_name="location_id",
                            hover_data=["location_id", "price"],
                            color="price",
                            color_continuous_scale=color_scale,
                            size="price",
                            zoom=10,
                            height=500,
                            width=500)

    fig3.update_layout(mapbox_style="open-street-map",
                        map_center={"lat": 33.57087, "lon": 73.05618}, # Rawalpindi
                        map_zoom=10,
                        margin={"r":0,"t":0,"l":0,"b":0})
    return fig3

def createFig4():
    df = pd.read_csv("../pakistan-houses.csv", usecols=['location_id', 'latitude', 'longitude', 'price'])
    color_scale = [(0, 'yellow'), (1, 'green')]
    fig4 = px.scatter_map(df,
                            lat="latitude",
                            lon="longitude",
                            hover_name="location_id",
                            hover_data=["location_id", "price"],
                            color="price",
                            color_continuous_scale=color_scale,
                            size="price",
                            zoom=10,
                            height=500,
                            width=500)

    fig4.update_layout(mapbox_style="open-street-map",
                        map_center={"lat": 31.41683, "lon": 73.09086}, # Faisalabad
                        map_zoom=10,
                        margin={"r":0,"t":0,"l":0,"b":0})
    return fig4
