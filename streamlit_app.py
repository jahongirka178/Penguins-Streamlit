import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import category_encoders as ce
import plotly.express as px

url = "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"

st.title("🐧 Датасет Penguins")


df=pd.read_csv(url)

st.write("Данные из GitHub:")
st.dataframe(df)
