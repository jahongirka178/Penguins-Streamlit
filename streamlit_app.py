import streamlit as st
import pandas as pd
import plotly.express as px

# Ссылка на raw CSV-файл в GitHub
url = "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"

df=pd.read_csv(url)

st.write("Данные из GitHub:")
st.dataframe(df)
