
def check_pal(s:str) -> bool:
    return s == s[::-1]

def check_pal1(s:str) -> bool:
    i, j = 0, len(s)-1
    is_palindrom = True
    while i < j:
        if s[i] != s[j]:
            is_palindrom = False
            break
        i += 1
        j -= 1
    return is_palindrom


def check_pal2(s:str) -> bool:
    rev = ''.join(reversed(s))
    return s == rev


def check_pal3(s:str, i, j) -> bool:
    if i < j:
        return True
    if s[i] != s[j]:
        return False
    return check_pal3(s, i+1, j-1)


def check_pal4(s:str) -> bool:
    rev = ""
    for char in s:
        rev = char + rev
    return s == rev

def check_pal5(n:int) -> bool:
    rev = 0
    temp = abs(n)
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10

    return (rev == abs(n))


def check_pal6(n:int) -> bool:
    s = str(abs(n))
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length- i -1]:
            return False
    return True


def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""

    # DP table initialization
    dp = [[False] * n for _ in range(n)]

    start = 0
    max_length = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for substrings of length 3 or more
    for length in range(3, n + 1):  # Length of substring
        for i in range(n - length + 1):  # Start index
            j = i + length - 1  # End index

            if s[i] == s[j] and dp[i + 1][j - 1]:  # Check inner substring
                dp[i][j] = True
                start = i
                max_length = length

    return s[start:start + max_length]


# Test case
A = "AAABAAABD"
print(longest_palindromic_substring(A))


if __name__ == '__main__':
    s = "AAAAAABAAAAAA"
    # print(check_pal(s))
    # print(check_pal3(s, 0, len(s)-1))
    # print(check_pal4(s))
    print(check_pal5(121))