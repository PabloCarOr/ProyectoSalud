import streamlit as st
import pandas as pd
import openpyxl

df = pd.read_excel('50000_Set_de_datos.xlsx')

st.title('Proyecto Covid 19 / Equipo Pumas')

st.write(df)

# ----- Sidebar -----
st.sidebar.header("Filtra aquí:")
edad = st.sidebar.multiselect(
    "Selecciona la ciudad:",
    options=df["EDAD"].unique(),
    default=df["EDAD"].unique()
)