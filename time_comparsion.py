# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 01:58:16 2023

@author: likhith
"""

import random
import time

# Generate input data
data = [random.randint(1, 1000) for i in range(1000)]

# Define sorting algorithms
def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [x for x in data[1:] if x <= pivot]
        greater = [x for x in data[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Time the algorithms
start = time.time()
bubble_sort(data)
end = time.time()
bubble_sort_time = end - start

start = time.time()
quick_sort(data)
end = time.time()
quick_sort_time = end - start

# Print the results
print("Bubble sort time: %.5f seconds" % bubble_sort_time)
print("Quick sort time: %.5f seconds" % quick_sort_time)


import random
import time

# Generate input data
data = [random.randint(1, 100) for i in range(1000)]

# Merge Sort
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        # Recursive calls to sort left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge sorted left and right halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

# Selection Sort
def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]



# Time the algorithms
start = time.time()
merge_sort(data)
end = time.time()
merge_sort_time = end - start

start = time.time()
selection_sort(data)
end = time.time()
selection_sort_time = end - start


# Print the results
print("Merge sort time: %.5f seconds" % merge_sort_time)
print("Selection sort time: %.5f seconds" % selection_sort_time)


import random
import time

# Generate input data
data = [random.randint(1, 100) for i in range(1000)]

# Insertion Sort
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

# Time the algorithm
start = time.time()
insertion_sort(data)
end = time.time()
insertion_sort_time = end - start

# Print the result
print("Insertion sort time: %.5f seconds" % insertion_sort_time)
