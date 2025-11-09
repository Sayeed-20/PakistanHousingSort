from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd

from mapping import createFig
from dictionaries import *
from quicksort import *
from mergesort import *
from parseSelectedData import *

# Read dataset
df = pd.read_csv("pakistanHousingData_cleaned.csv") # O(n)
df["bedrooms"] = df["bedrooms"].astype(str)
df["baths"] = df["baths"].astype(str)

# Create frontend application
app = Dash()
app.layout = html.Div([
    # Title
    html.H1("Pakistan Housing Prices"),

    html.Div([
        # Display map centered on selected data
        dcc.Graph(
            id='All of Pakistan',
            figure=createFig(df, selectedCities, selectedPropTypes, selectedBedrooms, selectedBathrooms), # O(m)
            style={'width': '70%'}
        ),
        # Display datatable in center
        html.Div([
            html.H3("Sorted Housing Data"),
            dash_table.DataTable(
                id='housing-table',
                columns=[{"name": i, "id": i} for i in df.columns], # O(5)
                data=df.to_dict("records"), #O(N)
                style_table={'height': '600px', 'overflowY': 'auto'},
                style_cell={'textAlign': 'left', 'padding': '5px'},
                style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'},
                fixed_rows={'headers': True},
                page_action='none',
                virtualization=True
            )
        ], style={
            'width': '60%',
            'padding': '0 20px',
            'overflowY': 'scroll',
            'border': '1px solid #ccc'
        }),

        # Filters and dropdowns for all selections
        html.Div([

            # Select which sorting method
            dcc.Dropdown(
                ['QuickSort Ascending', 'MergeSort Ascending', 'QuickSort Descending', 'MergeSort Descending'],
                id='sorting-options',
                multi=False,
                placeholder="Choose how you would like to sort it"
            ),
            html.Div(id='dd-output-container-sorting'),

            # Select which city(s)
            dcc.Dropdown(
                ['Faisalabad', 'Islamabad', 'Karachi', 'Lahore', 'Rawalpindi'],
                id='city selection',
                multi=True, value=all_cities,
                placeholder="Select which cities"
            ),
            html.Div(id='dd-output-container-city'),

            # Select which property types
            dcc.Dropdown(
                ["House", "Penthouse", "Flat", "Farm House", "Lower Portion", "Upper Portion"],
                id='property type selection',
                multi=True, value=all_types,
                placeholder="Select which property types"
            ),
            html.Div(id='dd-output-container-property'),

            # Select number of bedrooms
            dcc.Dropdown(
                [str(i) for i in range(0, 29)],
                id='number of bedrooms selection',
                multi=True,value=all_bedrooms,
                placeholder="Multi-select number of bedrooms"
            ),
            html.Div(id='dd-output-container-bedroom'),

            # Select number of bathrooms
            dcc.Dropdown(
                [str(i) for i in range(0, 15)],
                id='number of bathrooms selection',
                multi=True,value=all_bathrooms,
                placeholder="Multi-select number of bathrooms"
            ),
            html.Div(id='dd-output-container-bathroom'),

        ], style={'width': '25%', 'padding': '0 20px', 'display': 'flex', 'flexDirection': 'column', 'gap': '10px'})
    ], style={'display': 'flex', 'justifyContent': 'space-between'})
])

# Front end communication to update backend data for datatable
@app.callback(
    Output('housing-table', 'data'),
    Input('sorting-options', 'value'),
    Input('city selection', 'value'),
    Input('number of bedrooms selection', 'value'),
    Input('number of bathrooms selection', 'value'),
    Input('property type selection', 'value')
)

# Update backend data regarding creation of datatable
def update_data(sortType, cities, bedrooms, bathrooms, propTypes):
    print("callback triggered")
    for city in selectedCities:
        selectedCities[city] = city in cities if cities else False
        print("Selected city: ", city, "status: ", selectedCities[city])
    for bathroom in selectedBathrooms:
        selectedBathrooms[bathroom] = bathroom in bathrooms if bathrooms else False
        print("Selected bathroom: ", bathroom, "status: ", selectedBathrooms[bathroom])
    for bedroom in selectedBedrooms:
        selectedBedrooms[bedroom] = bedroom in bedrooms if bedrooms else False
        print("Selected bedroom: ", bedroom, "status: ", selectedBedrooms[bedroom])
    for propType in selectedPropTypes:
        selectedPropTypes[propType] = propType in propTypes if propType else False

    tempDataset = parseSelectedData(df, selectedCities, selectedPropTypes, selectedBedrooms, selectedBathrooms)

    if sortType == "QuickSort Ascending":
        quicksort(tempDataset.data, 0, len(tempDataset.data)-1, "ascending")
    elif sortType == "MergeSort Ascending":
        mergeSort(tempDataset.data, 0, len(tempDataset.data)-1, "ascending")
    elif sortType == "QuickSort Descending":
        quicksort(tempDataset.data, 0, len(tempDataset.data)-1, "descending")
    elif sortType == "MergeSort Descending":
        mergeSort(tempDataset.data, 0, len(tempDataset.data)-1, "descending")

    newDf = pd.DataFrame(columns=["property_id",
                                  "price",
                                  "city",
                                  "property_type",
                                  "longitude",
                                  "latitude",
                                  "bedrooms",
                                  "baths"])

    for item in tempDataset.data:
        newDf.loc[len(newDf)] = [item.id,
                                 item.price,
                                 item.city,
                                 item.propType,
                                 item.long,
                                 item.lat,
                                 item.bedrooms,
                                 item.baths]

    table_data = newDf.to_dict("records")

    return table_data

# Front end communication to update backend data for map
@app.callback(
    Output('All of Pakistan', 'figure'),
    Input('city selection', 'value'),
    Input('number of bedrooms selection', 'value'),
    Input('number of bathrooms selection', 'value'),
    Input('property type selection', 'value')
)

# Update backend data regarding creation of map
def update_figure(cities, bedrooms, bathrooms, propTypes):
    for city in selectedCities:
        selectedCities[city] = city in cities if cities else False
        print("Selected city: ", city, "status: ", selectedCities[city]) # Debugging statement
    for bathroom in selectedBathrooms:
        selectedBathrooms[bathroom] = bathroom in bathrooms if bathrooms else False
        print("Selected bathroom: ", bathroom, "status: ", selectedBathrooms[bathroom]) # Debugging statement
    for bedroom in selectedBedrooms:
        selectedBedrooms[bedroom] = bedroom in bedrooms if bedrooms else False
        print("Selected bedroom: ", bedroom, "status: ", selectedBedrooms[bedroom]) # Debugging statement
    for propType in selectedPropTypes:
        selectedPropTypes[propType] = propType in propTypes if propType else False

    return createFig(df, selectedCities, selectedPropTypes, selectedBedrooms, selectedBathrooms)

if __name__ == '__main__':
    app.run(debug=True)
