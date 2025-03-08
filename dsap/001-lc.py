# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target

"""
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


def target_sum(nums:list, target:int) -> list:
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if i != j and nums[i] + nums[j] == target:
                return list[i, j]


def target_sum_better(nums:list, target:int) -> list:
    m = {}
    for i, x in enumerate(nums):
        m[x] = i
        y = target - x
        if y in m:
            return [m[y], i]


if __name__ == '__main__':
    nums, target = [2, 7, 11, 15], 9
    # nums, target = [3, 2, 4], 6
    # nums, target = [3, 3], 6
    # print(target_sum(nums, target))
    print(target_sum_better(nums, target))
