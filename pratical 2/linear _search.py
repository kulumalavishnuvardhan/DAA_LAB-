def linear_search(arr, target):
    """Perform a linear search for target in arr without built-in search functions."""
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def main():
    print("Linear Search Demo")
    input_list = input("Enter numbers separated by spaces: ").strip().split()
    arr = []
    for item in input_list:
        try:
            arr.append(int(item))
        except ValueError:
            print(f"Skipping non-integer value: {item}")

    if not arr:
        print("No valid numbers were entered.")
        return

    try:
        target = int(input("Enter the number to search for: ").strip())
    except ValueError:
        print("Please enter a valid integer to search.")
        return

    result = linear_search(arr, target)
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the list.")


if __name__ == "__main__":
    main()
