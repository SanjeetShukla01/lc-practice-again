# fn = fn-1 + fn-2
# f0 = 0 and f1 = 1


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


FibArray = [0, 1]
def fibonacci_arr(n):

    if n < 0:
        print("Incorrect input")

    # Check is n is less
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci_arr(n - 1) + fibonacci_arr(n - 2))
        return FibArray[n]


if __name__ == '__main__':
    # Driver Program
    print(Fibonacci(9))
    print(fibonacci_arr(9))

