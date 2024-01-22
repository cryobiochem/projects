# This code snippet utilizes Python libraries such as NumPy, Pandas, Matplotlib, Seaborn, and Plotly 
# to create and visualize data related to the photostability of substances under different concentrations 
# and exposure times to UVA and UVB radiation.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# can be abstracted into function, leave for now
concentration = [0.05, 0.1, 0.2, 0.25, 1]

UVA_t0 = [1.00, 1.00, 1.00, 1.00, 1.00]
UVA_t30 = [1.04, 0.99, 0.95, 0.99, 1.04]
UVA_t60 = [0.99, 0.92, 0.93, 0.96, 1.04]
UVA_t90 = [0.97, 0.87, 0.90, 0.95, 1.04]
UVA_rest = [np.nan, 0.81, 0.93, 0.98, 1.05]

UVB_t0 = [1.00, 1.00, 1.00, 1.00, 1.00]
UVB_t30 = [0.83, 0.90, 0.95, 0.99, 0.99]
UVB_t60 = [0.68, 0.84, 0.93, 0.98, 0.99]
UVB_t90 = [0.77, 0.79, 0.92, 0.97, 0.99]
UVB_rest = [np.nan, 0.78, 0.94, 0.99, 1.00]


ps = pd.DataFrame(
    {'concentration':concentration,
    'UVA_t0': UVA_t0,
     'UVA_t30': UVA_t30,
     'UVA_t60': UVA_t60,
     'UVA_t90': UVA_t90,
     'UVA_rest': UVA_rest,
     'UVB_t0': UVB_t0,
     'UVB_t30': UVB_t30,
     'UVB_t60': UVB_t60,
     'UVB_t90': UVB_t90,
     'UVB_rest': UVB_rest
    })




import plotly.graph_objects as go

UVA_t90_percent = [i * 100 for i in UVA_t90]
UVB_t90_percent = [i * 100 for i in UVB_t90]

UVA_rest_percent = [i * 100 for i in UVA_rest]
UVB_rest_percent = [i * 100 for i in UVB_rest]

x=['Winter', 'Spring', 'Summer', 'Fall']
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=ps['concentration'], y=UVA_t90_percent,
    mode='lines',
    line=dict(width=0.5, color='red'),
    stackgroup='one',
    name='UVA'
))

fig.add_trace(go.Scatter(
    x=ps['concentration'], y=UVB_t90_percent,
    mode='lines',
    line=dict(width=0.5, color='blue'),
    stackgroup='two',
    name='UVB'
))


fig.add_trace(go.Scatter(
    x=ps['concentration'], y=[90, 90, 90, 90, 90],
    mode='lines',
    name='lines',
    line=dict(width=2, color='black', dash='dot')
))



fig.update_layout(
    showlegend=False,
    xaxis_type='category',
    yaxis=dict(
        type='linear',
        range=[54, 105],
        ticksuffix='%', title='Photostability'),
    xaxis=dict(title='FucoPol concentration (wt%)'))

fig.show()
fig.write_image(file="C:\\Users\\Asus\\github\\testspace\\Projects\\plotly-notes\\images\\photostable_region.jpg",
                width=675, height=500, scale=16)
                # highest quality export for jpg, better go pdf + zamzar conversion
