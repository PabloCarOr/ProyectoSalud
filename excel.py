import streamlit as st
import pandas as pd
import os

os.chown("/home/adminuser/venv/lib/python3.9/site-packages/et_xmlfile", int("adminuser"), -1)
os.chmod("/home/adminuser/venv/lib/python3.9/site-packages/et_xmlfile", 777)

import pip
pip.main(["install", "openpyxl"])

st.title('Subir base de datos de Excel')

df = pd.read_excel('prueba.xlsx')

st.write(df)