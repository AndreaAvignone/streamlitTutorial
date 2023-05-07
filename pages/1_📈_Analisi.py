import streamlit as st
from utils.utils import *
import pandas as pd

#ogni tab ha una funzione separata

def create_tab_prodotti(tab_prodotti):
    col1,col2,col3=tab_prodotti.columns(3)
    payment_info=execute_query(st.session_state["connection"],"SELECT SUM(amount) AS 'Total Amount', MAX(amount) AS 'Max Payment', AVG(amount) AS 'Average Payment' FROM payments;")
    #creare una struttura dati adatti dal risultato della query
    payment_info_dict= [dict(zip(payment_info.keys(), result)) for result in payment_info]
    #aggiungere come metriche orizzontali i parametri selezionati
    col1.metric('Importo Totale',f"$ {compact_format(payment_info_dict[0]['Total Amount'])}")
    col2.metric('Pagamento Massimo',f"$ {compact_format(payment_info_dict[0]['Max Payment'])}")
    col3.metric('Pagamento Medio',f"$ {compact_format(payment_info_dict[0]['Average Payment'])}")

    with tab_prodotti.expander("Panoramica Prodotti",True):
        #impostare le dimensioni desiderate, si possono generare colonne non utilizzate per definire gli spazi in modo più gradevole
        prod_col1,prod_col2,prod_col3=st.columns([3,3,6])
        #personalizzazione della query
        sort_param=prod_col1.radio("Ordina per:",["code","name","quantity","price"])
        sort_choice=prod_col2.selectbox("Ordine:",["Crescente","Decrescente"])

        #dizionario per il mapping tra SQL e le opzioni mostrate all'utente
        sort_dict={"Crescente": "ASC","Decrescente":"DESC"}
        
        #il type del button è prettamente per gusto grafico
        if prod_col1.button("Mostra",type='primary'):
            #spezzare la query in due stringhe per facilitare la leggibilità del codice: una fissa e l'altra che si adatta alle opzioni scelte
            query_base="SELECT productCode AS 'code', productName AS 'name', quantityInStock AS quantity, buyPrice AS price, MSRP FROM products"
            query_sort=f"ORDER BY {sort_param} {sort_dict[sort_choice]};"
            prodotti=execute_query(st.session_state["connection"],query_base+" "+query_sort)
            #creazione automatica del dataframe
            df_prodotti=pd.DataFrame(prodotti)
            st.dataframe(df_prodotti,use_container_width=True)

    with tab_prodotti.expander("Pagamenti",True):
        #abilitare un filtraggio per range di date su cui costruire l'interrogazione
        #prima effettuare una query per avere il range effettivo di valori nel database
        query="SELECT MIN(paymentDate), MAX(paymentDate) FROM payments"
        date=execute_query(st.session_state["connection"],query)
        min_max=[dict(zip(date.keys(), result)) for result in date]

        #sappiamo che ci viene restituita una sola tupla
        min_value=min_max[0]['MIN(paymentDate)']
        max_value=min_max[0]['MAX(paymentDate)']
        #specificare min_value e max_value per impostare il widget con il range di date
        date_range=st.date_input("Seleziona il range di date:",value=(min_value,max_value),min_value=min_value,max_value=max_value)
        query=f"SELECT paymentDate, SUM(amount) as 'Total Amount' FROM payments WHERE paymentDate >'{date_range[0]}' AND paymentDate <'{date_range[1]}' GROUP BY paymentDate"
        paymentsDate=execute_query(st.session_state["connection"],query)
        df_paymentDate=pd.DataFrame(paymentsDate)

        #verificare che ci siano dati nel periodo selezionato
        if df_paymentDate.empty:
            st.warning("⚠️ Nessun dato trovato.")
        else:
            #trasformare in float e date type
            df_paymentDate['Total Amount']=df_paymentDate['Total Amount'].astype(float)
            df_paymentDate['paymentDate']=pd.to_datetime(df_paymentDate['paymentDate'])

            st.write("Periodo",date_range[0],'-',date_range[1])
            st.line_chart(df_paymentDate,x="paymentDate",y='Total Amount')
    
def create_tab_staff(tab_staff):
    #si può usare mappings() e first() (aspettandoci una sola tupla) per ottenere i dati desiderati dal risultato della query
    #trovare nome e cognome del presidente e del VP Sales
    president_query="SELECT lastName,firstName FROM employees WHERE jobTitle='President'"
    president=execute_query(st.session_state["connection"],president_query).mappings().first()
    vp_sales_query="SELECT lastName,firstName FROM employees WHERE jobTitle='VP Sales'"
    vp_sales=execute_query(st.session_state["connection"],vp_sales_query).mappings().first()

    col1,col2,col3=tab_staff.columns(3)
    col1.markdown(f"#### :blue[PRESIDENT:] {president['firstName']} {president['lastName']}")
    col3.markdown(f"#### :orange[VP SALES:] {vp_sales['firstName']} {vp_sales['lastName']}")

    #ordine non presente nel bar chart
    staff_query="SELECT jobTitle,COUNT(*) as numDipendenti FROM employees GROUP BY jobTitle ORDER BY numDipendenti DESC;"
    staff=execute_query(st.session_state["connection"],staff_query)
    df_staff=pd.DataFrame(staff)
    tab_staff.markdown("### Componenti Staff")
    #specificare quali colonne del dataframe devono essere l'asse x o y
    tab_staff.bar_chart(df_staff,x='jobTitle',y='numDipendenti',use_container_width=True)

def create_tab_clienti(tab_clienti):
    col1,col2=tab_clienti.columns(2)
    query="SELECT COUNT(*) as 'numeroClienti',country FROM customers GROUP by country order by `numeroClienti` DESC;"
    result=execute_query(st.session_state["connection"],query)
    df=pd.DataFrame(result)
    col1.subheader("Distribuzione clienti nel mondo")
    #impostare un'altezza uguale per i vari elementi può rendere il risultato più curato
    col1.dataframe(df,use_container_width=True,height=350)

    query="SELECT customername, state, creditLimit FROM customers WHERE country = 'USA' AND creditLimit > 100000 ORDER BY creditLimit DESC;"
    result=execute_query(st.session_state["connection"],query)
    df=pd.DataFrame(result)
    col2.subheader("Clienti con maggior *credit limit* negli USA")
    col2.dataframe(df,use_container_width=True,height=350)

if __name__ == "__main__":
    st.title("📈 Analisi")

    #creazione dei tab distinti
    tab_prodotti,tab_staff,tab_clienti=st.tabs(["Prodotti","Staff","Clienti"])
    
    #se la connessione al DB è avvenuta, mostrare i dati
    if check_connection():
        create_tab_prodotti(tab_prodotti=tab_prodotti)
        create_tab_staff(tab_staff=tab_staff)
        create_tab_clienti(tab_clienti=tab_clienti)