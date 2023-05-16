# Streamlit Tutorial: Live Coding

## Installazione completa su Windows
Vai [qui](readme_windows.md) per una guida completa all'installazione su Windows

## Installazione generica

Creazione di un'applicazione web multi-page in Streamlit interagendo con un database MySQL per visualizzare e aggiungere dati.

```git clone https://github.com/AndreaAvignone/streamlitTutorial.git```

## Warm up 
* Branch *live_coding* è il punto di partenza, branch *live_coding_complete* è l'applicazione finale, branch *base* come starting point per un nuovo progetto generico.
* Per ulteriori informazioni riguardo al database far riferimento a https://www.mysqltutorial.org/mysql-sample-database.aspx.
* Per la guida passo-passo sulla creazione dell'applicazione, dar riferimento a *guide.md*
* Per aggiungere emojii utilizzare https://emojifinder.com con copia-incolla.

## Environment
### Per ulteriori informazioni riguardo ai diversi OS e Streamlit: https://docs.streamlit.io/library/get-started/installation

#### 1. Installare l'environment MySQL (con Docker e Docker-compose https://github.com/AndreaAvignone/mysql-docker.git)
#### 2. Creare un nuovo virtual environment Python (e.g. *pipenv*).

Installare pipenv:
```
pip install pipenv
```
Avviare il virtual env:
```
pipenv shell
```
Installare le dependencies:
```
pip install -r requirements.txt

```
#### 3. Verificare l'installazione di streamlit:
```
streamlit hello
```

Per fermare:

```Ctrl + C```

#### 4. Lanciare l'applicazione:
```
python -m streamlit run 01_🏠_Home.py
```
O direttamente con il comando *streamlit*:
```
streamlit run 01_🏠_Home.py
```
Per evitare che si apri in automatico il browser:
```
streamlit run 01_🏠_Home.py --server.headless true
```
