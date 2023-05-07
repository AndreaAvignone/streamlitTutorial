# Guida Live Coding

>Operazioni step-by-step per completare la dashboard sul DB *classicmodels*

## Presentazione progetto
* Cartella ```images```
* Cartella ```pages```
* Script utils ```utils/utils.py```
* File Home
Avviare il progetto 

```pipenv shell```

```pip install -r requirements.txt```

```python -m streamlit run 01_🏠_Home.py```

## Markdown e personalizzazione pagina
Nella pagina Home:

1. Inserire la configurazione di pagina
	```st.set_page_config()```
2. Dividere in colonne ```st.columns([3,2])```
3. Inserire titoli e sottotitoli ```st.title()``` e ```st.markdown()```
4. (Opzionale) Personalizzare il tema
5. Caricare l'immagine ```st.image()```
6. Inizializzare il session state ```st.session_state["connection"]```

## Connessione al Database
Definire le funzioni e i comandi per connettersi al database.

1. Includere le funzioni ```connect_db(dialect,username,password,host,dbname)``` e ```execute_query(conn,query)``` in *utils*
2. Aggiungere la funzione ```check_connection()``` a *utils* e richiamarla nella home
3. Visualizzare sulla sidebar il pulsante

## Setup della pagina Analisi
Definire la struttura della pagina
1. Definire i tab ```st.tabs(["Prodotti","Staff","Clienti"])```
2. Richiamare il check con comando per accedere al database attraverso il pulsante sulla sidebar:
```
if check_connection():
	pass
```

### Visualizzazione Prodotti
Panoramica delle principali informazioni riguardanti i prodotti in vendita. Creare la funzione ```def create_tab_prodotti(tab_prodotti):```

#### Metriche
Raccogliere le informazioni riguardante i pagamenti: *Importo totale, Pagamento Massimo, Pagamento Medio*.

SQL: ```SELECT SUM(amount) AS 'Total Amount', MAX(amount) AS 'Max Payment', AVG(amount) AS 'Average Payment' FROM payments:```

1. Aggiungere la funzione ```compact_format(num)``` a *utils* per una migliore visualizzazione dei numeri grandi.
2. Definire le 3 colonne con ```tab_prodotti.columns(3)```
3. Per ogni colonna definire la metrica specifica con ```col.metric()```

#### Panoramica Prodotti
Visualizzare i prodotti in vendita con widget di personalizzazione della query riguardo al *sorting*.
1. Definire il primo expander con la with notation e il flag `expanded=True` o `expanded=False` a piacimento
```
with tab_prodotti.expander("Panoramica Prodotti",True):
	# Codice
```
2. Definire le colonne all'interno dell'expander con le dimensioni per migliorare la resa grafica.
3. Definire il dizionario per il mapping di *DESC* e *ASC*
3. Includere il *radio button*, il *select box* e il *button*
```
prod_col1.radio()
prod_col2.selectbox()
prod_col1.button():
```
4. Eseguire la query e visualizzare il dataframe ottenuto

#### Pagamenti
Visualizzare l'andamento dei pagamenti con filtro temporale.

1. Definire il secondo expander con la with notation
```
with tab_prodotti.expander("Pagamenti",True):
	# Codice
```
2. Eseguire la query per definire gli estremi temporali. SQL: ```SELECT MIN(paymentDate), MAX(paymentDate) FROM payments```
3. Definire il widget per la selezione delle date, passando come valori di default la tupla ```(min_value,max_value)``` e i valori di massimo e minimo consentiti
```
st.date_input("Seleziona il range di date:",value=(min_value,max_value),
	min_value=min_value,max_value=max_value)
```
4. Eseguire la query con filtraggio delle date e create il dataframe
5. Verificare se il datafame è vuoto e gestire eventuali errori
```
st.warning("Nessun dato trovato.",icon='⚠️')
```
6. Modificare il tipo di dato per *paymentDate* e *Total Amount*
7. Fare il plot del risultato
```
st.line_chart(df_paymentDate,x="paymentDate",y='Total Amount')
```