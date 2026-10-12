# Linear Search without using inbuilt functions

# Take number of elements from user
n = int(input("Enter the number of elements: "))

# Create an empty list
arr = []

# Take elements as input
print("Enter the elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Element to search
key = int(input("Enter the element to search: "))

# Linear Search
found = False
position = -1

for i in range(n):
    if arr[i] == key:
        found = True
        position = i
        break

# Display result
if found:
    print("Element found at index:", position)
else:
    print("Element not found")