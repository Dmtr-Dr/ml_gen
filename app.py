import streamlit as st
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image
import io

st.title("Molecules")
molecule = st.text_input('Input Molecule', 'CC0')

def predict():
    st.success("It's done")

st.button('Predict',on_click=predict)

mol = Chem.MolFromSmiles(molecule)
img = Draw.MolToImage(mol, size=(300, 300))
st.image(Image.fromarray(img), caption="Молекула", use_column_width=True)

uploaded_file = st.file_uploader("Выберите текстовый файл", type=["txt"])

if uploaded_file is not None:
    # Считываем содержимое загруженного файла
    file_contents = uploaded_file.read()

    # Отображаем содержимое файла
    st.write("Содержимое загруженного файла:")
    st.write(file_contents)
