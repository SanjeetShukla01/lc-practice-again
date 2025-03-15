def find_permutations_simple(s, prefix=""):
    if not s:  # Base case: If string is empty, store the prefix
        return [prefix]

    permutations = []
    for i in range(len(s)):
        new_prefix = prefix + s[i]  # Add current character to prefix
        new_remaining = s[:i] + s[i + 1:]  # Remove character from remaining
        permutations += find_permutations_simple(new_remaining, new_prefix)  # Recur

    return permutations



if __name__ == '__main__':
    # Example usage
    # print(find_permutations_simple("abc"))
    s = "abc"
    print(s[0+1:])
