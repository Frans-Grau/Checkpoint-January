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

dropdown_country = list(map(lambda ctr: str(ctr), wines['country'].unique()))
dropdown_province = list(map(lambda provin: str(provin), wines['province'].unique()))
dropdown_variety = list(map(lambda vrty: str(vrty), wines['variety'].unique()))

###Static figures 
winexcountry = wines.groupby('country')['title'].count().sort_values(ascending=False)
fig1 = px.histogram(winexcountry, x=winexcountry.index, y=winexcountry.values,nbins=50)

###Layout
layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3(["Industry Overview"])))),
        dbc.Row(dbc.Col(dcc.Dropdown(
                        id= 'country',
                        placeholder= 'Select a country',
                        options= dropdown_country))),
        html.Br(),
        dbc.Row(
    [
    dbc.Col(html.Div(
    dcc.Graph(id='pie1',
              figure= fig1
              ))
    ),
    dbc.Col(html.H2('Graph2')),
    ]
        ),
    ]
),

### Callbacks

