# Binary Search without using built-in search functions

import time

# Taking user input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements in sorted order:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

start_time = time.perf_counter()

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        end_time = time.perf_counter()
        print(f"Element found at index {mid}")
        print(f"Execution Time: {end_time - start_time:.10f} seconds")
        found = True
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    end_time = time.perf_counter()
    print("Element not found")
    print(f"Execution Time: {end_time - start_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case   : O(1)")
print("Average Case: O(log n)")
print("Worst Case  : O(log n)")
print("Space Complexity: O(1)")