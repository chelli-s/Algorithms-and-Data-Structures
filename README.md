# Algorithms-and-Data-Structures

Project Description

The goal of this laboratory project is to verify that students are able to design, implement, and analyze the complexity of a program using the tools and techniques presented during the Algorithms and Data Structures course.

The programs developed must solve classic computational problems and be formally correct. Each laboratory project consists of:

Implementing one or more programs to solve a given computational problem.

Empirically estimating the complexity of the programs based on the input size and any other relevant parameters.

Writing a report discussing implementation choices and providing a detailed analysis of the complexity estimation.

Project Objectives – Part 1

The first part of the project focuses on implementing and analyzing the average execution time of three selection algorithms, which compute the k-th smallest element in an unsorted vector of integers. The algorithms are:

1. Quick Select

A variant of the Quick Sort algorithm.

Each recursive call on an interval [i, j] terminates in constant time if k is not in [i, j].

Time complexity: Θ(n²) in the worst case, O(n) on average, where n is the vector size.

2. Heap Select

Uses two min-heaps, H1 and H2.

H1 is built from the input vector in linear time and remains unchanged.

H2 initially contains the root of H1. At each iteration i (from 1 to k−1), the root of H2 is extracted, and its children in H1 are inserted into H2. After k−1 iterations, the root of H2 is the k-th smallest element.

Time complexity: O(n + k log k) for both worst and average cases.

For small k, Heap Select may outperform Quick Select in the worst case.

3. Median-of-Medians Select

Divides the input vector into blocks of 5 elements.

Computes the median of each block.

Recursively computes the median of medians M.

Partitions the array around M (using a Quick Sort partition variant) and recursively searches the left or right subarray depending on k.

Can be implemented in-place for higher efficiency.

Time and space complexity: Θ(n) in the worst case.

Submission Requirements

Implementation:

Implement the three algorithms in a programming language of your choice (C, C++, Java, etc.).

Programs must be formally correct (inputs are guaranteed to be valid: non-empty vectors and 1 ≤ k ≤ n).

Verification is done using Virtual Programming Laboratory (VPL) modules provided by the instructors.

Empirical Time Analysis:

Estimate the average execution times for each algorithm as the vector size n varies (and optionally the parameter k).

Input vectors should be generated pseudo-randomly (integers, possibly negative).

Measure execution times with a maximum relative error of 1% using a monotonic stopwatch.

For each algorithm, report a sequence of records in the format:

`N K T1 D1 T2 D2 T3 D3`


where N = vector size, K = k value, Ti = mean execution time of algorithm i, Di = standard deviation.

Recommended sample sizes: 100 vectors with N varying from 100 to 5,000,000 using exponential or geometric distribution.

Report:

Present and discuss the results of the time analysis in a PDF report.

Include key implementation choices, graphical comparisons, and complexity analysis.

Graphs should include both linear (N vs t(N)) and log-log (log(N) vs log(t(N))) scales.

The report should be concise (a few dozen pages is sufficient).
