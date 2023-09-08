import streamlit as st
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from PIL import Image
import io

st.title("Molecules")
molecule = st.text_input('Input Molecule', 'O=C(O)Cc1ccc(SSc2ccc(CC(=O)O)cc2)cc1')

def predict():
    st.success("It's done")

st.button('Predict',on_click=predict)

mol = Chem.MolFromSmiles(molecule)
img = AllChem.MolToImage(mol, size=(300, 300))
img_byte_array = io.BytesIO()
img.save(img_byte_array, format="PNG")
img_data = img_byte_array.getvalue()
st.image(Image.open(io.BytesIO(img_data)), caption="Молекула", use_column_width=True)

uploaded_file = st.file_uploader("Выберите текстовый файл", type=["txt"])

if uploaded_file is not None:
    # Считываем содержимое загруженного файла
    file_contents = uploaded_file.read()

    # Отображаем содержимое файла
    st.write("Содержимое загруженного файла:")
    st.write(file_contents)
