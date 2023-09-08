import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Molecules")
molecule = st.text_input('Input Molecule', 'CH-Co')

def predict():
    st.success("It's done")

st.button('Predict',on_click=predict)

chart_data = np.random.randn(20, 3)

# Создаем график
plt.plot(chart_data)

# Отображаем график на странице
st.pyplot(plt)

uploaded_file = st.file_uploader("Выберите текстовый файл", type=["txt"])

if uploaded_file is not None:
    # Считываем содержимое загруженного файла
    file_contents = uploaded_file.read()

    # Отображаем содержимое файла
    st.write("Содержимое загруженного файла:")
    st.write(file_contents)
