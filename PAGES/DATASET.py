import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Load dataset
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "..", "train.csv")
df = pd.read_csv(data_path)

st.title("Loan Dataset/Visualization")

df = pd.read_csv("train.csv")

st.write("Dataset Preview")

st.dataframe(df)
# Example interactive chart
fig = px.histogram(df, x="Gender", color="Loan_Status", barmode="group")
st.plotly_chart(fig)
