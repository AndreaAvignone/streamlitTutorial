import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *

if __name__ == "__main__":
    st.set_page_config(
        page_title="La mia App",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://dbdmg.polito.it/',
            'Report a bug': "https://dbdmg.polito.it/",
            'About': "# Corso di *Basi di Dati*"
        }
    )
    st.title("📈 Gestione Stanze Hotel")
    st.markdown(" ## :blue[Laboratorio] :red[Streamlit]")

    if "connection" not in st.session_state.keys():
        st.session_state["connection"]=False

    check_connection()
