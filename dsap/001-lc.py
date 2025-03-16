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
    seen = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index


def find_two_sum(nums, target):
    seen = {}
    index = 0
    for number in nums:
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index
        index = index + 1

    return None




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next


if __name__ == '__main__':
    nums, target = [2, 7, 11, 15], 9
    # nums, target = [3, 2, 4], 6
    # nums, target = [3, 3], 6
    # print(target_sum(nums, target))
    print(target_sum_better(nums, target))
