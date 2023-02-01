### Imports
import dash
import dash_bootstrap_components as dbc
from dash import dash_table
from dash import Input, Output, dcc, html, callback
import pandas as pd
import plotly.express as px

### Load the dataset
link = "https://github.com/murpi/wilddata/raw/master/wine.zip"
wines = pd.read_csv(link)

### Link
dash.register_page(__name__, name = 'Country Overview') 

### Dropdown menus
dropdown_country = list(map(lambda ctr: str(ctr), wines['country'].unique()))
dropdown_country.sort()
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
        dbc.Row(dbc.Col(html.Div(html.H3(["Country Overview"])))),
        dbc.Row(dbc.Col(dcc.Dropdown(
                        id= 'country',
                        placeholder= 'Select a country',
                        options= dropdown_country))),
        html.Br(),
        dbc.Row([
                dbc.Col(html.Div(html.H5(["Wine production"]))),
                dbc.Col(html.Div(html.H5([f"Top 10 Wines"]))),
    ]),
    
            dbc.Row(
    [
    dbc.Col(html.Div(
    dcc.Graph(id='figC1',
              )),md=6,
    ),
    dbc.Col(html.Div(id="update-table"),md=6,
    )
    ],
        ),
            html.Br(),
            dbc.Row(html.Div(html.H3(["Region Overview"]))),
            dbc.Row(
    [
    dbc.Col(html.Div(
    dcc.Graph(id='fig2',
              )),md=6,
    ),
    dbc.Col(html.Div(
    dcc.Graph(id='fig3',
              )),md=6,
    ),
    ],
        ),
        dbc.Row(
    [
    dbc.Col(html.Div(
    dcc.Graph(id='fig4',
              )),md=6,
    ),
    dbc.Col(html.Div(
    dcc.Graph(id='fig5',
              )),md=6,
    ),
    ],
        ),
    
    ]
),

### Callbacks
@callback(
        Output('figC1','figure'),
        Input('country','value')
)
def update_countryx(selected_country):
    wines['year'] = wines['title'].str.extract(r'\b(1[8-9][0-9][0-9]|20[0-2][0-9])\b').astype(float)
    forline = wines[wines['country']==selected_country].groupby('year')['title'].count()
    figc1 = px.line(forline, x=forline.index, y=forline.values,labels=dict(x="", y="production (#bottles)"))
    figc1.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")
    return figc1
@callback(
    Output('update-table', 'children'),
    [Input('country', 'value')]
)
def update_table(selected_country):
    countrytable = wines[wines['country']==selected_country][['title','province','points','price']].sort_values('points',ascending=False)[:10]
    return html.Div(
        [
            # html.H5(f"Top 10 Wines in {selected_country}"),
            # html.Br(),
            dash_table.DataTable(
                data=countrytable.to_dict("rows"),
                columns=[{"id": x, "name": x} for x in countrytable.columns],
                style_cell={'textAlign': 'center'},
            )
        ]
    )

@callback(
    Output('fig2','figure'),
    Input('country','value')
)
def update_region(selected_country):
    wine_c = wines[wines['country']==selected_country]
    grapescore = wine_c.groupby('province')['points'].mean().sort_values(ascending=False)
    fig2 = px.histogram(grapescore[:5], x=grapescore.index[:5], y=grapescore.values[:5],color_discrete_sequence =['green']*5,labels=dict(x="", y="Points"))
    fig2.update_layout(title="Best Rated Regions",paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")
    return fig2
@callback(
    Output('fig3','figure'),
    Input('country','value')
)
def update_region2(selected_country):
    wine_c = wines[wines['country']==selected_country]
    grapescore = wine_c.groupby('province')['points'].mean().sort_values(ascending=True)
    fig3 = px.histogram(grapescore[:5], x=grapescore.index[:5], y=grapescore.values[:5],color_discrete_sequence =['red']*5,labels=dict(x="", y="Points"))
    fig3.update_layout(title="Worst Rated Regions",paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")
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
    fig4.update_layout(title="Largest Producers",paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")
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
    fig5.update_layout(title="Most Common Grape Variety",paper_bgcolor = "rgba(0,0,0,0)",
                  plot_bgcolor = "rgba(0,0,0,0)")
    return fig5