import pandas as pd

# Imposta il percorso del tuo file CSV
percorso_file_csv = 'dataset_climatico.csv'

# Importa il dataset come DataFrame
df = pd.read_csv(percorso_file_csv)

# Ad esempio, puoi visualizzare le prime righe del DataFrame
print(df.head())

#Normalizzazione dei Dati:
#Pulire i dati per rimuovere eventuali valori mancanti o errati. 
df.dropna(inplace=True)
#Applicare la normalizzazione Z-score alla temperatura_media, precipitazioni, umidità e velocità_vento per standardizzarle.
colonnes_da_standardizzare = ['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']

# Calcola la media e la deviazione standard di ciascuna colonna
for colonna in colonnes_da_standardizzare:
    media = df[colonna].mean()
    deviazione_standard = df[colonna].std()
    
    # Standardizzazione Z-score: ((x - media) / deviazione standard)
    df[colonna] = (df[colonna] - media) / deviazione_standard

#Analisi Esplorativa dei Dati:
import matplotlib.pyplot as plt
import seaborn as sns

# Calcola statistiche descrittive
desc_stats = df.describe()

# Stampa le statistiche descrittive
print(desc_stats)

sns.set(style="whitegrid")

# Crea una heatmap con il risultato di describe
plt.figure(figsize=(12, 6))
sns.heatmap(desc_stats, annot=True, fmt=".2f", cmap='coolwarm', linewidths=.5, cbar=False)
plt.title('Descrizione del Dataset')
plt.savefig("Descrizione_dataset.png")
plt.show()

# Crea un istogramma per ogni variabile
df.hist(bins=20, figsize=(12, 8))
plt.suptitle('Distribuzione delle Variabili Normalizzate')
plt.savefig('istogramma.png')
plt.show()

# Crea un box plot per ogni variabile
df.boxplot(figsize=(12, 8))
plt.title('Box Plot delle Variabili Normalizzate')
plt.savefig('box_plot.png')
plt.show()

# Calcola la matrice di correlazione
# Seleziona le colonne di interesse
colonne_di_interesse = df.iloc[:, [2, 3]]

# Calcola la matrice di correlazione
matrice_correlazione = colonne_di_interesse.corr()

# Visualizza la matrice di correlazione come heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(matrice_correlazione, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlazione tra Umidità e Precipitazioni')
plt.savefig('correlazione_umidita_precipitazioni.png')
plt.show()

# Sostituisci 'temperatura_media' e 'precipitazioni' con i nomi delle colonne effettive nel tuo DataFrame
variabile1 = colonne_di_interesse.columns[0]
variabile2 = colonne_di_interesse.columns[1]

# Utilizza regplot per visualizzare la relazione lineare tra le variabili
sns.regplot(x=variabile1, y=variabile2, data=colonne_di_interesse)
plt.title(f'Regplot tra {variabile1} e {variabile2}')
plt.savefig('corr_umidità_precipitazioni.png')
plt.show()


