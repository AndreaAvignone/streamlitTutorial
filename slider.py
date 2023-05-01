import streamlit as st
from datetime import datetime,time

st.set_page_config(
    page_title="La mia App",
    layout="wide",
    initial_sidebar_state="expanded",

)

st.sidebar.title("Streamlit :red[Tutorial]")
st.sidebar.header(":blue[Basi di dati]")
st.sidebar.subheader("🧑‍💻️ Applicazioni web")

#slider semplice
age = st.slider('Quanti anni hai?', 0, 130, 25)
st.write("Hai", age, 'anni')

#slider con range
values = st.slider(
    'Seleziona un range di valori',
    0.0, 100.0, (25.0, 75.0))
st.write('Valori:', values)

#range time slider
appointment = st.slider(
    "Fissa il tuo appuntamento:",
    value=(time(11, 30), time(12, 45)))
st.write("Ti sei prenotato per:", appointment)

#datetime slider
start_time = st.slider(
    "Quando vuoi cominciare?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Inizio:", start_time)