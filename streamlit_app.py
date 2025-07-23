import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import category_encoders as ce
import plotly.express as px


st.set_page_config(page_title='🐧 Penguin Classifier', layout='wide')
st.title("🐧 Датасет Penguins - Обучение и предсказание")
st.write('## Работа с датасетом пингвинов')

url = "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"

df=pd.read_csv(url)

st.subheader('10 случайных строк')
st.dataframe(df.sample(10), use_container_width=True)
