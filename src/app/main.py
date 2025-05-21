import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Dashboard", layout="wide")

# Load data from Google Drive
@st.cache_data
def load_data():
    url = "https://drive.google.com/file/d/1OChqFUGYtjx115D3xgcWPJYL-Tu_Isd0/view?usp=sharing"
    df = pd.read_csv(url)
    return df

df = load_data()

st.title("☀️ Solar Dashboard")

st.sidebar.header("Filters")
countries = st.sidebar.multiselect(
    "Select Countries", options=df["Country"].unique(), default=df["Country"].unique()
)
plot_type = st.sidebar.radio("Select Plot Type", ["GHI", "DNI", "DHI"])

filtered_df = df[df["Country"].isin(countries)]

# Boxplot
st.subheader(f"📦 Boxplot of {plot_type}")
fig, ax = plt.subplots()
sns.boxplot(x="Country", y=plot_type, data=filtered_df, palette="YlOrBr", ax=ax)
st.pyplot(fig)
