### Imports
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
import pandas as pd
import plotly.express as px

### Load the dataset
link = "https://github.com/murpi/wilddata/raw/master/wine.zip"
wines = pd.read_csv(link)

### Link
dash.register_page(__name__,path='/', name = 'Airport Analysis') #slash is homepage

###Layout
layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3(["Airports"])))),
    ]
)