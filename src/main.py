import pandas as pd
import streamlit as st

# pandas
csv_path = "./data/country_wise_latest.csv"
df = pd.read_csv(csv_path)

metric_columns = [
    "Confirmed",
    "Deaths",
    "Recovered",
    "Active",
    "New cases",
    "New deaths",
    "New recovered",
]

# streamlit
st.set_page_config(page_title="Covid DashBoard", layout="wide", page_icon="🦠")

# sidebar
with st.sidebar:
    st.title("Covid-19 DashBoard")

    country = df["Country/Region"].unique().tolist()
    selected_country = st.selectbox("Country / Region", country)

    metric = metric_columns
    selected_metric = st.selectbox("Filter", metric)

    if selected_country != "All":
        df = df[df["Country/Region"] == selected_country]

st.header("DashBoard")
st.markdown("---")

x_col = "Country/Region"
y_col = selected_metric
st.bar_chart(df, x=x_col, y=y_col)
