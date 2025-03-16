

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


def is_valid_palindrom(s:str):
    c_s = ''.join(char.lower() for char in s if char.isalnum())
    return c_s == c_s[::-1]


if __name__ == '__main__':
    s = "kdsjflsjk"
    t = "wuio093jfkdsjflsjkkdslfkjl"
    # print(is_subsequence(s, t))
    # print(getRow(5))
    # print(using_pascals_triangle(5))

    sn = "A man, a plan, a canal: Panama"
    print(is_valid_palindrom(sn))
