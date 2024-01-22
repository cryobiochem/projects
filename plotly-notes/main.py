# libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as sql
import seaborn as sns
import os

from plotly.subplots import make_subplots
import chart_studio.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

import plotly.io as pio
import plotly.express as px
import cufflinks as cf

# imported functions
import importlib
importlib.import_module('.functions', 'Projects.plotly-notes')
importlib.import_module('.dash', 'Projects.plotly-notes')
importlib.import_module('.plot', 'Projects.plotly-notes')

# datasets
db = pd.read_excel('C:\\Users\\Asus\\github\\testspace\\Projects\\plotly-notes\\data\\Multidimensional analysis.xlsm', delimiter='tab', sheet_name=3)
db


sns.countplot(data=db, x='ExtremeType')
sns.countplot(data=db, x='Source')

sns.heatmap(db.corr(), cmap='seismic')
sns.clustermap(db.corr(), cmap='seismic')


sns.violinplot(x='Source', y='Man', data=db)
sns.violinplot(x='ExtremeType', y='Glc', data=db)


db.drop('Man', axis=1,inplace=True)

### RADAR CHART THAT REMOVES 0s
values = list()
cols = list()


for i in range(4,25):
    if db.iloc[0][i] != 0:
        values.append(db.iloc[0][i])
        cols.append(db.columns[i])
    else

values
cols

df = pd.DataFrame(dict(
    r=values,
    theta=cols))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
fig.show()




### RADAR CHART V2
values = list()
cols = list()
sample = 0

for i in range(4,25):
    values.append(db.iloc[sample][i])
    cols.append(db.columns[i])

values = np.array(values)
index = np.argsort(values)
index = index[-6:]
values = values[index]
cols  = cols[index]


# bruno's humble code. doesnt work, but its humble
mean = db.mean().sort_values(ascending=False)
mean
mean_array = np.array(mean)
mean_array


count_notnull = db.astype(bool).sum(axis=0).sort_values(ascending=False)[4:]
count_notnull
count_notnull.index
count_notnull_array = np.array(count_notnull)
count_notnull_array
# bruno's humble code. doesnt work, but its humble





### NR OCORRÊNCIAS TOP 6 MONÓMEROS NAS ESTRUTURAS
df = pd.DataFrame(dict(
    r=count_notnull,
    theta=count_notnull.index))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
fig.show()


### UBER OP RADAR CHART MULTIPLE INFO PUBLISH NATURE


### Todos os ExtremeTypes
fig = make_subplots(rows=7, cols=3)

for n in range(len(db)):
        fig.add_trace(
            go.Scatterpolar(
              r=db[count_notnull.index].iloc[n],
              theta=count_notnull.index,
              fill='toself', name=db.iloc[n][0])
    )
fig.update_layout(autosize=True)
fig.show()

with open('plotly_graph.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))

#Thermophiles
fig = make_subplots(rows=7, cols=3)

for n in range(len(db)):
    if db.iloc[n][2] == 'Thermophile':
        fig.add_trace(
            go.Scatterpolar(
              r=db[count_notnull.index].iloc[n],
              theta=count_notnull.index,
              fill='toself', name=db.iloc[n][0])
    )
fig.update_layout(title_text="Top 6 Most Frequent Monomer Compositions")
fig.show()


# Psychrophiles
fig = make_subplots(rows=7, cols=3)

for n in range(len(db)):
    if db.iloc[n][2] == 'Psychrophile':
        fig.add_trace(
            go.Scatterpolar(
              r=db[count_notnull.index].iloc[n],
              theta=count_notnull.index,
              fill='toself', name=db.iloc[n][0])
    )
fig.update_layout(title_text="Top 6 Most Frequent Monomer Compositions")
fig.show()



## Metadata

db.iplot('bar', x='Glc', y='Gal')



# monomer_db -> Charge -1/0/1
# db -> Gal, Glc, ...


monomers = db[20:41].columns
