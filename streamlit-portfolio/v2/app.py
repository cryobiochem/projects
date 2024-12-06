import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Streamlit Boilerplate", layout="centered")

# Title and description
st.title("Streamlit App Boilerplate")
st.write("""
This is a basic template for a Streamlit app. Customize it as needed for your project!
""")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Use the options below to interact with the app.")

# Example of user input
name = st.text_input("Enter your name:", "John Doe")
st.write(f"Hello, {name}!")

# Example of numeric input
num = st.number_input("Choose a number:", min_value=0, max_value=100, value=50)
st.write(f"Your chosen number is: {num}")

# Example of a data frame
st.subheader("Dataframe Example")
data = pd.DataFrame({
    'Column A': np.random.randn(10),
    'Column B': np.random.rand(10)
})
st.dataframe(data)

# Example of a plot
st.subheader("Matplotlib Example Plot")
fig, ax = plt.subplots()
ax.plot(data['Column A'], label="Column A")
ax.plot(data['Column B'], label="Column B")
ax.set_title("Line Plot Example")
ax.legend()
st.pyplot(fig)

# Example of a button
if st.button("Click Me!"):
    st.write("Button clicked!")

# Example of file uploader
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(df)

# Example of a progress bar
import time
st.subheader("Progress Bar Example")
progress = st.progress(0)
for i in range(101):
    time.sleep(0.01)
    progress.progress(i)
st.success("Progress Complete!")
