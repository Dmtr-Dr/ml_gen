import streamlit as st
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt
from PIL import Image

st.title("Molecules")
molecule = st.text_input('Input Molecule', 'CCO')

def predict():
    st.success("It's done")

st.button('Predict',on_click=predict)

if molecule is not None:
    img = Draw.MolToImage(mol, size=(300, 300))
    pil_img = Image.fromarray(img)
    st.image(pil_img, caption='Молекула', use_column_width=True)
else:
    st.error("Некорректная SMILES-нотация молекулы")

uploaded_file = st.file_uploader("Выберите текстовый файл", type=["txt"])

if uploaded_file is not None:
    # Считываем содержимое загруженного файла
    file_contents = uploaded_file.read()

    # Отображаем содержимое файла
    st.write("Содержимое загруженного файла:")
    st.write(file_contents)
