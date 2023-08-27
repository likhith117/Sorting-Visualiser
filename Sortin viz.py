import csv
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        yield arr

def update_plot(ax, data):
    ax.clear()
    ax.bar(range(len(data)), [x[1] for x in data])
    ax.set_xticklabels([x[0] for x in data], rotation=45, ha='right')
    plt.draw()
    plt.pause(0.01)

def visualize_sorting(sort_algo, arr):
    fig, ax = plt.subplots()
    data = arr.copy()
    barlist = ax.bar(range(len(data)), [x[1] for x in data])
    ax.set_xticklabels([x[0] for x in data], rotation=45, ha='right')
    plt.show(block=False)

    for i, data in enumerate(sort_algo(data)):
        if i % 5 == 0:
            update_plot(ax, data)
    update_plot(ax, data)

# Read sales data from CSV file
sales_data = []
with open('C:/Users/likhith/Desktop/Sorting Visualiser/sales_data_sample.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            sales_data.append((row[5], int(row[1])))
        except ValueError:
            continue

# Sort the sales data using bubble sort
sorted_sales = [x for x in bubble_sort(sales_data)][-1]

# Visualize the sorted sales data
visualize_sorting(bubble_sort, sales_data)

# Print the highest and lowest sales values
highest_sale = sorted_sales[-1]
lowest_sale = sorted_sales[0]
print("Highest sale:", highest_sale)
print("Lowest sale:", lowest_sale)
