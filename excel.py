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

st.sidebar.header("Filtra aquí:")
nacionalidad = st.sidebar.multiselect(
    "Selecciona la nacionalidad:",
    options=df["NACIONALIDAD"].unique(),
    default=df["NACIONALIDAD"].unique()
)

st.sidebar.header("Filtra aquí:")
embarazo = st.sidebar.multiselect(
    "Selecciona la categoría de embarazo:",
    options=df["EMBARAZO"].unique(),
    default=df["EMBARAZO"].unique()
)

st.sidebar.header("Filtra aquí:")
lenguaIndigena = st.sidebar.multiselect(
    "Selecciona la categoría de lengua indígena:",
    options=df["HABLA_LENGUA_INDIG"].unique(),
    default=df["HABLA_LENGUA_INDIG"].unique()
)