import pandas as pd
import matplotlib.pyplot as plt

# Scarica il dataset
url = "https://github.com/plotly/datasets/raw/master/stockdata.csv"
dataset = pd.read_csv(url)
print(dataset)
print(dataset.columns) #stampa solo i nomi delle colonne

msft_data = dataset['MSFT']                      #estraggo i dati dalla colonna MSFT
plt.figure(figsize=(10, 6))                      #dimensione del grafico
plt.plot(dataset.index, msft_data, label='MSFT') 
plt.title('Andamento Azioni Microsoft')          #Titolo grafico
plt.xlabel('Data (indice)')                      #Titolo asse x
plt.ylabel('Prezzo Azioni')                      #Titolo asse y
plt.legend()                                     #leggenda
plt.show()

#Estrai le prime 5 righe
prime_5_righe = dataset.head(5)
prime_5_date = prime_5_righe.iloc[:, 0] #la prima colonna del dataset
prime_5_msft = prime_5_righe['MSFT'] 

# Crea un grafico con le prime 5 righe
plt.figure(figsize=(8, 4))
plt.plot(prime_5_date, prime_5_msft, marker='o', linestyle='-', color='b')
plt.title('Prime 5 Righe - Azioni Microsoft (MSFT)')
plt.xlabel('Data')
plt.ylabel('Prezzo Azioni')
plt.show()

# Estrai le ultime 5 righe della colonna MSFT e della prima colonna come data
ultime_5_righe = dataset.tail(5)
ultime_5_date = ultime_5_righe.iloc[:, 0]  # La prima colonna del dataset
ultime_5_msft = ultime_5_righe['MSFT']

# Crea un grafico con le ultime 5 righe
plt.figure(figsize=(8, 4))
plt.plot(ultime_5_date, ultime_5_msft, marker='o', linestyle='-', color='g')
plt.title('Ultime 5 Righe - Azioni Microsoft (MSFT)')
plt.xlabel('Data')
plt.ylabel('Prezzo Azioni')
plt.show()


# Estrai le prime 20 istanze della colonna AAPL
aapl_data_first_20 = dataset['AAPL'].head(20)

# Visualizza il grafico delle azioni di Apple
plt.figure(figsize=(10, 6))
plt.plot(aapl_data_first_20, marker='o', linestyle='--', color='red', markerfacecolor='black', linewidth=2)        
plt.title('Azioni Apple')
plt.xlabel('Data')
plt.ylabel('Valore')
plt.show()


