import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
import pandas as pd
import plotly.express as px

### Link
dash.register_page(__name__,name = 'Price Prediction')

layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3(["Price Prediction"])))),
    ]
)