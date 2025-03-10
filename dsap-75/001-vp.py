def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False
    return not stack


if __name__ == '__main__':
    # Test cases
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "{[]}"
    s6 = "([{}])"
    s7 = "([)]"
    s8 = "(("
    s9 = "))"
    s10 = "abc"
    s11 = ")("

    # print(f"s1: {s1} is valid? {is_valid(s1)}")
    # print(f"s2: {s2} is valid? {is_valid(s2)}")
    # print(f"s3: {s3} is valid? {is_valid(s3)}")
    # print(f"s4: {s4} is valid? {is_valid(s4)}")
    # print(f"s5: {s5} is valid? {is_valid(s5)}")
    # print(f"s6: {s6} is valid? {is_valid(s6)}")
    # print(f"s7: {s7} is valid? {is_valid(s7)}")
    # print(f"s8: {s8} is valid? {is_valid(s8)}")
    # print(f"s9: {s9} is valid? {is_valid(s9)}")
    # print(f"s10: {s10} is valid? {is_valid(s10)}")
    print(f"s11: {s11} is valid? {is_valid(s11)}")
