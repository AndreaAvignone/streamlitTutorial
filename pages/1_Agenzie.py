import streamlit as st
from utils.utils import *
import pandas as pd

if __name__ == "__main__":
    st.title("🏢 :blue[Agenzie]")
    col1,col2,col3=st.columns(3)
    if check_connection():
        query="SELECT COUNT(*) AS 'numAgenzie' FROM AGENZIA;"
        agenzieN=execute_query(st.session_state["connection"],query)
        query="SELECT COUNT(DISTINCT Citta_Indirizzo) AS numCittà FROM `AGENZIA`;;"
        agenzieCity=execute_query(st.session_state["connection"],query)
        query="SELECT Citta_Indirizzo,COUNT(*) AS num FROM `AGENZIA` GROUP BY Citta_Indirizzo ORDER BY `num` DESC LIMIT 1;"
        city=execute_query(st.session_state["connection"],query)
        col1.metric("Numero di Agenzie",agenzieN.mappings().first()['numAgenzie'])
        col2.metric("Numero di Città",agenzieCity.mappings().first()["numCittà"])
        col3.metric("Città con più agenzie",city.mappings().first()["Citta_Indirizzo"])

        query="SELECT AGENZIA.Citta_Indirizzo,CITTA.Latitudine AS 'LAT', CITTA.Longitudine AS 'LON' FROM `AGENZIA`,CITTA WHERE AGENZIA.Citta_Indirizzo=CITTA.Nome;"
        citygeo=execute_query(st.session_state["connection"],query)
        df_map=pd.DataFrame(citygeo)
        st.map(df_map)

        cityName=st.text_input("Filtra per città")
        if cityName=='':
            query="SELECT Citta_Indirizzo,CONCAT(Via_Indirizzo,' ',Numero_Indirizzo) AS 'Indirizzo' FROM `AGENZIA`;"
        else:
            query=f"SELECT Citta_Indirizzo,CONCAT(Via_Indirizzo,' ',Numero_Indirizzo) AS 'Indirizzo' FROM `AGENZIA` WHERE Citta_Indirizzo='{cityName}'"

        cityInfo=execute_query(st.session_state["connection"],query)
        df_info=pd.DataFrame(cityInfo)
        st.dataframe(df_info,use_container_width=True)

    