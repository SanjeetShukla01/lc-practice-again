# Example 1:
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.


def str_in_Str(haystack, needle):
    for i in range(len(haystack)):
        if needle == haystack[i:i+len(needle)]:
            return i
    return -1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    print(str_in_Str(haystack, needle))
