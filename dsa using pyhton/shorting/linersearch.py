def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
my_list = [23, 34, 4, 53, 234, 123, 56, 68562, 34, 656]
target_item = 53

index = linear_search(my_list, target_item)
if index != -1:
    print(f"The target item {target_item} is found at index {index}.")
else:
    print(f"The target item {target_item} is not found in the list.")
