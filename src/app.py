from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd

from mapping import createFig
from dictionaries import *
from quicksort import *
from mergesort import *
from parseSelectedData import *


# Read dataset
df = pd.read_csv("pakistanHousingData_cleaned.csv") # Not needed here, should be in main
df["bedrooms"] = df["bedrooms"].astype(str)
df["baths"] = df["baths"].astype(str)

app = Dash()
app.layout = html.Div([
    # title
    html.H1("Pakistan Housing Prices"),

    html.Div([
        # display map centered on selected data
        dcc.Graph(
            id='All of Pakistan',
            figure=createFig(df, selectedCities, selectedPropTypes, selectedBedrooms, selectedBathrooms),
            style={'width': '70%'}
        ),
        # now display table of data in the middle
        html.Div([
            html.H3("Sorted Housing Data"),
            dash_table.DataTable(
                id='housing-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                # TODO: set data equal to a dictionary representing the updated data
                 data=df.to_dict("records"),
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

        # filters and dropdowns for all selections
        html.Div([

            # select which sorting method
            dcc.Dropdown(
                ['QuickSort Ascending', 'MergeSort Ascending', 'QuickSort Descending', 'MergeSort Descending'],
                id='sorting-options',
                multi=False,
                placeholder="Choose how you would like to sort it"
            ),
            html.Div(id='dd-output-container-sorting'),

            # select which city
            dcc.Dropdown(
                ['Faisalabad', 'Islamabad', 'Karachi', 'Lahore', 'Rawalpindi'],
                id='city selection',
                multi=False, value='Faisalabad',
                placeholder="Select which cities"
            ),
            html.Div(id='dd-output-container-city'),

            # select multiple property types
            dcc.Dropdown(
                ["House", "Penthouse", "Farm House", "Lower Portion", "Upper Portion"],
                id='property type selection',
                multi=True, value=all_types,
                placeholder="Select which property types"
            ),
            html.Div(id='dd-output-container-property'),

            # select number of bathrooms
            dcc.Dropdown(
                [str(i) for i in range(1, 29)],
                id='number of bedrooms selection',
                multi=True,value=all_bathrooms,
                placeholder="Multi-select number of bedrooms"
            ),
            html.Div(id='dd-output-container-bedroom'),

            # select number of bedrooms
            dcc.Dropdown(
                [str(i) for i in range(1, 15)],
                id='number of bathrooms selection',
                multi=True,value=all_bedrooms,
                placeholder="Multi-select number of bathrooms"
            ),
            html.Div(id='dd-output-container-bathroom'),

        ], style={'width': '25%', 'padding': '0 20px', 'display': 'flex', 'flexDirection': 'column', 'gap': '10px'})
    ], style={'display': 'flex', 'justifyContent': 'space-between'})
])

@app.callback(
    Output('All of Pakistan', 'figure'),
    Output('housing-table', 'data'),
    Input('sorting-options', 'value'),
    Input('city selection', 'value'),
    Input('number of bedrooms selection', 'value'),
    Input('number of bathrooms selection', 'value'),
    Input('property type selection', 'value')
)

def update_figure(cities, bedrooms, bathrooms, propTypes):
    for city in selectedCities:
        selectedCities[city] = city in cities if cities else False
    for bathroom in selectedBathrooms:
        selectedBathrooms[bathroom] = bathroom in bathrooms if bathrooms else False
    for bedroom in selectedBedrooms:
        selectedBedrooms[bedroom] = bedroom in bedrooms if bedrooms else False
    for propType in selectedPropTypes:
        selectedPropTypes[propType] = propType in propTypes if propType else False

    return createFig(df, selectedCities, selectedPropTypes, selectedBedrooms, selectedBathrooms)

# TODO: implement update table with updated dictionary of data,
#  make sure it implements merge and quick sort as needed
# def update_table():
#     df = getSelectedData()

if __name__ == '__main__':
    app.run(debug=True)
