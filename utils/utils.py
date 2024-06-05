import streamlit as st
from sqlalchemy import create_engine, text

"""Raccoglie le principali funzioni condivise dalle varie pagine"""

#connettersi all'engine
def connect_to_db():
    try:
        dialect = "mysql+pymysql"
        username = "student"
        password = "user_pwd"
        host = "localhost"
        dbname = "palestra"
        engine = create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}')
        conn = engine.connect()
        return conn
    except:
        return None

 # esegue la query fornita con un tempo massimo di risposta di 240s (4 minuti)
def execute_query(query):
    conn = st.session_state["connection"]
    return conn.execute(text(query))

#TODO: serve?
# mostra i numeri in una forma più compatta
def compact_format(num):
    num=float(num)
    if abs(num) >= 1e9:
        return "{:.2f}B".format(num / 1e9)
    elif abs(num) >= 1e6:
        return "{:.2f}M".format(num / 1e6)
    elif abs(num) >= 1e3:
        return "{:.2f}K".format(num / 1e3)
    else:
        return "{:.0f}".format(num)

# controlla se si è connessi al database
def has_connection():
    return "connection" in st.session_state.keys() and st.session_state["connection"] is not None

# pulsante per connettersi al database
def _connect_button():
    if st.sidebar.button("Connettiti al DB"):
        my_connection = connect_to_db()
        if my_connection is None:
            st.session_state["connection"] = None
            st.sidebar.error("❌ Errore nella connessione al DB")
        else:
            st.session_state["connection"] = my_connection
            st._rerun()

# pulsante per disconnettersi dal database
def _disconnect_button():
    if st.sidebar.button("Disconnettiti dal DB"):
        st.session_state["connection"] = None
        st._rerun()

# ui per connettersi / disconnettersi con il database
def connection_ui():
    if has_connection():
        st.sidebar.success("✅ Connesso al DB")
        _disconnect_button()
    else:
        st.sidebar.warning("⚠️ Non connesso al DB")
        _connect_button()

    if not has_connection():
        st.warning("⚠️ Connettiti al DB per visualizzare la pagina ⚠️")
        quit()
