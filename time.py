from HeapSelect import heapSelect
from QuickSelect import quickSelect
from partition3WayRandomized import quickSelectRandomized
from MedianOfMediansSelect import medianOfMediansSelect
from DisegnaGrafico import disegnaGrafico
import random
import time
import os
#################################### ! DISCLAIMER ! ###################################################################
# THE FOLLOWING BENCHMARK IS NOT DESIGNED TO RUN ON WINDOWS.
# IT HAS BEEN TESTED ON MACOSX AND UBUNTU, SO WE DO NOT RECOMMEND EXECUTION ON DIFFERENT OPERATING SYSTEMS.
# IN PARTICULAR, THE BENCHMARK EXECUTION TIMES ON WINDOWS MAY BE EXTREMELY HIGHER.
# ALSO, THE GRAPH WILL NOT BE GENERATED.
'''
minimumMeasurableTime:
Returns the minimum measurable time by the time.monotonic() counter.
'''
def minimumMeasurableTime():
startMeasurement = time.monotonic()
while time.monotonic() == startMeasurement:
pass
endMeasurement = time.monotonic()
return endMeasurement - startMeasurement
'''
measureTimes:
1) Accurately measures the execution time of each algorithm in the algoritmiDiSelezione list.
2) Ensures a relative error less than 1%.
3) Adds the average measured time to the average time counter of each executed algorithm.
'''
tMinMeasurable = minimumMeasurableTime() * (1 + (1 / 0.01))
# max_rel_error = 1% = 0.01
def measureTimes(array, k, algoritmiDiSelezione, averageTimes):
for i, func in enumerate(algoritmiDiSelezione):
count = 0
startTime = time.monotonic()
while time.monotonic() - startTime < tMinMeasurable:
func(array.copy(), k)
count += 1
duration = time.monotonic() - startTime
averageTimes[i] += (duration / count)
'''
benchmark:
1) Measures the average execution time of each algorithm in the algoritmiDiSelezione list.
2) Generates passiSuccessione(100) arrays of increasing size following a geometric series.
The size of the arrays ranges from 100 to 100000.
3) At each step, testPerOgniN(500) tests are performed with random k to ensure that the execution times of the algorithms are average.
4) In each test, the array of predetermined size is filled with random values in a range [-1000,1000].
5) In each test, the execution time is measured.
6) At the end of the tests, the average times for that step of the series are saved in a list of lists averageTimes.
7) At each step, after performing testPerOgniN(500), the size of the array used for that step is saved.
8) At the end of the 100 steps, the average time data is saved in separate files. One for each algorithm.
9) Finally, the function that draws the graph using the data from the generated files is called.
'''
# List of selection algorithms
algoritmiDiSelezione = [quickSelect, quickSelectRandomized, heapSelect, medianOfMediansSelect]
nomi_algoritmiDiSelezione = ["QuickSelect", "QuickSelectRandomizedPTW", "HeapSelect", "MedianOfMediansSelect"]
# Initialize the lists for average times
averageTimes = [[] for _ in algoritmiDiSelezione]
# list of as many lists as there are selection algorithms
generatedArraySizes = []
def benchmark():
A = 100 # Start of the geometric series
B = (100000 / 100) ** (1 / 99)
# Calculate B to get final n of 100000 (99th root)
passiSuccessione = 100
testPerOgniN = 1
for i in range(passiSuccessione):
arraySize = int(A * (B ** i))
print("Executing step {} / {} of the series \t len(A) : {}".format(i+1, passiSuccessione, arraySize))
# Initialize average times for this array size
stepAverageTimes = [0] * len(algoritmiDiSelezione)
for _ in range(testPerOgniN):
array = [random.randint(-1000, 1000) for _ in range(arraySize)]
k = random.randint(1, arraySize)
measureTimes(array, k, algoritmiDiSelezione, stepAverageTimes)
for j in range(len(algoritmiDiSelezione)):
averageTimes[j].append(stepAverageTimes[j] / testPerOgniN)
generatedArraySizes.append(arraySize)
# Set the working directory relative to the location of this file
directoryPath = os.path.join(os.path.dirname(__file__), 'RisultatiBenchmark')
# Check if the folder exists, otherwise create it
if not os.path.exists(directoryPath):
os.makedirs(directoryPath)
# Build the file paths relative to this directory
arraySizesPath = os.path.join(directoryPath, 'dimensioniArray.txt')
# Write the size of each generated array to a file.
with open(arraySizesPath, 'w') as f:
for n in generatedArraySizes:
f.write(f"{n}\n")# Write the execution time results to separate text files. One for each algorithm.
for i, name in enumerate(nomi_algoritmiDiSelezione):
filePath = os.path.join(directoryPath, f'tempi{name}.txt')
with open(filePath, 'w') as f:
for time in averageTimes[i]:
f.write(f"{time}\n")
print("Benchmark started")
benchmark()
print("Benchmark completed. Creating the graph.")
disegnaGrafico()
