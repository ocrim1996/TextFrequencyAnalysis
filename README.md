# TextFrequencyAnalysis

Per svolgere questo esercizio sono state utilizzate le seguente librerie (che devono essere installate, prima di eseguire il codice):

- `pandas`
- `matplotlib`

Una volta eseguito il codice, l’utente può scegliere tra una lista di funzioni disponibili che vengono stampate a schermo, semplicemente inserendo il numero corrispondente.

![Schermata 2021-04-01 alle 15.46.48.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/F2D83C7F-B668-4BFB-B297-5D43AB4A3540/CCBD40A2-2DAA-461F-A583-52F72D2EE421_2)

Per semplicità il calcolo della distribuzione empirica e dell’indice di coincidenza e dell’entropia della distribuzione degli m-grammi è stato accorpato in un’unica funzione tra quelle che possono essere scelte dall’utente. Questo poichè per il calcolo dell’indice di coincidenza e dell’entropia è necessaria la distribuzione empirica.

## 1. Istogramma della Frequenza delle 26 lettere

Il programma prende in ingresso un file txt passatogli dall’utente (deve essere inserito il *path*) tramite la funzione Python:

```python
def get_text_file():
	file_name = input("...")
	'''some code'''
```

Il testo del file viene processato e viene effettuato il conteggio delle occorrenze di ciascuna lettera dell’alfabeto.

Il dizionario creato dalle frequenze viene utilizzato per generare un’**istogramma** tramite le funzioni della libreria `matplotlib`, in cui sulle ascisse sono riportate le lettere in ordine alfabetico invece sulle ordinate è riportata la relativa frequenza.

La funzione nel codice che genera l’istogramma è:

```python
def create_frequencies_histogram(data):
	counts = Counter(data)
	'''some code'''
```

In particolare nell’esercizio proposto era richiesto di mostrare i risultati ottenuti per il primo capitolo di “*Moby Dick*”. L’istogramma risultante è dunque il seguente:

![Schermata 2021-03-29 alle 15.02.09.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/F2D83C7F-B668-4BFB-B297-5D43AB4A3540/CC951B50-14EA-49A4-A6F4-1BDC8ACE4F5B_2)

## 2. Distribuzione Empirica dei m-grammi

Il programma prende in ingresso un file txt passatogli dall’utente (deve essere inserito il *path*) e da esso vengono generati tutti gli m-grammi tramite la seguente funzione:

```python
def generate_grams(text, m):
	'''some code'''
```

Una volta trovato gli m-grammi, è possibile calcolare la **distribuzione empirica dei m-grammi**, definita come segue:

![equation](https://latex.codecogs.com/gif.latex?e%20%3D%20%28e_%7B0%7D%2C.%20.%20.%2Ce_%7Bk%7D%29%20%3D%20%5Cleft%28%5Cfrac%7Bf_%7B0%7D%7D%7Bn%7D%2C.%20.%20.%2C%5Cfrac%7Bf_%7Bk%7D%7D%7Bm%7D%5Cright%29%5C%5C%20%5Ctext%7Bdove%3A%7D%5C%5C%20%5Cbullet%20%5Cquad%20f_%7Bi%7D%20%3A%3D%20%5Ctext%7B%20indica%20la%20frequenza%20del%20m-gramma%20i-esimo.%7D%5C%5C%20%5Cbullet%20%5Cquad%20n%20%3A%3D%20%5Ctext%7B%20indica%20la%20lunghezza%20del%20vettore%20di%20tutti%20gli%20m-grammi.%7D)

Nel codice la funzione che calcola tale distribuzione empirica dei m-grammi è:

```python
def get_empirical_distribution(text, m):
	'''some code'''
```

## 3. Indice di Coincidenza ed Entropia della distribuzione dei m-grammi

Per quanto riguarda l’**indice di coincidenza delle distribuzioni dei m-grammi** è possibile notare che il testo analizzato è sufficientemente lungo tale da definire la formula come segue:

![equation](https://latex.codecogs.com/gif.latex?%5Ctext%7BDato%20%7D%20p_%7Bi%7D%20%3D%20%5Cfrac%7Bf_%7Bi%7D%7D%7Bn%7D%20%5Cquad%20%5CLongrightarrow%20%5Cquad%20%5Ctext%7BIndice%20di%20Coincidenza%20%7D%20%5C%2C%5C%2C%20I_%7Bc%7D%28x%29%20%3D%20%5Csum_%7Bi%3D0%7D%5E%7B25%7Dp_%7Bi%7D%5E%7B2%7D)

Nel codice la funzione che calcola tale indice di coincidenza delle distribuzioni dei m-grammi è:

```python
def get_coincidence_index(empirical_distribution):
	'''some code'''
```

Invece per quanto riguarda l’**entropia delle distribuzioni dei m-grammi** la formula utililizzata è quella dell’**entropia di Shannon**:

![equation](https://latex.codecogs.com/gif.latex?H%28p%29%20%3D%20-%20%5Csum_%7Bi%3D0%7D%5E%7B25%7Dp_%7Bi%7D%20%5Ccdot%20%5Clog%28p_%7Bi%7D%29)

E nel codice la funzione che calcola tale entropia delle distribuzioni dei m-grammi è:

```python
def get_entropy(empirical_distribution):
	'''some code'''
```

## Run
To run the project:
```
python3 TextFrequencyAnalysis.py
```
