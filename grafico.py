import csv
import matplotlib.pyplot as plt

# Nome del file CSV
file_name = "dati.csv"

# Liste vuote per memorizzare i dati
lunghezza_n = []
quickSelect = []
heapSelect = []
medianOfMedians = []

# Lettura dei dati dal file CSV
with open(file_name, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lunghezza_n.append(int(row["lunghezza n"]))
        quickSelect.append(float(row["quickSelect"]))
        heapSelect.append(float(row["heapSelect"]))
        medianOfMedians.append(float(row["medianOfMedians"]))

# Creazione del grafico
plt.plot(lunghezza_n, quickSelect, label='quickSelect')
plt.plot(lunghezza_n, heapSelect, label='heapSelect')
plt.plot(lunghezza_n, medianOfMedians, label='medianOfMedians')

# Aggiunta di titoli e etichette
plt.title('Tempi di esecuzione in funzione di lunghezza n')
plt.xlabel('lunghezza n')
plt.ylabel('Tempo (secondi)')
plt.legend()


plt.yscale('log')
plt.xscale('log')
# Mostra il grafico
plt.show()



