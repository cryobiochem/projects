import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Simulate Data ---
@st.cache
def generate_data():
    np.random.seed(42)
    dates = pd.date_range(start="2022-01-01", end="2023-12-31", freq="D")
    regions = ["North", "South", "East", "West"]
    categories = ["Electronics", "Fashion", "Home"]
    products = [f"{cat} Product {i}" for cat in categories for i in range(1, 6)]

    data = {
        "Date": np.random.choice(dates, 5000),
        "Region": np.random.choice(regions, 5000),
        "Category": np.random.choice(categories, 5000),
        "Product": np.random.choice(products, 5000),
        "Quantity": np.random.randint(1, 10, 5000),
        "Price": np.random.uniform(10, 500, 5000).round(2),
        "Discount": np.random.uniform(0, 0.3, 5000).round(2),
    }
    df = pd.DataFrame(data)
    df["Revenue"] = (df["Quantity"] * df["Price"] * (1 - df["Discount"])).round(2)
    return df

# Load data
data = generate_data()

# --- Streamlit Layout ---
st.title("E-commerce Sales Dashboard")

# Sidebar for filters
st.sidebar.header("Filters")
date_range = st.sidebar.date_input("Date Range", [data["Date"].min(), data["Date"].max()])
region_filter = st.sidebar.multiselect("Select Region", options=data["Region"].unique(), default=data["Region"].unique())
category_filter = st.sidebar.multiselect("Select Category", options=data["Category"].unique(), default=data["Category"].unique())

# Apply filters
filtered_data = data[
    (data["Date"].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1]))) &
    (data["Region"].isin(region_filter)) &
    (data["Category"].isin(category_filter))
]

# --- Charts and KPIs ---
# KPIs
total_sales = filtered_data["Quantity"].sum()
total_revenue = filtered_data["Revenue"].sum()
avg_order_value = (filtered_data["Revenue"] / filtered_data["Quantity"]).mean()

st.metric("Total Sales", f"{total_sales:,}")
st.metric("Total Revenue", f"${total_revenue:,.2f}")
st.metric("Avg Order Value", f"${avg_order_value:,.2f}")

# Sales Trends
st.subheader("Sales and Revenue Trends")
sales_trend = filtered_data.groupby("Date").agg({"Quantity": "sum", "Revenue": "sum"}).reset_index()
fig = px.line(sales_trend, x="Date", y=["Quantity", "Revenue"], labels={"value": "Metrics", "variable": "Legend"})
st.plotly_chart(fig, use_container_width=True)

# Product Performance
st.subheader("Top Products")
top_products = filtered_data.groupby("Product").agg({"Revenue": "sum"}).sort_values(by="Revenue", ascending=False).head(10).reset_index()
fig = px.bar(top_products, x="Product", y="Revenue", color="Product", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

# Regional Performance
st.subheader("Regional Performance")
region_performance = filtered_data.groupby("Region").agg({"Revenue": "sum"}).reset_index()
fig = px.pie(region_performance, names="Region", values="Revenue", title="Revenue by Region")
st.plotly_chart(fig, use_container_width=True)
