import math

def MedianOfMedians(arr, k):
    _MedianOfMedians(arr, k - 1)

def _MedianOfMedians(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Divide l'array in blocchi di dimensione 5
    blocks = [arr[i:i+5] for i in range(0, len(arr), 5)]

    # Calcola le mediane di ogni blocco
    medians = [sorted(block)[len(block)//2] for block in blocks]

    # Trova la mediana delle mediane dei blocchi
    pivot = _MedianOfMedians(medians, len(medians)//2)

    # Partiziona l'array attorno al pivot
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    pivotCount = arr.count(pivot)

    # Calcola le posizioni
    leftLen = len(left)
    pivotLen = len(arr) - leftLen - len(right)
    # Ricorsione
    if k < leftLen:
        return _MedianOfMedians(left, k)
    elif k < leftLen + pivotLen:
        return pivot
    else:
        return _MedianOfMedians(right, k - leftLen - pivotCount)



'''def ordina_blocchi_di_5(arr):
    n = len(arr)
    
    # Itera su blocchi di 5 elementi
    for i in range(0, n, 5):
        # Trova il limite del blocco corrente
        fine_blocco = min(i + 5, n)
        # Ordina il blocco corrente in place
        arr[i:fine_blocco] = sorted(arr[i:fine_blocco])

def trova_mediana_ricorsiva(arr):
    ordina_blocchi_di_5(arr)
    n = len(arr)
    
    # Se l'array è abbastanza piccolo, calcola direttamente la mediana
    if n <= 5:
        indice_centrale = (n - 1) // 2
        return arr[indice_centrale]
    
    # Altrimenti, calcola le mediane dei blocchi di 5 elementi
    mediane_blocchi = []
    for i in range(0, n, 5):
        fine_blocco = min(i + 5, n)
        blocco = arr[i:fine_blocco]
        indice_centrale = (len(blocco) - 1) // 2
        valore_centrale = blocco[indice_centrale]
        mediane_blocchi.append(valore_centrale)
    
    # Trova la mediana delle mediane
    mediana_delle_mediane = trova_mediana_ricorsiva(mediane_blocchi)
    
    return mediana_delle_mediane

def partition(arr, start, end, pivot):
    # Trova l'indice del pivot
    pivot_index = arr.index(pivot, start, end + 1)
    # Sposta il pivot alla fine dell'array
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    # Inizializza l'indice del partitore
    partition_index = start
    
    # Itera attraverso l'array
    for i in range(start, end):
        # Se l'elemento corrente è minore o uguale al pivot, lo scambia con l'elemento nella posizione del partitore
        if arr[i] <= pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1
    
    # Sposta il pivot nella sua posizione finale
    arr[partition_index], arr[end] = arr[end], arr[partition_index]
    
    # Restituisci l'indice del pivot dopo il partizionamento
    return partition_index

def medianOfMedians(arr, start, end, k):
    if start == end:
        return arr[start]
    
    M = trova_mediana_ricorsiva(arr[start:end + 1])
    pivot = partition(arr, start, end, M)
    
    if k == pivot:
        return arr[pivot]
    elif k < pivot:
        return medianOfMedians(arr, start, pivot - 1, k)
    else:
        return medianOfMedians(arr, pivot + 1, end, k)

def MedianOfMedians(arr, k):
    return medianOfMedians(arr, 0, len(arr) - 1, k-1)
'''