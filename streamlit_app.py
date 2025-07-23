import streamlit as st
import pandas as pd
import plotly.express as px

url = "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"

st.title("🐧 Датасет Penguins")


df=pd.read_csv(url)

st.write("Данные из GitHub:")
st.dataframe(df)
