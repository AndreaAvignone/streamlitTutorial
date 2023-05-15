# Guida Live Coding

>Operazioni step-by-step per completare la dashboard sul DB *classicmodels*

## Presentazione progetto
* Cartella ```images```
* Cartella ```pages```
* Script utils ```utils/utils.py```
* File ```01_🏠_Home``` (homepage)

### Avviare il progetto 
``` pip install pipenv```

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
Panoramica delle principali informazioni riguardanti i prodotti in vendita. Creare la funzione ```create_tab_prodotti(tab_prodotti)```
e aggiungerla al *main*:
```
if check_connection():
    create_tab_prodotti(tab_prodotti=tab_prodotti)
```

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

### Staff
Visualizzare brevemente informazioni sui dipendenti. Creare la funzione ```create_tab_prodotti(tab_prodotti)```
e aggiungerla al *main*:
```
if check_connection():
    create_tab_prodotti(tab_prodotti=tab_prodotti)
    create_tab_staff(tab_staff=tab_staff)
```
1. Recuperare il nome e cognome di *President* e *VP Sales*. SQL: 
```
SELECT lastName,firstName FROM employees WHERE jobTitle='President'

SELECT lastName,firstName FROM employees WHERE jobTitle='VP Sales'
```
2. Personalizzare il markdown
3. Recuperare le informazioni riguardo la distribuzione dei dipendenti nei vari ruoli. SQL: ```SELECT jobTitle,COUNT(*) as numDipendenti FROM employees GROUP BY jobTitle ORDER BY numDipendenti DESC;```

4. Generare il dataframe e plottare il risultato:
```
df_staff=pd.DataFrame(staff)
tab_staff.bar_chart(df_staff,x='jobTitle',y='numDipendenti',use_container_width=True)
```

### Clienti
Visualizzare brevemente le informazioni sui clienti in relazione al paese di origine.
Creare la funzione ```create_tab_clienti(tab_prodotti)```
e aggiungerla al *main*:
```
if check_connection():
    create_tab_prodotti(tab_prodotti=tab_prodotti)
    create_tab_staff(tab_staff=tab_staff)
    create_tab_clienti(tab_clienti=tab_clienti)
```
1. Creare le colonne nel tab clienti ```col1,col2=tab_clienti.columns(2)```
2. Utilizzare il subheader per specificare il ruolo di ogni colonna
 ```
col1.subheader("Distribuzione clienti nel mondo")
col2.subheader("Clienti con maggior *credit limit* negli USA")
 ```
 3. Recuperare le informazioni sull'origine dei clienti ordinandoli per numero. SQL:```
 	SELECT COUNT(*) as 'numeroClienti',country FROM customers GROUP by country order by ``numeroClienti` DESC;```
 4. Recuperare le informazioni sui clienti **USA** con **creditLimit > 100000** ordinandoli in ordine decrescente. (N.B. questi valori potrebbero essere ulteriori input dell'utente in futuro)
5. Impostare un'altezza identica per i due df e visualizzarli
```
col1.dataframe(df,use_container_width=True,height=350)
col2.dataframe(df,use_container_width=True,height=350)
```


## Aggiungere un prodotto
Creare un form per aggiungere un nuovo prodotto al DB.
### Creazione del form
Creare la funzione ```create_form()``` e richiamarla nel main 
```
if check_connection():
	create_form()
```
Includere il widget del form a cui aggiungere i vari parametri:
```
with st.form("Nuovo Prodotto"):
	st.header(":blue[Aggiungi prodotto:]")
```
Creare le funzioni ```get_info()``` e ```get_list(attributo)``` che recuperano tutti i valori distinti possibili per un dato attributo e li restituisce come lista. Ottenere così la lista di *categorie, scale, venditori* all'interno del form per creare le opzioni tra cui scegliere. 
#### Widget di input
Inserire i widget per ricevere come input *code, nome,categoria,scala,venditore,descerizione,quantità,prezzo,MSRP* utilizzando:
```
st.text_input("",placeholder="")
st.selectbox("",)
st.text_area("",placeholder="")
st.slider("",,)
st.number_input("",)
```
Creare il dizionario che raccolga i parametri e **includere il submit button**:
```
insert_dict= {"productCode":code, "productName":nome,"productLine":categoria,"productScale":scala,"productVendor":venditore,"productDescription":descrizione,"quantityInStock":qta,"buyPrice":prezzo,"MSRP":msrp}
submitted =st.form_submit_button("Submit",type='primary')
```
#### Eseguire l'*insert*
Definire la funzione ```insert(prod_dict)``` che si occupa di eseguire la query e la funzione ```check_info(prod_dict)``` per controllare che non ci siano campi testuali lasciati vuoti.

#### Verifica che l'inserimento sia andato a buon fine

Fuori dal form verificare che, quando il tasto *submit* viene premuto, sia stato possibile completare l'operazione con successo e printare lo status:
```
 if submitted:
        #verificare che l'inserimento sia andato a buon fine oppure no
        if insert(insert_dict):
            st.success("Hai inserito questo prodotto: ",icon='✅ ')
            st.write(insert_dict)
        else:
            st.error("Impossibile aggiungere il prodotto.",icon='⚠️')
```

