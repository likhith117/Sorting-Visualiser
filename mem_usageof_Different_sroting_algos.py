import random
from memory_profiler import memory_usage
import multiprocessing as mp

# bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

# selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left_half = [x for x in arr[1:] if x <= pivot]
    right_half = [x for x in arr[1:] if x > pivot]
    return quick_sort(left_half) + [pivot] + quick_sort(right_half)

if __name__ == '__main__':
    # generate a list of random integers
    arr = [random.randint(1, 1000) for i in range(1000)]

    # measure the memory usage of each sorting algorithm
    mem_usage_bubble = memory_usage((bubble_sort, (arr,)), max_iterations=10)
    mem_usage_insertion = memory_usage((insertion_sort, (arr,)), max_iterations=10)
    mem_usage_selection = memory_usage((selection_sort, (arr,)), max_iterations=10)
    mem_usage_merge = memory_usage((merge_sort, (arr,)), max_iterations=10)
    mem_usage_quick = memory_usage((quick_sort, (arr,)), max_iterations=10)

    # print the results
    print("Memory usage (bubble sort):", (max(mem_usage_bubble) - min(mem_usage_bubble))*1024, "KB")
    print("Memory usage (insertion sort):", (max(mem_usage_insertion) - min(mem_usage_insertion))*1024, "KB")
    print("Memory usage (selection sort):", (max(mem_usage_selection) - min(mem_usage_selection))*1024, "KB")
    print("Memory usage (merge sort):", (max(mem_usage_merge) - min(mem_usage_merge))*1024, "KB")
    print("Memory usage (quick sort):", (max(mem_usage_quick) - min(mem_usage_quick))*1024, "KB")
    
