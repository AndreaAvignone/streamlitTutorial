import streamlit as st
import datetime

st.set_page_config(
    page_title="La mia App",
    layout="wide",
    initial_sidebar_state="expanded",

)

st.sidebar.title("Streamlit :red[Tutorial]")
st.sidebar.header(":blue[Basi di dati]")
st.sidebar.subheader("🧑‍💻️ Applicazioni web")

with st.form("form"):
   st.subheader("Form di inserimento dati")
   product=st.text_input("Nome prodotto:")
   data=st.date_input("Data di uscita:",value=datetime.datetime(2023,1,1))

   price = st.slider("Prezzo prodotto :blue[(euro)]:",1,2000)
   status = st.radio("Status:",("Disponibile","Non Disponibile"))

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Hai inserito questo prodotto:")
    st.write({"Prodotto": product, "Data di uscita": data.strftime('%d/%m/%Y'), "Prezzo": price, "Status":status})
