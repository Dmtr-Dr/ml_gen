import streamlit as st
import numpy as np
import pandas as pd
from openbabel import pybel


st.title("Molecules")
molecule = st.text_input('Input Molecule', 'O=C(O)Cc1ccc(SSc2ccc(CC(=O)O)cc2)cc1')

def predict():
    st.success("It's done")

st.button('Predict',on_click=predict)

def draw_molecule(molecule_text):
    try:
        # Преобразование текста молекулы в изображение
        mol = pybel.readstring("smi", molecule_text)
        mol.make3D()
        mol.draw(format="png", filename="molecule.png", overwrite=True)

        # Отображение изображения в Streamlit
        st.image("molecule.png", use_column_width=True)
    except Exception as e:
        st.error(f"Произошла ошибка при отображении молекулы: {e}")

if molecule:
    draw_molecule(molecule)

uploaded_file = st.file_uploader("Выберите текстовый файл", type=["txt"])

if uploaded_file is not None:
    # Считываем содержимое загруженного файла
    file_contents = uploaded_file.read()

    # Отображаем содержимое файла
    st.write("Содержимое загруженного файла:")
    st.write(file_contents)
