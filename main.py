# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from data import countries_df, totals_df
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
title="Confirmed By Country",
template="plotly_dark",
color_continuous_scale = px.colors.sequential.Oryel,

hover_data={
"Confirmed":":,2f",
"Deaths":":,2f",
"Recovered":":,2f",
"Country_Region":False
}, color="Confirmed", 
    locations="Country_Region",
    locationmode="country names")

#bubble_map changing layout
bubble_map.update_layout(margin=dict(l=0,r=0,t=50,b=0)) 

# barGraph
bars_graph = px.bar(totals_df, x="condition", y="count",
hover_data={
    'count':":,"
},
 template="plotly_dark", 
 title="Total Global Cases",
 labels={
     "conditon":"Condition",
     "count":"Count",
     "color": "Condition"
    }
 )

#bar의 제목 설정 x좌표, y좌표 각각 설정
#bars_graph.update_layout(
#    xaxis=dict(title="Condition"),
#    yaxis=dict(title="Count")
#) -> labels 설정을 통해 똑같은 세팅을 할 수 있다.
 
#bar color 지정
bars_graph.update_traces(marker_color=["#ff4d4d","#7d5fff","#32ff7e"])


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
                "display":"grid",
                "gap":50,
                "gridTemplateColumns":"repeat(4, 1fr)"
            },
            children=[
                html.Div(
                    style={"grid-column":"span 3"},
                    children=[dcc.Graph(figure=bubble_map)]),
                html.Div(children=[make_table(countries_df)]),
            ],
        ), html.Div(
            children=[
                html.Div(
                    style={
                        "display":"grid",
                        "gap":50,
                        "gridTemplateColumns":"repeat(4, 1fr)"
                    },
                    children=[dcc.Graph(figure=bars_graph)]),
      
            ],
        ),
 
            ],
        )



if __name__ == '__main__':
    app.run_server(debug=True)