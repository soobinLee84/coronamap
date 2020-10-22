# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from data import countries_df
from builders import make_table


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(countries_df,
size="Confirmed",
hover_name="Country_Region",
size_max=40,
template="plotly_dark",
projection="natural earth",
hover_data={
"Confirmed":":,2f",
"Deaths":":,2f",
"Recovered":":,2f",
"Country_Region":False
}, color="Confirmed", 
    locations="Country_Region",
    locationmode="country names")

app.layout = html.Div(
    style={
        "minHeight":"100vh",
        "backgroundColor":"#111",
        "color":"white",
        "fontFamily":"Open Sans, sans-serif"
        },
     children=[
        html.Header(
            style={"textAlign": "center", "paddingTop": "50px", "marginBottom": 100},
            children=[html.H1("Corona Dashboard", style={"fontSize": 40})],
        ),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
            children=[
                html.Div(
                    style={"grid-column": "span 3"},
                    children=[dcc.Graph(figure=bubble_map)],
                ),
                html.Div(children=[make_table(countries_df)]),
            ],
        ),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
            children=[
                    ],
                ),
            ],
        )



if __name__ == '__main__':
    app.run_server(debug=True)