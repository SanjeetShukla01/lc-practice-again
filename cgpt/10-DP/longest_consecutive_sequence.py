def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)  # Store all numbers in a HashSet
    longest_streak = 0

    for num in num_set:  # Iterate through unique numbers
        if num - 1 not in num_set:  # Check if 'num' is the start of a sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:  # Expand the sequence
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)  # Update longest streak

    return longest_streak


if __name__ == '__main__':
    # Example usage
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive(nums))  # Output: 4 (Sequence: [1, 2, 3, 4])
