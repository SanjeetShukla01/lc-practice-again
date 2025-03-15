
def is_vowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']


def count_vowels(s:str):
    v_cv = 0

    for char in s:
        if is_vowel(char):
            v_cv += 1
    return v_cv


def countVovels1(str, n):
    if (n == 1):
        return is_vowel(str[n - 1])

    return (countVovels1(str, n - 1) +
            is_vowel(str[n - 1]))


if __name__ == '__main__':
    ch = 'a'
    s = "eskldfjaslkji"
    # print(is_vowel(ch))
    print(countVovels1(s, len(s)))