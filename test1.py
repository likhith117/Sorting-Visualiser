import csv
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        yield arr

import time

def update_plot(ax, data):
    ax.clear()
    ax.bar(range(len(data)), [x[1] for x in data])
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels([x[0] for x in data], rotation=45, ha='right')
    plt.draw()
    plt.gcf().canvas.flush_events()  # Force matplotlib to update the plot
    time.sleep(0.01)  # Add a delay to slow down the animation


def visualize_sorting(sort_algo, arr):
    fig, ax = plt.subplots()
    data = arr.copy()
    barlist = ax.bar(range(len(data)), [x[1] for x in data])
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels([x[0] for x in data], rotation=45, ha='right')
    plt.show(block=False)

    for i, data in enumerate(sort_algo(data)):
        if i % 5 == 0:
            update_plot(ax, data)
    update_plot(ax, data)

# Read sales data from CSV file
sales_data = []
try:
    with open('C:/Users/likhith/Desktop/Sorting Visualiser/sales_data_sample.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                sales_data.append((row[0], int(row[1])))  # Assumes that the item name is in the first column
            except (ValueError, IndexError):
                continue
except FileNotFoundError:
    print("File not found!")
    exit(1)

if not sales_data:
    print("No data found in the CSV file!")
    exit(1)

# Sort the sales data using bubble sort
sorted_sales = [x for x in bubble_sort(sales_data)][-1]

# Visualize the sorted sales data
visualize_sorting(bubble_sort, sales_data)

# Print the highest and lowest sales values
highest_sale = sorted_sales[-1]
lowest_sale = sorted_sales[0]
print("Highest sale:", highest_sale)
print("Lowest sale:", lowest_sale)
