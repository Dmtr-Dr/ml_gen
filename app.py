import streamlit as st
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt

st.title("Molecules")
molecule = st.text_input('Input Molecule', 'O=C(O)Cc1ccc(SSc2ccc(CC(=O)O)cc2)cc1')

def predict():
    st.success("It's done")

st.button('Predict',on_click=predict)

core = Chem.MolFromSmiles(molecule)
img = Draw.MolToImage(core)
img_matplotlib = Draw.MolToMPL(img)
st.pyplot(img_matplotlib, clear_figure=True)


uploaded_file = st.file_uploader("Выберите текстовый файл", type=["txt"])

if uploaded_file is not None:
    # Считываем содержимое загруженного файла
    file_contents = uploaded_file.read()

    # Отображаем содержимое файла
    st.write("Содержимое загруженного файла:")
    st.write(file_contents)
