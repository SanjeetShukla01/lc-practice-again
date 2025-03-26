# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


def group_anagrams(strs: list):
    def are_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    result = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key not in result:
            result[key] = [word]
        else:
            result[key].append(word)

    # return result
    return result.values()


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))
    # print(''.join(sorted("eat")))




