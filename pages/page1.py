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
dash.register_page(__name__,path='/', name = 'Wine Analysis') #slash is homepage

###Static figures 
winexcountry = wines.groupby('country')['title'].count().sort_values(ascending=False)
fig1 = px.histogram(winexcountry, x=winexcountry.index, y=winexcountry.values,nbins=50,title="Largest wine producers",labels=dict(x="Country", y="wines"))
fig1.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")

grapescore = wines.groupby('variety')['points'].mean().sort_values(ascending=False)
fig2 = px.bar(grapescore[:5], x=grapescore.index[:5], y=grapescore.values[:5],color_discrete_sequence =['green']*5,title="Best Rated Regions",labels=dict(x="", y="Points"))
fig2.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")

grapescore2 = wines.groupby('variety')['points'].mean().sort_values(ascending=True)
fig3 = px.bar(grapescore2[:5], x=grapescore2.index[:5], y=grapescore2.values[:5],color_discrete_sequence =['red']*5,title="Worst Rated Regions",labels=dict(x="", y="Points"))
fig3.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")

pxccounts = wines.groupby("province")['country'].count().reset_index().sort_values('country',ascending=False)
top_7 = pxccounts[:5]
other = pxccounts[5:].sum()
other["province"] = "Other"
pxccounts = top_7.append(other, ignore_index=True)
fig4 = px.pie(pxccounts, values="country", names="province",hole=.5,title="Largest Producing Regions")
fig4.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")

vxccounts = wines.groupby("variety")['country'].count().reset_index().sort_values('country',ascending=False)
top_7 = vxccounts[:5]
other = vxccounts[5:].sum()
other["variety"] = "Other"
vxccounts = top_7.append(other, ignore_index=True)
fig5 = px.pie(vxccounts, values="country", names="variety",hole=.5,title="Most Common Grape Variety")
fig5.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
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
        html.Br(),
            dbc.Row(
    [
    dbc.Col(html.Div(
    dcc.Graph(id='fig4',
              figure=fig4
              )),md=6,
    ),
    dbc.Col(html.Div(
    dcc.Graph(id='fig5',
              figure=fig5,
              )),md=6,
    ),
    ],
        ),

    
    ]
),