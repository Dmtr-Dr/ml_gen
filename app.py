import streamlit as st

st.title("Мое первое Streamlit приложение")

user_input = st.text_input("Введите ваше имя")
if user_input:
    st.write(f"Привет, {user_input}!")

import matplotlib.pyplot as plt
import numpy as np

chart_data = np.random.randn(20, 3)
st.line_chart(chart_data)
