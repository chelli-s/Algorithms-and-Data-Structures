import time
import random
import math
import copy
import csv
from quickSelect import QuickSelect
from heapSelect import HeapSelect
from medianaDiMediane import MedianOfMedians

# Funzione per stimare la risoluzione del clock di sistema
def resolution():
    start = time.perf_counter()
    while time.perf_counter() == start:
        pass
    stop = time.perf_counter()
    return stop - start

# Funzione per calcolare il tempo minimo misurabile
def TMin(resolution, E):
    return resolution * (1/E + 1)

# Algoritmo da testare
def testAlgorithm(i):
    match i:
        case 0:
            return QuickSelect
        case 1:
            return HeapSelect
        case 2:
            return MedianOfMedians
            
# Genera un array di n elementi con valori casuali
def generateInput(n):
    arr = [random.randint(0, 10000000) for _ in range(n)]
    return arr

'''
# Generazione dei parametri k random
def generateKValues(n, numK):
    # Genera numK valori k casuali tra 1 e n
    return [random.randint(1, n) for _ in range(numK)]    
'''
def generateKValues(n, numK):
    if numK <= 1:
        return [n // 2] 
    
    step = n // (numK - 1)
    return [max(i * step, 1) for i in range(numK)]

# Funzione per calcolare il tempo medio di esecuzione dell'algoritmo
def average_execution_time(algorithm, n, numSamples, numK, TMin):
    totalTime = 0
    totalExecutions = 0
    
    for _ in range(numSamples):
        arr = generateInput(n)
        k_values = generateKValues(n, numK)
        
        for k in k_values:
            arr_copy = copy.deepcopy(arr)
            if k == k_values[0]:
                startTime = time.perf_counter()

            result = algorithm(arr, k)

            if k == k_values[numK-1]:
                endTime = time.perf_counter()
                elapsedTime = endTime - startTime
            
                if elapsedTime >= TMin:
                    totalTime += elapsedTime
                else:
                    totalTime += TMin
            
            totalExecutions += 1
    
    return totalTime / totalExecutions
# Parametri
tempoInizioEseuzione = time.perf_counter()
contatore = 0
A = 100
B = 10**(3 / 99)
E = 0.01  # Errore relativo massimo ammissibile
numSamples = 10 # numero di array da testare per ogni lunghezza n
numK = 1  # Numero di valori k da testare per ogni array

# Generazione delle lunghezze n secondo una serie geometrica
lengths = [math.floor(A * math.pow(B, i)) for i in range(100)]

# Stimare la risoluzione del clock di sistema
R = resolution()

# Calcolare il tempo minimo misurabile
TMin = TMin(R, E)

file_name = "dati.csv"

with open(file_name, 'w', newline='') as csvfile:
    fieldnames = ["lunghezza n", "quickSelect", "heapSelect", "medianOfMedians"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    
# Calcolare il tempo medio di esecuzione per ogni lunghezza n
    for n in lengths:

        contatore = contatore + 1
        print(f"Lunghezza n = {n}, Test numero {contatore}")
        for i in range(0, 3):
            Algorithm = testAlgorithm(i)
            alg= ''
            averageTime = average_execution_time(Algorithm, n, numSamples,numK,TMin)

            if(i == 0):
                quickSelect_time = averageTime
            elif (i == 1):
                heapSelect_time = averageTime
            elif(i == 2):
                medianOfMedians_time = averageTime

            print(f"Tempo medio di esecuzione di {Algorithm.__name__}: {averageTime:.6f} secondi")

        row = {
                    "lunghezza n": n,
                    "quickSelect": quickSelect_time,
                    "heapSelect": heapSelect_time,
                    "medianOfMedians": medianOfMedians_time
                }

        writer.writerow(row)
        print("-----------------------------")
        if(n == 100000):
            tempoFineEsecuzione = time.perf_counter()
            print(f"tempo totale: {tempoFineEsecuzione - tempoInizioEseuzione:.6f} secondi")

