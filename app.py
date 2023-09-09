from __future__ import print_function, division, unicode_literals
import streamlit as st
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt
import deepchem as dc
import os
from deepchem.molnet import load_hiv, featurizers
from deepchem.feat.molecule_featurizers import MolGraphConvFeaturizer
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from tensorflow import keras
import pickle
from utils import *

st.title("Tool для определения молекул-ингибиторов и блокираторов репликации ВИЧ")
molecule = st.text_input('Input Molecule', 'CCO')

mol = Chem.MolFromSmiles(molecule)
if mol is None:
    st.write("Некорректная SMILES-нотация молекулы")
else:
    img = Draw.MolToImage(mol)
    img_matplotlib = Draw.MolToMPL(mol)
    st.pyplot(plt, clear_figure=True)

new_smiles_data = list(molecule)
tokenizer = keras.layers.TextVectorization(max_tokens=1000)
tokenizer.adapt(new_smiles_data)

load_model = pickle.load(open('model.pkl', 'rb'))
prediction = load_model.predict(new_smiles_data)
binary_prediction = [1 if score > 0.5 else 0 for score in prediction]

def predict():
    if binary_prediction[0] ==0:
        st.header("No")
    else:
        st.header("Yes")

st.button('Predict',on_click=predict)

