

def find_largest_element(l):
    largest = 0
    for e in l:
        if e > largest:
            largest = e
    return largest


def find_2nd_largest(arr):
    if len(arr) < 2:
        return None

    largest = max(arr[0], arr[1])
    second_largest = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return second_largest
