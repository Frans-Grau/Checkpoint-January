import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback, dash_table
import pandas as pd
import plotly.express as px

### Link
dash.register_page(__name__,name = 'Price Prediction')

### Upload Dataset
wine = pd.read_csv('https://raw.githubusercontent.com/Frans-Grau/Checkpoint-January/main/ML-Output/wines_with_price.csv')
wine['price'] = wine['price'].round(2)
wine = wine[wine['price']>0]

### Static Graphs
### Average price for the largest varieties
varietytop10 = wine['variety'].value_counts()[:5].index.tolist()
data = wine[wine['variety'].isin(varietytop10)]
fig311 = px.violin(data, x='variety', y='price',labels=dict(x="Country", y="Average Price"))
fig311.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")

### Average price for the largest varieties
expensive = wine.groupby('province')['price'].mean().sort_values(ascending=False)[:5].index.tolist()
data = wine[wine['province'].isin(expensive)]
fig322 = px.violin(data, x='province', y='price',labels=dict(x="Country", y="Average Price"))
fig322.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")


### Static table
domaincroix = wine[['title','country','province','variety','year','points','price']].sort_values('points',ascending=False)

###Layout
layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3(["Price Overview"])))),
        dbc.Row([
                dbc.Col(html.Div(html.H5(["Largest wine categories price distribution"]))),
                dbc.Col(html.Div(html.H5(["Price distribution in expensive regions"]))),
                ]),
        dbc.Row([
                dbc.Col(html.Div(dcc.Graph(id='fig31', figure= fig311)),md=6,),
                dbc.Col(html.Div(dcc.Graph(id='fig32', figure= fig322)),md=6,),
                ]),
        dbc.Row([
                dbc.Col(html.Div(html.H5(["Domain des Croix Price Prediction"]))),
                ]),
        dbc.Row([
                html.Div([dash_table.DataTable(
                                                data=domaincroix.to_dict("rows"),
                                                columns=[{"id": x, "name": x} for x in domaincroix.columns],
                                                style_cell={'textAlign': 'center'},
                                                ),
                                ]),
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

### Callbacks