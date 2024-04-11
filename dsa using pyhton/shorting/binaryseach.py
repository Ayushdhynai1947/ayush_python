def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Return the index if the target is found
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if the target is not found

# Example usage:
my_list = [4, 12, 23, 34, 53, 56, 123, 234, 656, 68562]
target_item = 53

index = binary_search(my_list, target_item)
if index != -1:
    print(f"The target item {target_item} is found at index {index}.")
else:
    print(f"The target item {target_item} is not found in the list.")
