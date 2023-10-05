import streamlit as st
import pandas as pd
import os
import pwd

# Obtiene el UID del usuario 'adminuser'
uid = pwd.getpwnam("adminuser").pw_uid

# Cambia el propietario del directorio '/home/adminuser/venv/lib/python3.9/site-packages/et_xmlfile' al usuario 'adminuser'
os.chown("/home/adminuser/venv/lib/python3.9/site-packages/et_xmlfile", uid, -1)

# Cambia los permisos del directorio '/home/adminuser/venv/lib/python3.9/site-packages/et_xmlfile' a 777
os.chmod("/home/adminuser/venv/lib/python3.9/site-packages/et_xmlfile", 777)

import pip
pip.main(["install", "openpyxl"])

st.title('Subir base de datos de Excel')

df = pd.read_excel('prueba.xlsx')

st.write(df)