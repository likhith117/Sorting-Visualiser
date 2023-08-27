# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 01:58:16 100023

@author: likhith
"""

import random
import time

data = [random.randint(1,1000) for i in range(2000)]

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
data = [random.randint(1, 2000) for i in range(2000)]

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
data = [random.randint(1, 2000) for i in range(2000)]

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

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

    return arr


def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])


def subsortalgo(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                left=arr[start:midpoint + 1],
                right=arr[midpoint + 1:end + 1]
            )
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr

import random
import time

# Generate input data
data = [random.randint(1, 1000) for i in range(1000)]

# Define subsortalgo algorithm
def subsortalgo(data):
    # Set the minimum run size
    minrun = 32
    
    # Get the length of the data
    n = len(data)
    
    # Determine the runs
    runs = []
    i = 0
    while i < n:
        run = [data[i]]
        if i == n - 1:
            runs.append(run)
            break
        j = i + 1
        if data[j] < data[i]:
            while j < n - 1 and data[j] < data[j + 1]:
                j += 1
            run += data[i + 1:j + 1]
            run.reverse()
        else:
            while j < n - 1 and data[j] >= data[j + 1]:
                j += 1
            run += data[i + 1:j + 1]
        i = j + 1
        runs.append(run)
    
    # Merge the runs
    while len(runs) > 1:
        i = 0
        while i < len(runs) - 1:
            A = runs[i]
            B = runs[i + 1]
            C = []
            while A and B:
                if A[0] <= B[0]:
                    C.append(A.pop(0))
                else:
                    C.append(B.pop(0))
            if A:
                C += A
            if B:
                C += B
            runs[i:i + 2] = [C]
            i += 1
    
    # Return the sorted data
    return runs[0]

# Time the algorithm
start = time.time()
subsortalgo(data)
end = time.time()
subsortalgo_time = end - start

# Print the result
print("Newsorting algo time: %.5f seconds" % subsortalgo_time)
import random
import time
import sys

# Generate input data
data = [random.randint(1, 500) for i in range(6000)]

# subsortalgo
def subsortalgo(data):
    data.sort()

# Time and space the algorithm
start_time = time.time()
start_space = sys.getsizeof(data)
subsortalgo(data)
end_space = sys.getsizeof(data)
end_time = time.time()

# Print the results

print("Newsorting Algo space: %d bytes" % (end_space - start_space))
