# LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
import chart_studio.plotly as py
import chart_studio
import cufflinks as cf
import importlib
import datetime

from plotly.subplots import make_subplots
from plotly.colors import n_colors
from IPython.display import Image
from plotly.offline import download_plotlyjs, plot, iplot


### DATASETS
db = pd.read_excel("C:\\Users\\Asus\\github\\testspace\\Projects\\plotly-notes\\data\\Multidimensional analysis.xlsm", delimiter='tab', sheet_name=3)
db2 = pd.read_excel("C:\\Users\\Asus\\github\\testspace\\Projects\\plotly-notes\\data\\Multidimensional analysis.xlsm", delimiter='tab', sheet_name=4)

db
db2


### FUNCTIONS
def polarity (monomer, charge):
# Create a list of cationic, anionic, and uncharged monomers as an alternative to parameter nesting
cationic=list()
anionic=list()
neutral=list()

for i in db2.index:
    monomer = db2['sugar'][i]
    charge = db2['Physiological Charge'][i]
    if charge == -1:
        anionic.append(monomer)
    elif charge == 1:
        cationic.append(monomer)
    else:
        neutral.append(monomer)

print('Positively charged monomers:', ', '.join(cationic))
print('Negatively charged monomers:', ', '.join(anionic))
print('Uncharged monomers:', ', '.join(neutral))

def percentage(part, whole):
    # Transform absolute data in axis to % of max
  return 100 * float(part) / float(whole)



### VARS
#monomers
#cationic + anionic + neutral
#extremeColorCode
#extremeMeanComposition



# METADATA - TYPES OF EXTREMOPHILES
fig = px.histogram(db, x="ExtremeType",
                 color="Source"
                 ).update_layout(title=dict(text="Total polymer dataset", font=dict(family="verdana", size=18))
                 ).update_xaxes(categoryorder='total descending', title_text=""
                 ).update_yaxes(title_text="Number of entries")
fig.show()
fig.write_image(file="C:\\Users\\Asus\\github\\testspace\\Projects\\BrunoDavid\\plotly-notes\\images\\test.jpg",
                width=1000, height=1000, scale=16)
                # highest quality export for jpg, better go pdf + zamzar conversion



# METADATA - TYPES OF SOURCES
fig = px.histogram(db, x="Source",
                 color="Source"
                 ).update_layout(title=dict(text="What sources are we using for sampling?", font=dict(family="verdana", size=18))
                 ).update_xaxes(categoryorder='total descending', title_text="")

fig.show()







# METADATA - POLYMERS BY LOCATION
def getList(dict):
    return [*dict]

Countries=db['Country'].value_counts().to_dict()
CountryCounts=list(Countries.values())
CountryNames=getList(Countries)

px.choropleth(db, locations=CountryNames,
                  locationmode="country names",
                  color=CountryCounts,
                  hover_name=db['Country'].unique(),
                  animation_frame='Year',
                  color_continuous_scale=px.colors.sequential.Plasma,
                  title='Geographical distribution of polymer sources')
# TODO: change title of color bar





# METADATA - HOW EXTENSIVE IS THE CHARACTERIZATION OF EACH POLYMER?
px.bar(db, x=db['Name'], y=db.count(axis=1),
                 color=db['ExtremeType']
                 ).update_layout(title=dict(text="Extent of research", font=dict(family="verdana", size=18))
                 ).update_xaxes(categoryorder="trace", title_text=""
                 ).update_yaxes(title_text="Parameters gathered")











# METADATA - PARAMETER COMPLETENESS
def percentage(part, whole):
  return 100 * float(part) / float(whole)

percentListParam = []
for x in db.columns:
    percent= percentage(db.count()[x], db.count().max())
    percentListParam.append(percent)

px.bar(db, x=db.columns, y=percentListParam,
                 # color=db.columns
                 ).update_layout(title=dict(text="Completeness by parameter", font=dict(family="verdana", size=18))
                 ).update_xaxes(categoryorder='total descending', title_text=""
                 ).update_yaxes(title_text="Polymer entries (%)")
# TODO: create variable relevant, to segment by color relevance












# MEAN OF EVERY MONOMER PER EXTREMOPHILE
monomers = pd.Series(cationic+anionic+neutral)
monomers

extremophiles = {'Type': ['Thermophile', 'Psychrophile', 'Halothermophile', 'Halophile', 'Haloalkaliphile', 'Mesophile'],
                 'Color Key': ['crimson', 'lightseagreen', 'peachpuff', 'darkorange', 'mediumpurple', 'mediumseagreen']}
extremeColorCode = pd.DataFrame(extremophiles, columns = ['Type', 'Color Key'])

# DEBUG: automate this with loop. problem: columns get out of order
#extremeMeanComposition = pd.DataFrame()
#for i in db['ExtremeType'].unique():
    #appender = pd.DataFrame(
    #    {
    #        i: db[monomers][db['ExtremeType'] == i].mean().fillna(0),
    #    }
    #)

    #extremeMeanComposition = pd.concat([extremeMeanComposition, appender], axis=1)

mean = db[monomers].mean()
median = db[monomers].median()
mean_Thermophile = db[monomers][db['ExtremeType'] == 'Thermophile'].mean()
mean_Psychrophile = db[monomers][db['ExtremeType'] == 'Psychrophile'].mean()
mean_Halothermophile = db[monomers][db['ExtremeType'] == 'Halothermophile'].mean()
mean_Halophile = db[monomers][db['ExtremeType'] == 'Halophile'].mean()
mean_Haloalkaliphile = db[monomers][db['ExtremeType'] == 'Haloalkaliphile'].mean()
mean_Mesophile = db[monomers][db['ExtremeType'] == 'Mesophile'].mean()

fig = go.Figure()
fig.add_trace(go.Bar(x=db[monomers].columns, y=mean_Thermophile, name='Thermophile', marker_color='crimson'))
fig.add_trace(go.Bar(x=db[monomers].columns, y=mean_Psychrophile, name='Psychrophile', marker_color='lightseagreen'))
fig.add_trace(go.Bar(x=db[monomers].columns, y=mean_Halothermophile, name='Halothermophile', marker_color='peachpuff'))
fig.add_trace(go.Bar(x=db[monomers].columns, y=mean_Halophile, name='Halophile', marker_color='darkorange'))
fig.add_trace(go.Bar(x=db[monomers].columns, y=mean_Haloalkaliphile, name='Haloalkaliphile', marker_color='mediumpurple'))
fig.add_trace(go.Bar(x=db[monomers].columns, y=mean_Mesophile, name='Mesophile', marker_color='mediumseagreen'))
fig.add_trace(go.Scatter(x=db[monomers].columns, y=mean, name='Global average', marker_color='black', mode='markers'))
fig.add_trace(go.Scatter(x=db[monomers].columns, y=median, name='Global median', marker_color='white', marker_line_width=1, mode='markers'))

fig.update_traces()
fig.update_layout(barmode='stack', barnorm='',
                  xaxis={'categoryorder':'total descending'},
                  yaxis={'title_text':'Cumulative mean composition'},
                  title=dict(text="Quantitative monomer incidence per extremophile", font=dict(family="verdana", size=18)))

fig.show()




 # RADAR CHART OF POLYMER ENTRY BY POLARITY

fig = go.Figure()

# Draw opacity region for cationic monomers
fig.add_trace(go.Barpolar(
    r=[1, 1],
    theta=['GalN', 'GlcN'],
    width=[1,0.5],
    offset=[0,0],
    marker_color=['steelblue', 'steelblue'],
    marker_line_width=0,
    opacity=0.3,
    name = 'Cationic region'
    ))

# Draw opacity region for anionic monomers
fig.add_trace(go.Barpolar(
    r=[1, 1],
    theta=['GalA', 'GlcA'],
    width=[1,0.5],
    offset=[-0.5,-0.5],
    marker_color=['crimson', 'crimson'],
    marker_line_width=0,
    opacity=0.3,
    name = 'Anionic region'
    ))

# Draw opacity region for neutral monomers
fig.add_trace(go.Barpolar(
    r=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    theta=['Ara', 'Fru', 'Fuc', 'Gal', 'GalNAc', 'Glc', 'GlcNAc', 'Man', 'Rha', 'Rib', 'Xil', 'Tre'],
    width=[13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    offset=[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    marker_color=['oldlace', 'oldlace'],
    marker_line_width=0,
    opacity=0.6,
    name = 'Neutral region'
    ))


# Setting legend groups
for type in extremeColorCode['Type']:
    fig.add_trace(go.Scatterpolar(
                r=[0],
                theta=['Glc'],
                showlegend=True,
                legendgroup=type,
                name=type,
                marker=dict(color='black')
    ))


# Plotting data points by extremophile
# Thermophile
for n in range(len(db)):
    if db.iloc[n]['ExtremeType'] == 'Thermophile':
        fig.add_trace(go.Scatterpolargl(
          r = db[monomers].iloc[n],
          theta = monomers,
          mode="markers",
          name = db['Name'][n],
          legendgroup='Thermophile',
          showlegend=True,
          marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='crimson')
          ))

# Psychrophile
for n in range(len(db)):
    if db.iloc[n]['ExtremeType'] == 'Psychrophile':
        fig.add_trace(go.Scatterpolargl(
          r = db[monomers].iloc[n],
          theta = monomers,
          mode="markers",
          name = db['Name'][n],
          legendgroup='Psychrophile',
          showlegend=True,
          marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='lightseagreen')
          ))

# Halothermophile
for n in range(len(db)):
    if db.iloc[n]['ExtremeType'] == 'Halothermophile':
        fig.add_trace(go.Scatterpolargl(
          r = db[monomers].iloc[n],
          theta = monomers,
          mode="markers",
          name = db['Name'][n],
          legendgroup='Halothermophile',
          showlegend=True,
          marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='peachpuff')
          ))

# Halophile
for n in range(len(db)):
    if db.iloc[n]['ExtremeType'] == 'Halophile':
        fig.add_trace(go.Scatterpolargl(
          r = db[monomers].iloc[n],
          theta = monomers,
          mode="markers",
          name = db['Name'][n],
          legendgroup='Halophile',
          showlegend=True,
          marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='darkorange')
          ))

# Haloalkaliphile
for n in range(len(db)):
    if db.iloc[n]['ExtremeType'] == 'Haloalkaliphile':
        fig.add_trace(go.Scatterpolargl(
          r = db[monomers].iloc[n],
          theta = monomers,
          mode="markers",
          name = db['Name'][n],
          legendgroup='Haloalkaliphile',
          showlegend=True,
          marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='mediumpurple')
          ))

# Mesophile
for n in range(len(db)):
    if db.iloc[n]['ExtremeType'] == 'Mesophile':
        fig.add_trace(go.Scatterpolargl(
          r = db[monomers].iloc[n],
          theta = monomers,
          mode="markers",
          name = db['Name'][n],
          legendgroup='Mesophile',
          showlegend=True,
          marker=dict(size=8, line_width=0, opacity=0.8, symbol='hexagon-dot', color='mediumseagreen')
          ))



fig.update_traces(marker_line_width=1)
fig.update_layout(template=None)


fig.show()





### CHRONOLOGICAL BY YEAR
px.violin(data_frame=db,x='Year', y='ExtremeType', orientation='h', color='ExtremeType', color_discrete_sequence=px.colors.sequential.Plotly3
         ).update_layout(title=dict(text="Chronological footprint of extremophile research", font=dict(family="verdana", size=18)), xaxis_showgrid=False, xaxis_zeroline=False
         ).update_traces(orientation='h', side='negative', width=1, points='all',
         ).update_xaxes(categoryorder="trace", title_text=""
         ).update_yaxes(title_text="")





### IDEAS
# MOLECULAR WEIGHT DISTRIBUTION BY EXTREMOPHILE

import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

# Group data together
hist_data = [x1, x2, x3, x4]

group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5, 1])
fig.show()
