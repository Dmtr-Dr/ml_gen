import streamlit as st
import numpy as np
import pandas as pd
from extra import mol_image


st.title("Molecules")
molecule = st.text_input('Input Molecule', 'O=C(O)Cc1ccc(SSc2ccc(CC(=O)O)cc2)cc1')

def predict():
    st.success("It's done")

st.button('Predict',on_click=predict)


if molecule:
    mol_image(molecule)

uploaded_file = st.file_uploader("Выберите текстовый файл", type=["txt"])

if uploaded_file is not None:
    # Считываем содержимое загруженного файла
    file_contents = uploaded_file.read()

    # Отображаем содержимое файла
    st.write("Содержимое загруженного файла:")
    st.write(file_contents)
