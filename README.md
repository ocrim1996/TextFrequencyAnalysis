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

$$ e = (e_{0},. . .,e_{k}) = \left(\frac{f_{0}}{n},. . .,\frac{f_{k}}{m}\right)\\
\text{dove:}\\
\bullet \quad \bm{f_{i}} := \text{ indica la frequenza del m-gramma i-esimo.}\\
\bullet \quad \bm{n} := \text{ indica la lunghezza del vettore di tutti gli m-grammi.} $$

$ a^2 $

Nel codice la funzione che calcola tale distribuzione empirica dei m-grammi è:

```python
def get_empirical_distribution(text, m):
	'''some code'''
```

## 3. Indice di Coincidenza ed Entropia della distribuzione dei m-grammi

Per quanto riguarda l’**indice di coincidenza delle distribuzioni dei m-grammi** è possibile notare che il testo analizzato è sufficientemente lungo tale da definire la formula come segue:

$$
\text{Dato } \bm{p_{i} = \frac{f_{i}}{n}} \quad \Longrightarrow \quad \text{Indice di Coincidenza } \,\, \bm{I_{c}(x) = \sum_{i=0}^{25}p_{i}^{2}}
$$

Nel codice la funzione che calcola tale indice di coincidenza delle distribuzioni dei m-grammi è:

```python
def get_coincidence_index(empirical_distribution):
	'''some code'''
```

Invece per quanto riguarda l’**entropia delle distribuzioni dei m-grammi** la formula utililizzata è quella dell’**entropia di Shannon**:

$$
\bm{H(p) = - \sum_{i=0}^{25}p_{i} \cdot \log(p_{i})}
$$

E nel codice la funzione che calcola tale entropia delle distribuzioni dei m-grammi è:

```python
def get_entropy(empirical_distribution):
	'''some code'''
```

