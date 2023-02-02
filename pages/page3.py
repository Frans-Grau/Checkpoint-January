import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
import pandas as pd
import plotly.express as px

### Link
dash.register_page(__name__,name = 'Price Prediction')

### Upload Dataset
wine_p = pd.read_csv('https://raw.githubusercontent.com/Frans-Grau/Checkpoint-January/main/ML-Output/wines_with_price.csv')
layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3(["Price Overview"])))),
        dbc.Row([
                dbc.Col(html.Div(html.H5(["High-end Categories"]))),
                dbc.Col(html.Div(html.H5(["Most Expensive Regions"]))),
                ]),
        dbc.Row([
                dbc.Col(html.Div(dcc.Graph(id='fig31',)),md=6,),
                dbc.Col(html.Div(dcc.Graph(id='fig32',)),md=6,),
                ]),
        dbc.Row([
                dbc.Col(html.Div(html.H5(["Domain des Croix Price Prediction"]))),
                ]),
        dbc.Row([
                dbc.Col(html.Div(id="table-2"),md=12,),
                ]),
        dbc.Row([
                dbc.Col(html.Div(html.H5(["Country's wine Description"]))),
                dbc.Col(html.Div(html.H5(["Varietys of wine Description"]))),
                ]),
        dbc.Row([
                dbc.Col(html.Div(dcc.Graph(id='fig35',)),md=6,),
                dbc.Col(html.Div(dcc.Graph(id='fig36',)),md=6,),
                ]),
    ]
)