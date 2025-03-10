
def reverse_string(s:str) -> str:
    return s[::-1]


def reverse_string1(s:str) -> str:
    return ''.join(reversed(s))


def reverse_string2(s:str) -> str:
    result = ""
    for char in s:
        result = char + result
    return result


def reverse_string_loop(s:str) -> str:
    result = ""
    for _ in range(len(s)-1, -1, -1):
        result += s[_]
    return result


def reverse_using_list_comprehension(s:str) -> str:
    rev = ''.join([s[i] for i in range(len(s) - 1, -1, -1)])
    return rev


def reverse_string_using_stck(s:str) -> str:
    stack = list(s)
    rev = ""
    while stack:
        rev += stack.pop()
    return rev


if __name__ == '__main__':
    s = "reverse this string"
    print(reverse_string_using_stck(s))