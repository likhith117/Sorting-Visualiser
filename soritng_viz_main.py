import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        yield arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j][1] < arr[min_idx][1]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key[1] < arr[j][1] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        yield arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        yield from merge_sort(L)
        yield from merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        yield arr


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high][1]
    for j in range(low, high):
        if arr[j][1] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        yield from quick_sort(arr, low, pi-1)
        yield from quick_sort(arr, pi+1, high)
    yield arr


def get_sorting_algorithm(data):
    """
    Returns the most efficient sorting algorithm to use for the given data.
    """
    if len(data) < 100:
        return insertion_sort
    elif len(data) < 1000:
        return selection_sort
    elif len(data) < 10000:
        return merge_sort
    else:
        return quick_sort



# Read sales data from CSV file
# Read sales data from CSV file
sales_data = []
with open('C:/Users/likhith/Desktop/sorting visualiser/sales_data_sample.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            # Append the string directly without converting to NumPy array
            sales_data.append((row[5], int(row[1])))
        except ValueError:
            continue

    # Convert NumPy arrays to tuples
    sorted_sales = [(str(x[0]), int(x[1])) for x in sorted(sales_data, key=lambda x: x[1])]

    # Print the highest and lowest sales values
    highest_sale = sorted_sales[-1]
    lowest_sale = sorted_sales[0]
    print(f'Highest sale: {highest_sale}')
    print(f'Lowest sale: {lowest_sale}')


# Set up the figure and axis for visualization
fig, ax = plt.subplots()
barlist = ax.bar(range(len(sorted_sales)), [x[1] for x in sorted_sales])
ax.set_xticklabels([x[0] for x in sorted_sales], rotation=45, ha='right')

# Define the function to update the plot
def update_plot(data):
    ax.clear()
    barlist = ax.bar(range(len(data)), [x[1] for x in data])
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels([x[0] for x in data], rotation=45, ha='right')
    plt.draw()
    plt.pause(0.01)



# Animate the plot
sorting_algorithm = get_sorting_algorithm(sorted_sales)
animation = FuncAnimation(fig, update_plot, frames=sorting_algorithm(sorted_sales), repeat=False)
plt.show()
