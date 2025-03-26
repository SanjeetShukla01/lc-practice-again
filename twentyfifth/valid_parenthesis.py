


def is_valid_brute_force(s: str) -> bool:
    def check_valid(sub_s):
        if not sub_s:
            return True
        if len(sub_s) % 2 != 0:
            return False

        for i in range(len(sub_s)):
            for j in range(i + 1, len(sub_s)):
                if (sub_s[i] == '(' and sub_s[j] == ')') or \
                   (sub_s[i] == '{' and sub_s[j] == '}') or \
                   (sub_s[i] == '[' and sub_s[j] == ']'):

                    if check_valid(sub_s[i + 1:j]) and check_valid(sub_s[0:i] + sub_s[j + 1:]):
                        return True
        return False

    return check_valid(s)

