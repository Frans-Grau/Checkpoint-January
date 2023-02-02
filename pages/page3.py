import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback, dash_table
import pandas as pd
import plotly.express as px
import numpy as np 
import re
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import nltk
import spacy
from nltk.corpus import stopwords
from wordcloud import WordCloud
import plotly
import plotly.graph_objs as go
from plotly.offline import plot
import random

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
domainX = wine[wine['winery']=='Domaine des Croix'][['title','country','province','variety','year','points','price']].sort_values('points',ascending=False)

### Dropdown menus
selectcountry = list(map(lambda ctr: str(ctr), wine['country'].unique()))
selectcountry.sort()
selectvariety = list(map(lambda vtr: str(vtr), wine['variety'].unique()))
selectvariety.sort()

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
                                                data=domainX.to_dict("rows"),
                                                columns=[{"id": x, "name": x} for x in domainX.columns],
                                                style_cell={'textAlign': 'center'},
                                                ),
                                ]),
                ]),
        dbc.Row([
                dbc.Col(html.Div(html.H5(["Country's wine Description"]))),
                dbc.Col(html.Div(html.H5(["Varietys of wine Description"]))),
                ]),
        dbc.Row([dbc.Col(dcc.Dropdown(
                        id= 'country',
                        placeholder= 'Select a country',
                        options= selectcountry)),
                dbc.Col(dcc.Dropdown(
                        id= 'variety',
                        placeholder= 'Select a wine variety (grape)',
                        options= selectvariety)),
                ]),
        dbc.Row([
                dbc.Col(html.Div(dcc.Graph(id='fig35',)),md=6,),
                dbc.Col(html.Div(dcc.Graph(id='fig36',)),md=6,),
                ]),
    ]
)

### Callbacks
callback(
    Output('fig35','figure'),
    Input('country','value')
)
def generate_country(selectcountry):
    description_country = str(wine[wine['country']==selectcountry]['description'])
    description_country = re.sub(r"\d+","",description_country)
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    nopunc = tokenizer.tokenize(description_country)
    country_words=" ".join(nopunc)
    country_words= nltk.word_tokenize(country_words.lower())
    nums = re.findall("[0-9]+",description_country)
    stop_words = set(stopwords.words('english'))
    stop_words |= set(nums) #add the list with all the numbers in the string to the list of stopwords
    stop_words.update({'like','much','is','in', 'with',selectcountry.lower()})
    words = country_words
    sentence = [w for w in words if not w in stop_words]
    colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(25)]
    weights = [random.randint(15, 35) for i in range(30)]
    data = go.Scatter(x=[random.random() for i in range(20)],
                 y=[random.random() for i in range(25)],
                 mode='text',
                 text=sentence,
                 marker={'opacity': 0.3},
                 textfont={'size': weights,
                           'color': colors})
    layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                        'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})
    fig35 = go.Figure(data=[data], layout=layout)
    return fig35

callback(
    Output('fig36','figure'),
    Input('variety','value')
)
def generate_variety(selectvariety):
    description_country = str(wine[wine['variety']==selectvariety]['description'])
    description_country = re.sub(r"\d+","",description_country)
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    nopunc = tokenizer.tokenize(description_country)
    country_words=" ".join(nopunc)
    country_words= nltk.word_tokenize(country_words.lower())
    nums = re.findall("[0-9]+",description_country)
    stop_words = set(stopwords.words('english'))
    stop_words |= set(nums) #add the list with all the numbers in the string to the list of stopwords
    stop_words.update({'like','much','is','in', 'with',selectvariety.lower()})
    words = country_words
    sentence = [w for w in words if not w in stop_words]
    colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(25)]
    weights = [random.randint(15, 35) for i in range(30)]
    data = go.Scatter(x=[random.random() for i in range(20)],
                 y=[random.random() for i in range(25)],
                 mode='text',
                 text=sentence,
                 marker={'opacity': 0.3},
                 textfont={'size': weights,
                           'color': colors})
    layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                        'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})
    fig36 = go.Figure(data=[data], layout=layout)
    return fig36