# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from data import countries_df

print(countries_df.values)

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    style={
       
        "minHeight":"100vh",
        "backgroundColor":"#111",
        "color":"white",
        "fontFamily":"Open Sans, sans-serif"
        },
    children=[
            html.Header(
            style={"textAlign":"center","paddingTop":"50px"},
            children=[html.H1("Corona Dashboard",
            style={"fontSize":"40px"})],
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Table(
                                children=[
                                    html.Thead(
                                        children=[
                                            html.Tr(
                                                children=[
                                                    html.Th(column_name.replace("_"," ")) for column_name in countries_df.columns
                                                ]
                                            )
                                        ]
                                    ),
                                    html.Tbody(
                                        children=[
                                            html.Tr(
                                                children=[
                                                    html.Td(
                                                        value_column
                                                    )for value_column in value
                                                ]
                                            )for value in countries_df.values
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ],
)


if __name__ == '__main__':
    app.run_server(debug=True)