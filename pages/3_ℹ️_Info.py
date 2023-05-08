import streamlit as st

if __name__ == "__main__":
    st.title("ℹ️ Informazioni sul :red[DB]")
    st.subheader("*Database di un rivenditore di modellini in scala di automobili.*")

    col1,col2=st.columns(2)
    col1.image("images/MySQL-Sample-Database-Schema.png")
    col2.markdown("### 🎯 :blue[Obiettivo]: Realizzare una semplice dashboard che raccola alcune delle principali informazioni dell'azienda.")
    col2.markdown("### 📁 :blue[DB]: Si tratta di un Database MySQL di esempio chiamato *classicmodels* ")
    col2.markdown("### 🔬 :blue[Requisiti]: Riportare una panoramica dei prodotti, staff e clienti. Includere un'interfaccia per aggiungere nuovi prodotti al database.")
    col2.markdown("### 📊 :blue[Visualizzazione]: Eseguire le interrogazioni in SQL attraverso *SQLAlchemy* e visualizzare i risultati attraverso i widget :red[Streamlit].")
    
    st.markdown("🌐 Per ulteriori informazioni: https://www.mysqltutorial.org/mysql-sample-database.aspx")