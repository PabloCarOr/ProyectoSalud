import streamlit as st
import pandas as pd

import pip
pip.main(["install", "openpyxl"])

st.title('Subir base de datos de Excel')

df = pd.read_excel('prueba.xlsx')

st.write(df)
