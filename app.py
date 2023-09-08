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

featurizer = dc.feat.CircularFingerprint(size=1024)  # Фичи
ecfp = featurizer.featurize(list(molecule))

smiles_dataset = dc.data.NumpyDataset(X=ecfp)  # Датасет

model = dc.models.MultitaskClassifier(
    1,
    1024,
    layer_sizes=[1000],
    dropouts=[.25],
    learning_rate=0.001,
    batch_size=50)  # batch_size default 50

set_checkpoint(model, 'hiv')  # Устанавливаем чекпоинты

out = model.predict(smiles_dataset)
def predict():
    st.write(out)

st.button('Predict',on_click=predict)
