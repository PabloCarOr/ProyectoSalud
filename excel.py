import streamlit as st
import pandas as pd
import openpyxl

df = pd.read_excel('prueba.xlsx')

st.title('Subir base de datos de Excel')

st.write(df)
