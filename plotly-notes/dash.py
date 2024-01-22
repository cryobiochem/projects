# libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import plotly.express as px
import chart_studio.plotly as py
import chart_studio
import plotly.io as pio

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from plotly.offline import download_plotlyjs, plot, iplot
import cufflinks as cf


# login
username = 'cryobiochem'
api_key = 'mGO7GagmSClu6aQtCkii'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

# data
db = pd.read_excel(
    "C:\\Users\\Asus\\github\\testspace\\Projects\\BrunoDavid\\plotly-notes\\data\\Multidimensional analysis.xlsm", delimiter='tab', sheet_name=3)
test = db[:120]


# Histogram of Extreme Type by Source
fig1 = px.histogram(db, x="ExtremeType",
                 color="Source"
                 ).update_layout(title=dict(text="Total polymer dataset", font=dict(family="verdana", size=18))
                 ).update_xaxes(categoryorder='total descending', title_text=""
                 ).update_yaxes(title_text="Number of entries")
fig1.show()

fig2 = px.histogram(db, x="Source",
                 color="Source"
                 ).update_layout(title=dict(text="What sources are we using for sampling?", font=dict(family="verdana", size=18))
                 ).update_xaxes(categoryorder='total descending', title_text=""
                 ).update_yaxes(title_text="Number of entries")
fig2.show()


# initialize
app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

metadata = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=fig1), width=6, lg=12),
                dbc.Col(dcc.Graph(figure=fig2), width=6),
                dbc.Col(dcc.Graph(figure=fig2), width=6),
                dbc.Col(dcc.Graph(figure=fig2), width=6)
            ]
        ),
    ]
)

toast = dbc.Toast(
    [metadata],
    header="Metadata", style={"maxWidth": "100%"},
)

app.layout = dbc.Container(toast)
app.run_server(debug=False)
