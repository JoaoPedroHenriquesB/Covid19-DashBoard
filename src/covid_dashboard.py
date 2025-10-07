import pandas as pd
import plotly.express as px
import streamlit as st

# pandas
csv_path = "./data/country_wise_latest.csv"
try:
    df_original = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"Erro: O arquivo não foi encontrado em '{csv_path}'.")
    st.stop()

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

df_filtered = df_original.copy()

# sidebar
with st.sidebar:
    st.title("Filters 🔎")

    country_list = ["All"] + df_original["Country/Region"].unique().tolist()
    selected_country = st.selectbox("Country / Region", country_list)

    selected_metric = st.selectbox("Metrics", metric_columns)

    if selected_country != "All":
        df_filtered = df_original[df_original["Country/Region"] == selected_country]


st.title("Covid-19 DashBoard")
# st.markdown("---")

x_col = "Country/Region"
y_col = selected_metric
chart_data = df_filtered.copy()
chart_title = ""

if selected_country == "All":
    chart_data = chart_data.nlargest(20, y_col)
    chart_title = "Top 20 Countries"
else:
    chart_title = f"{y_col} in {selected_country}"

#st.subheader(chart_title)
try:
    fig = px.bar(
        chart_data,
        x=x_col,
        y=y_col,
        title=chart_title,
    )

    fig.update_xaxes(
        tickfont=dict(size=14, weight="bold"),
        automargin=True,
    )

    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao gerar o gráfico: {e}")
