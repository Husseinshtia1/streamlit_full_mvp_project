
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from etl_integration import airbyte_sync
from ml_pipeline import process_data
from visualization import plot_data

# Title of the Streamlit App
st.title("Streamlit-powered Data Analysis Platform")

# Sidebar: ETL, AI, and Automation Options
st.sidebar.header("Options")
etl_sync = st.sidebar.button("Run ETL Sync")

if etl_sync:
    st.write("Running ETL Sync...")
    sync_status = airbyte_sync()
    st.write(sync_status)

# Upload Data for Analysis
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(data.head())
    
    # Show Summary Statistics
    st.write("### Summary Statistics")
    st.write(data.describe())
    
    # Data Processing via ML Pipeline
    st.write("### AI-powered Data Processing")
    processed = process_data(data)
    st.write(processed)
    
    # Data Visualization
    st.write("### Visualization")
    x_col = st.selectbox("Select X-axis", data.columns)
    y_col = st.selectbox("Select Y-axis", data.columns)
    if st.button("Generate Plot"):
        st.write(f"Plotting {x_col} vs {y_col}")
        plot_data(data)
else:
    st.write("Please upload a CSV file for analysis.")
