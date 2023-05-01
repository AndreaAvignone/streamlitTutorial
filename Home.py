import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Business Analytics",
    layout="wide",
    page_icon="📈",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://dbdmg.polito.it/',
        'Report a bug': "https://dbdmg.polito.it/",
        'About': "# Corso di *Basi di Dati*"
    }
)
col1,col2=st.columns([3,2])
with col1:
    st.title(":red[Live Coding] Session")
    st.markdown("## Corso di :blue[**Basi di Dati**]")
    st.markdown("#### 🧑‍💻️ Creazione di una dashboard")
with col2:
    st.image("images/polito_white.png")