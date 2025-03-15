# Function for finding first and last occurrence of x
def find(arr, x):
    n = len(arr)
    first = -1
    last = -1

    for i in range(n):
        if x != arr[i]:
            continue

        if first == -1:
            first = i

        last = i
    res = [first, last]
    return res


if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    x = 5
    res = find(arr, x)
    print(res[0], res[1])
