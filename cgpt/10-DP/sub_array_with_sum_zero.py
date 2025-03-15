def find_subarray_with_zero_sum(arr):
    # Dictionary to store the cumulative sum and its index
    cumulative_sum_map = {}
    cumulative_sum = 0

    for i, num in enumerate(arr):
        cumulative_sum += num

        # If the cumulative sum is zero, the subarray from the start to the current index has a sum of zero
        if cumulative_sum == 0:
            return arr[0:i+1]

        # If the cumulative sum is already in the map, a subarray with sum zero exists
        if cumulative_sum in cumulative_sum_map:
            start_index = cumulative_sum_map[cumulative_sum] + 1
            return arr[start_index:i+1]

        # Store the cumulative sum and its index in the map
        cumulative_sum_map[cumulative_sum] = i

    # If no subarray with sum zero is found, return None
    return None

# Example usage:
arr = [4, 2, -3, 1, 6]
result = find_subarray_with_zero_sum(arr)

if result:
    print("Subarray with sum zero:", result)
else:
    print("No subarray with sum zero found.")