import streamlit as st
import pandas as pd
import openpyxl

df = pd.read_excel('50000_Set_de_datos.xlsx')

st.title('Proyecto Covid 19 / Equipo Pumas')

st.write(df)

# ----- Sidebar -----
st.sidebar.header("Filtra aquí:")
origen = st.sidebar.multiselect(
    "Selecciona la categoría de origen:",
    options=df["ORIGEN"].unique(),
    default=df["ORIGEN"].unique()
)

st.sidebar.header("Filtra aquí:")
sector = st.sidebar.multiselect(
    "Selecciona la categoría de sector:",
    options=df["SECTOR"].unique(),
    default=df["SECTOR"].unique()
)

st.sidebar.header("Filtra aquí:")
entidadUnidadMedica = st.sidebar.multiselect(
    "Selecciona la entidad de unidad médica:",
    options=df["ENTIDAD_UM"].unique(),
    default=df["ENTIDAD_UM"].unique()
)

st.sidebar.header("Filtra aquí:")
sexo = st.sidebar.multiselect(
    "Selecciona el sexo:",
    options=df["SEXO"].unique(),
    default=df["SEXO"].unique()
)

st.sidebar.header("Filtra aquí:")
entidadNacimiento = st.sidebar.multiselect(
    "Selecciona la entidad de nacimiento:",
    options=df["ENTIDAD_NAC"].unique(),
    default=df["ENTIDAD_NAC"].unique()
)

st.sidebar.header("Filtra aquí:")
entidadResidencia = st.sidebar.multiselect(
    "Selecciona la entidad de residencia:",
    options=df["ENTIDAD_RES"].unique(),
    default=df["ENTIDAD_RES"].unique()
)

st.sidebar.header("Filtra aquí:")
municipioResidencia = st.sidebar.multiselect(
    "Selecciona el municipio de residencia:",
    options=df["MUNICIPIO_RES"].unique(),
    default=df["MUNICIPIO_RES"].unique()
)

st.sidebar.header("Filtra aquí:")
tipoPaciente = st.sidebar.multiselect(
    "Selecciona el tipo de paciente:",
    options=df["TIPO_PACIENTE"].unique(),
    default=df["TIPO_PACIENTE"].unique()
)


st.sidebar.header("Filtra aquí:")
fechaIngreso = st.sidebar.multiselect(
    "Selecciona la fecha de ingreso:",
    options=df["FECHA_INGRESO"].unique(),
    default=df["FECHA_INGRESO"].unique()
)

st.sidebar.header("Filtra aquí:")
fechaSintomas = st.sidebar.multiselect(
    "Selecciona la fecha de síntomas:",
    options=df["FECHA_SINTOMAS"].unique(),
    default=df["FECHA_SINTOMAS"].unique()
)

st.sidebar.header("Filtra aquí:")
fechaDefuncion = st.sidebar.multiselect(
    "Selecciona la fecha de defunción:",
    options=df["FECHA_DEF"].unique(),
    default=df["FECHA_DEF"].unique()
)

st.sidebar.header("Filtra aquí:")
fechaDefuncion = st.sidebar.multiselect(
    "Selecciona la fecha de defunción:",
    options=df["INTUBADO"].unique(),
    default=df["INTUBADO"].unique()
)

st.sidebar.header("Filtra aquí:")
neumonia = st.sidebar.multiselect(
    "Selecciona la categoría de neumonía:",
    options=df["NEUMONIA"].unique(),
    default=df["NEUMONIA"].unique()
)

st.sidebar.header("Filtra aquí:")
edad = st.sidebar.multiselect(
    "Selecciona la edad:",
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

st.sidebar.header("Filtra aquí:")
diabetes = st.sidebar.multiselect(
    "Selecciona la categoría de diabetes:",
    options=df["DIABETES"].unique(),
    default=df["DIABETES"].unique()
)

st.sidebar.header("Filtra aquí:")
epoc = st.sidebar.multiselect(
    "Selecciona la categoría de epoc:",
    options=df["EPOC"].unique(),
    default=df["EPOC"].unique()
)

st.sidebar.header("Filtra aquí:")
asma = st.sidebar.multiselect(
    "Selecciona la categoría de asma:",
    options=df["ASMA"].unique(),
    default=df["ASMA"].unique()
)

st.sidebar.header("Filtra aquí:")
inmunosupresor = st.sidebar.multiselect(
    "Selecciona la categoría de inmunosupresor:",
    options=df["INMUSUPR"].unique(),
    default=df["INMUSUPR"].unique()
)

st.sidebar.header("Filtra aquí:")
hipertension = st.sidebar.multiselect(
    "Selecciona la categoría de hipertension:",
    options=df["HIPERTENSION"].unique(),
    default=df["HIPERTENSION"].unique()
)

st.sidebar.header("Filtra aquí:")
otraEnfermedad = st.sidebar.multiselect(
    "Selecciona la categoría de otra enfermedad:",
    options=df["OTRA_COM"].unique(),
    default=df["OTRA_COM"].unique()
)

st.sidebar.header("Filtra aquí:")
cardiovascular = st.sidebar.multiselect(
    "Selecciona la categoría de cardiovascular:",
    options=df["CARDIOVASCULAR"].unique(),
    default=df["CARDIOVASCULAR"].unique()
)

st.sidebar.header("Filtra aquí:")
obesidad = st.sidebar.multiselect(
    "Selecciona la categoría de obesidad:",
    options=df["OBESIDAD"].unique(),
    default=df["OBESIDAD"].unique()
)

st.sidebar.header("Filtra aquí:")
renalCronica = st.sidebar.multiselect(
    "Selecciona la categoría de insuficiencia renal crónica:",
    options=df["RENAL_CRONICA"].unique(),
    default=df["RENAL_CRONICA"].unique()
)

st.sidebar.header("Filtra aquí:")
tabaquismo = st.sidebar.multiselect(
    "Selecciona la categoría de tabaquismo:",
    options=df["TABAQUISMO"].unique(),
    default=df["TABAQUISMO"].unique()
)

st.sidebar.header("Filtra aquí:")
otroCaso = st.sidebar.multiselect(
    "Selecciona la categoría de contacto con otro caso de COVID:",
    options=df["OTRO_CASO"].unique(),
    default=df["OTRO_CASO"].unique()
)

st.sidebar.header("Filtra aquí:")
migrante = st.sidebar.multiselect(
    "Selecciona la categoría de migrante:",
    options=df["MIGRANTE"].unique(),
    default=df["MIGRANTE"].unique()
)

st.sidebar.header("Filtra aquí:")
paisNacionalidad = st.sidebar.multiselect(
    "Selecciona la categoría de país de nacionalidad:",
    options=df["PAIS_NACIONALIDAD"].unique(),
    default=df["PAIS_NACIONALIDAD"].unique()
)

st.sidebar.header("Filtra aquí:")
paisOrigen = st.sidebar.multiselect(
    "Selecciona la categoría de país de origen:",
    options=df["PAIS_ORIGEN"].unique(),
    default=df["PAIS_ORIGEN"].unique()
)

st.sidebar.header("Filtra aquí:")
unidadCuidadosIntensivos = st.sidebar.multiselect(
    "Selecciona la categoría de Unidad de Cuidados Intensivos:",
    options=df["UCI"].unique(),
    default=df["UCI"].unique()
)

#df_selection = df.query(
#    "EDAD == @edad & NACIONALIDAD == @nacionalidad & EMBARAZO == @embarazo & HABLA_LENGUA_INDIG == @lenguaIndigena"
#)

#st.dataframe(df_selection)