

def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2  # Integer division to find the middle index
        if arr[mid] == target:
          return mid  # Target found at the middle index
        elif arr[mid] < target:
          left = mid + 1  # Target is in the right half
        else:
          right = mid - 1  # Target is in the left half

    return -1  # Target not found


if __name__ == '__main__':
    # Example usage:
    my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_element = 23
    print(binary_search(my_list, target_element))
