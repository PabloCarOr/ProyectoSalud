import streamlit as st
import pandas as pd

st.title('Subir base de datos de Excel')

df = pd.read_excel('50000_Set_de_datos.xlsx')

st.write(df)
