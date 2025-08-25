import random

def Partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def RandomizedPartition(arr, low, high):
    randIndex = random.randint(low, high)
    arr[high], arr[randIndex] = arr[randIndex], arr[high]
    return Partition(arr, low, high)

def Quick(arr, low, high, k):
    if low <= high:
        pivotIndex = RandomizedPartition(arr, low, high)
        if pivotIndex == k:
            return arr[pivotIndex]
        elif pivotIndex < k:
            return Quick(arr, pivotIndex + 1, high, k)
        else:
            return Quick(arr, low, pivotIndex - 1, k)
    return None

def QuickSelect(arr, k):
    if k > len(arr) or k <= 0:
        return None
    return Quick(arr, 0, len(arr) - 1, k - 1)

arr_string = input()
k_string = input()
arr = list(map(int, arr_string.split()))
k = int(k_string)

print(QuickSelect(arr,k))