from dash import Dash, html, dcc
from mapping import createFig, createFig1, createFig2, createFig3, createFig4

app = Dash()

app.layout = html.Div([
    html.H1("Pakistan Housing Prices"),

    html.Div([
        dcc.Graph(id='All of Pakistan', figure=createFig()),
        dcc.Graph(id='Karachi House Prices', figure=createFig1()),
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),

    html.Div([
        dcc.Graph(id='Lahore House Prices', figure=createFig2()),
        dcc.Graph(id='Rawalpindi House Prices', figure=createFig3()),
    ], style={'display': 'flex', 'justifyContent': 'space-around'})
])

if __name__ == '__main__':
    app.run(debug=True)
