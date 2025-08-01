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
st.header('Работа с датасетом пингвинов')

url = "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
df = pd.read_csv(url)

# Выведем 10 случайных строк
st.write('## 10 случайных строк')
st.dataframe(df.sample(10), use_container_width=True)

# Графики
st.write('## Визуализация')
col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(df, x='species', color='island', barmode='group', title='Распределение видов по островам')
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    fig2 = px.scatter(df, x='bill_length_mm', y='flipper_length_mm', color='species',
                      title='Длина клюва vs. Длина крыла')
    st.plotly_chart(fig2, use_container_width=True)



# Работа с данными
X = df.drop(columns=['species'])
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

encoder = ce.TargetEncoder(cols=['island', 'sex'])
X_train_encoded = encoder.fit_transform(X_train, y_train)
X_test_encoded = encoder.transform(X_test)

### Классификация
models = {'Decision Tree': DecisionTreeClassifier(random_state=42),
          'KNN': KNeighborsClassifier(4),
          }

results = []

for name, model in models.items():
    model.fit(X_train_encoded, y_train)
    acc_train = accuracy_score(y_train, model.predict(X_train_encoded))
    acc_test = accuracy_score(y_test, model.predict(X_test_encoded))
    results.append({
        'Model': name,
        'Train Accuracy': round(acc_train, 2),
        'Test Accuracy': round(acc_test, 2)
    })

st.write('## Сравнение моделей по точности')
st.table(pd.DataFrame(results))

'''
st.sidebar.header('Предсказание по параметрам')
island_input = st.sidebar.selectbox('Остров', df['island'].unique())
sex_input = st.sidebar.selectbox('Пол', df['sex'].unique())

user_input = pd.DataFrame([{
    'island': island_input,
    'sex': sex_input
}])

st.dataframe(user_input, use_container_width=True)

st.sidebar.subheader("📈 Результаты предсказания")
for name, model in models.items():
    pred = model.predict(user_encoded)[0]
    proba = model.predict_proba(user_encoded)[0]
    st.sidebar.markdown(f"**{name}: {pred}**")
    proba_df = pd.DataFrame({'Вид': model.classes_, 'Вероятность': proba})
    st.sidebar.dataframe(proba_df.set_index("Вид"), use_container_width=True)
'''
