import streamlit as st
from utils.utils import *
import pymysql,cryptography

if __name__ == "__main__":
    st.set_page_config(
        page_title="Quaderno 4 BDD 2023-24",
        layout="wide",
        page_icon="📒",
        initial_sidebar_state="expanded",
        menu_items={
            # TODO: change this
            'Get Help': 'https://dbdmg.polito.it/',
            'Report a bug': "https://dbdmg.polito.it/",
            'About': "# Corso di *Basi di Dati*"
        }
    )


    col1, col2=st.columns([2,2])
    with col1:
        st.title(":blue[L'amichevole palestra di quartiere]")
        st.header("Qualche numero per fare bella figura...")

    connection_ui()

  