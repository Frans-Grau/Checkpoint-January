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
fig1.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")

grapescore = wines.groupby('variety')['points'].mean().sort_values(ascending=False)
fig2 = px.bar(grapescore[:5], x=grapescore.index[:5], y=grapescore.values[:5],color_discrete_sequence =['green']*5,title="Best Rated Regions")
fig2.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")

grapescore2 = wines.groupby('variety')['points'].mean().sort_values(ascending=True)
fig3 = px.bar(grapescore2[:5], x=grapescore2.index[:5], y=grapescore2.values[:5],color_discrete_sequence =['red']*5,title="Worst Rated Regions")
fig3.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")

###Layout
layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3(["Industry Overview"])))),
        html.Br(),
        dbc.Row(
    [
    dbc.Row(html.Div(
    dcc.Graph(id='pie1',
              figure= fig1
              ))
    ),
    ],
        ),
            html.Br(),
            dbc.Row(
    [
    dbc.Col(html.Div(
    dcc.Graph(id='fig2',
              figure=fig2
              )),md=6,
    ),
    dbc.Col(html.Div(
    dcc.Graph(id='fig3',
              figure=fig3,
              )),md=6,
    ),
    ],
        ),
        dbc.Row(
    [
    dbc.Col(html.Div(
    dcc.Graph(id='fig4',
              ))
    ),
    dbc.Col(html.Div(
    dcc.Graph(id='fig5',
              ))
    ),
    ],
        ),
    
    ]
),