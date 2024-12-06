import streamlit as st
from multipage import MultiPage
from dashboard1 import app as dashboard1_app

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.set_page_config(layout="wide")
app.add_page("Dashboard 1", dashboard1_app)

# The main app
app.run()
