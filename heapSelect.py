import heapq

def HeapSelect(arr, k):
    
    # Costruzione della prima heap H1 (tempo lineare)
    H1 = arr
    heapq.heapify(H1)
      
    # Costruzione della seconda heap H2 contenente solo la radice di H1
    H2 = [(H1[0], 0)]

    for i in range(0, k - 1):
        # Estrai il nodo radice da H2
        node = heapq.heappop(H2)

        rootIndex = node[1]

        # Trova gli indici dei successori di node in H1
        leftChildIndex = 2 * rootIndex + 1
        rightChildIndex = 2 * rootIndex + 2

        # controlla se i successori esistono e li aggiunge in H2
        if leftChildIndex < len(H1):
            heapq.heappush(H2, (H1[leftChildIndex], leftChildIndex))
            

        if rightChildIndex < len(H1):
            heapq.heappush(H2, (H1[rightChildIndex], rightChildIndex))

    # Alla fine delle k-1 iterazioni, la radice di H2 sarà il k-esimo elemento più piccolo
    return H2[0][0]

print("Test1: " + str(HeapSelect([11,7,5,3],2)))
print("Test2: " + str(HeapSelect([7,3, 11, 3, 7, 0, 0, 5],6)))
print("Test3: " + str(HeapSelect([10],1)))
print("Test4: " + str(HeapSelect([-7,3, 3, 3, -100, 0, 11, 5, 0, 3, 100],2)))
print("Test5: " + str(HeapSelect([10, 9, 8, 7, 6, 5, 4, 3, 2,1, 0, -1, -2, -3, -4, -5, -6, -7, -8,-9, -10],21)))
print("Test6: " + str(HeapSelect([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],1)))
print("Test7: " + str(HeapSelect([1,1,1,1,1,1,0,0,0,0,0,0],1)))
print("Test8: " + str(HeapSelect([0,1,0,1,0,1,0,1,0,1,0,1],1)))
print("Test9: " + str(HeapSelect([2,2,2,2,2,2,2,2,2,2,2],2)))
print("Test10: " + str(HeapSelect([1,2,3,4,5,6,7,8,9,10],5)))