import streamlit as st
from utils.utils import *
import pandas as pd

if __name__ == "__main__":
    st.title(":blue[Scopri il corso che fa per te]")

    connection_ui()

    # creazione dei tab distinti
    tab_prodotti, tab_staff, tab_clienti = st.tabs(["Prodotti", "Staff", "Clienti"])

    res = execute_query("SELECT DISTINCT Giorno FROM Programma;")
    df = pd.DataFrame(res)
    st.dataframe(df, use_container_width=True)
