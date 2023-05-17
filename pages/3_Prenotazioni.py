import streamlit as st
from utils.utils import *
import pandas as pd
if __name__ == "__main__":
    st.title("💸 :blue[Prenotazioni]")
    if check_connection():
        query="""WITH costi_mensili AS ( 
                    SELECT STANZA_CodS, EXTRACT(YEAR FROM STR_TO_DATE(DataInizio, '%Y-%m-%d')) AS Anno, EXTRACT(MONTH FROM STR_TO_DATE(DataInizio, '%Y-%m-%d')) AS Mese, 
                            Costo/(STR_TO_DATE(DataFine, '%Y-%m-%d') - STR_TO_DATE(DataInizio, '%Y-%m-%d')) AS CostoGiornaliero 
                    FROM PRENOTAZIONE 
                ), 
                costi_mensili_raggruppati AS ( 
                    SELECT Anno, Mese, STANZA_CodS, AVG(CostoGiornaliero) AS MediaGiornaliera 
                    FROM costi_mensili 
                    GROUP BY Anno, Mese, STANZA_CodS 
                ), 
                costi_mensili_max AS ( 
                    SELECT Anno, Mese, MAX(MediaGiornaliera) AS MediaGiornalieraMax 
                    FROM costi_mensili_raggruppati 
                    GROUP BY Anno, Mese 
                ) 
                SELECT cmr.Mese, cmr.STANZA_CodS, s.Piano, s.Superficie, s.Type, cmr.MediaGiornaliera 
                FROM costi_mensili_raggruppati cmr 
                JOIN costi_mensili_max cmm ON cmr.Anno = cmm.Anno AND cmr.Mese = cmm.Mese AND cmr.MediaGiornaliera = cmm.MediaGiornalieraMax 
                JOIN STANZA s ON s.CodS = cmr.STANZA_CodS;
            """
        result=execute_query(st.session_state["connection"],query)
        df=pd.DataFrame(result)
        col1,col2,col3=st.columns([2,3,2])
        col2.dataframe(df)
        st.line_chart(df,x="Mese",y="MediaGiornaliera")