

def find_missing_number(nums):
    n = len(nums) + 1                   ## because one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number


def find_missing_number_xor(nums):
    n = len(nums) + 1  # Total numbers including the missing one

    # XOR all numbers from 1 to N
    xor_n = 0
    for i in range(1, n + 1):
        xor_n ^= i

    # XOR all numbers in the array
    xor_arr = 0
    for num in nums:
        xor_arr ^= num

    # Missing number is the XOR of both
    missing_number = xor_n ^ xor_arr
    return missing_number


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 6]
    print("Missing Number:", find_missing_number(nums))
