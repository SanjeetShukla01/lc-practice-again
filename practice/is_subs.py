

def is_subsequence(s, t):
    window_len = len(s)
    length = len(t)
    result = False
    for i in range(length-window_len):
        if t[i:window_len] != s:
            result = False
        result = True
        break
    return  result


def getRow(rowIndex):
    row = []
    for i in range(rowIndex+1):
        new_row = [1] * (i + 1)  # Initialize with 1s
        if i > 1:
            for j in range(1, i):
                new_row[j] = row[j - 1] + row[j]
        row = new_row
    return row


def using_pascals_triangle(n: int):
    dp = [[1]*(i+1) for i in range(n+1)]
    for i in range(2, n+1):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    # print(dp)
    return dp[n]


def palindromic_number(n:int):
    if n < 0:
        return False
    if n <=9:
        return True

    reversed_num = 0
    original_num = n

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original_num == reversed_num



# def is_valid_palindrom(s:str):
#     c_s = ''.join(char.lower() for char in s if char.isalnum())
#     return c_s == c_s[::-1]


def is_valid_palindrom(s:str):
    alphanumeric_chars = ''.join(char.lower() for char in s if char.isalnum())
    length = len(alphanumeric_chars)
    for i in range(length):
        if alphanumeric_chars[i] != alphanumeric_chars[length-1-i]:
            return False
    return True


def valid_parenthesis(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
            print(stack)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False
    return not stack


def return_missing_balanced_numbers(input):
    tuples = [(i, input.count(i)) for i in input]
    print(tuples)
    tuples.sort(key=lambda x: -x[1])
    print(tuples)
    max_value = tuples[0][1]
    print(max_value)
    return {k: max_value - v for k, v in tuples if v < max_value}


def return_missing_balanced_numbers1(input):
    my_dict = {}
    for i in input:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return {a: max(my_dict.values()) - b for (a, b) in my_dict.items() if b != max(my_dict.values())}


def largest_palindrom(s:str):






if __name__ == '__main__':
    s = "kdsjflsjk"
    t = "wuio093jfkdsjflsjkkdslfkjl"
    # print(is_subsequence(s, t))
    # print(getRow(5))
    # print(using_pascals_triangle(5))

    sn = "A man, a plan, a canal: Panama"
    # print(is_valid_palindrom(sn))
    # print(palindromic_number(121))
    ln = [4, 5, 11, 5, 6, 11]
    print(return_missing_balanced_numbers(ln))