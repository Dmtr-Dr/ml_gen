import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title("Molecules")
molecule = st.text_input('Input Molecule', 'CH-Co')

def predict():
    st.success('It's done')

st.button('Predict',on_click=predict)
