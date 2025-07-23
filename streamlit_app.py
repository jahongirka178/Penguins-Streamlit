import streamlit as st
import pandas as pd
import plotly.express as px

url = "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"

st.title("🐧 Датасет Penguins")


df=pd.read_csv(url)

st.write("Данные из GitHub:")
st.dataframe(df)



'''
x_axis = st.selectbox("Выберите переменную по оси X", df.select_dtypes(include='number').columns)
y_axis = st.selectbox("Выберите переменную по оси Y", df.select_dtypes(include='number').columns, index=1)

# Построение графика
fig = px.scatter(
    df,
    x=x_axis,
    y=y_axis,
    color="species",
    symbol="sex",
    title="Визуализация данных пингвинов"
)

st.plotly_chart(fig)
'''
