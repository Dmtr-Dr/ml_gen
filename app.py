import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    background_color="#98ff98"
)

st.title("Molecules")
molecule = st.text_input('Input Molecule', 'CH-Co')

def predict():
    st.success("It's done")

st.button('Predict',on_click=predict)

chart_data = np.random.randn(20, 3)

# Создаем график
plt.plot(chart_data)

# Отображаем график на странице
st.pyplot(plt)
