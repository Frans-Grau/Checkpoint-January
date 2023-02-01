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

### Dropdown menus
dropdown_country = list(map(lambda ctry: str(ctry), wines['country'].unique()))
dropdown_province = list(map(lambda provin: str(provin), wines['province'].unique()))
dropdown_variety = list(map(lambda vrty: str(vrty), wines['variety'].unique()))

###Layout
layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3(["Industry Overview"])))),
        dbc.Row(dbc.Col(dcc.Dropdown(
                        id= 'country',
                        placeholder= 'Select a country',
                        options= dropdown_country))),
        dbc.Row(
    [
    dbc.Col(html.H2('Graph1')),
    dbc.Col(html.H2('Graph2')),
    ]
        )
    ]
),