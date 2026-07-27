# Quick Sort without using built-in sorting functions
# Takes user input, calculates execution time, and displays time complexity

import time

# Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left) + middle + quick_sort(right)

# User Input
n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

print("Original List:", arr)

# Start Time
start_time = time.perf_counter()

# Sorting
sorted_arr = quick_sort(arr)

# End Time
end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("Sorted List:", sorted_arr)
print("Execution Time:", execution_time, "seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n²)")
print("Space Complexity: O(log n) (recursion stack)")