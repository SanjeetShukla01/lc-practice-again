# Function to return K'th largest element
def kth_largest1(arr, K):
    # Sort the array in descending order
    arr.sort(reverse=True)
    return arr[K - 1]


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    K = 2
    print(kth_largest1(arr, K))
