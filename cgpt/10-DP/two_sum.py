def two_sum(nums, target):
    num_map = {}  # Dictionary to store number -> index
    for i, num in enumerate(nums):
        num_map[num] = i  # Store current number's index in hashmap
        complement = target - num  # Find the number needed to reach target
        if complement in num_map:
            return [num_map[complement], i]  # Return indices if found
    return []  # Return empty list if no pair found


def two_sum_sorted(nums, target):
    nums = sorted((num, i) for i, num in enumerate(nums))  # Sort while keeping original indices
    left, right = 0, len(nums) - 1

    while left < right:
        curr_sum = nums[left][0] + nums[right][0]  # Sum of two numbers
        if curr_sum == target:
            return [nums[left][1], nums[right][1]]  # Return original indices
        elif curr_sum < target:
            left += 1  # Move left pointer to increase sum
        else:
            right -= 1  # Move right pointer to decrease sum
    return []  # No solution found


if __name__ == '__main__':
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1]
