import streamlit as st
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt

st.title("Tool для определения молекул-ингибиторов и блокираторов репликации ВИЧ")
molecule = st.text_input('Input Molecule', 'CCO')

def predict():
    st.success("It's done")

st.button('Predict',on_click=predict)

mol = Chem.MolFromSmiles(molecule)
if mol is None:
    st.write("Некорректная SMILES-нотация молекулы")
else:
    img = Draw.MolToImage(mol)
    img_matplotlib = Draw.MolToMPL(mol)
    st.pyplot(plt, clear_figure=True)


uploaded_file = st.file_uploader("Выберите текстовый файл", type=["txt"])

if uploaded_file is not None:
    # Считываем содержимое загруженного файла
    file_contents = uploaded_file.read()

    # Отображаем содержимое файла
    st.write("Содержимое загруженного файла:")
    st.write(file_contents)
