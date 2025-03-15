

def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return nums[:i+1]


if __name__ == '__main__':
    sorted_list = [1, 2, 3, 3, 3, 5, 6, 7, 7, 9, 9]
    print(remove_duplicates(sorted_list))