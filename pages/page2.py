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
dash.register_page(__name__, name = 'Domain des Croix') #slash is homepage

### Dropdown menus
dropdown_country = list(map(lambda ctr: str(ctr), wines['country'].unique()))
dropdown_province = list(map(lambda provin: str(provin), wines['province'].unique()))
dropdown_variety = list(map(lambda vrty: str(vrty), wines['variety'].unique()))

###Static figures 
winexcountry = wines.groupby('country')['title'].count().sort_values(ascending=False)
fig1 = px.histogram(winexcountry, x=winexcountry.index, y=winexcountry.values,nbins=50)

###Layout
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
    dbc.Row(html.Div(
    dcc.Graph(id='pie1',
              figure= fig1
              ))
    ),
    ],
        ),
            html.Br(),
            dbc.Row(html.Div(html.H3(["Country Overview"]))),
            dbc.Row(
    [
    dbc.Col(html.Div(
    dcc.Graph(id='fig2',
              ))
    ),
    dbc.Col(html.Div(
    dcc.Graph(id='fig3',
              ))
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

### Callbacks
@callback(
    Output('fig2','figure'),
    Input('country','value')
)
def update_region(selected_country):
    wine_c = wines[wines['country']==selected_country]
    grapescore = wine_c.groupby('variety')['points'].mean().sort_values(ascending=False)
    fig2 = px.histogram(grapescore[:5], x=grapescore.index[:5], y=grapescore.values[:5])
    fig2.update_layout(title="Best Rated Grape Variety")
    return fig2
@callback(
    Output('fig3','figure'),
    Input('country','value')
)
def update_region2(selected_country):
    wine_c = wines[wines['country']==selected_country]
    grapescore = wine_c.groupby('variety')['points'].mean().sort_values(ascending=True)
    fig3 = px.histogram(grapescore[:5], x=grapescore.index[:5], y=grapescore.values[:5])
    fig3.update_layout(title="Worst Rated Grape Variety")
    return fig3
@callback(
    Output('fig4','figure'),
    Input('country','value')
)
def update_region3(selected_country):
    provincexcountry = wines[wines['country']==selected_country]
    pxccounts = provincexcountry.groupby("province")['country'].count().reset_index().sort_values('country',ascending=False)
    top_4 = pxccounts[:4]
    other = pxccounts[4:].sum()
    other["province"] = "Other"
    pxccounts = top_4.append(other, ignore_index=True)
    fig4 = px.pie(pxccounts, values="country", names="province",hole=.5)
    fig4.update_layout(title="Region Analysis")
    return fig4
@callback(
    Output('fig5','figure'),
    Input('country','value')
)
def update_region3(selected_country):
    varietyxcountry = wines[wines['country']==selected_country]
    vxccounts = varietyxcountry.groupby("variety")['country'].count().reset_index().sort_values('country',ascending=False)
    top_5 = vxccounts[:5]
    other = vxccounts[5:].sum()
    other["variety"] = "Other"
    vxccounts = top_5.append(other, ignore_index=True)
    fig5 = px.pie(vxccounts, values="country", names="variety",hole=.5)
    fig5.update_layout(title="Region Analysis")
    return fig5