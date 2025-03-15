# Find the Intersection of Two Arrays - Elements common to both.


def intersection(nums1, nums2):
    # Convert both arrays to sets and find the intersection
    result = list(set(nums1) & set(nums2))
    return result


from collections import Counter


def intersection_hash(nums1, nums2):
    # Create a frequency count of the first array
    count = Counter(nums1)
    print(count)
    result = []

    # Iterate through the second array
    for num in nums2:
        # Check if the number exists in the count dictionary
        if count[num] > 0:
            result.append(num)
            count[num] -= 1  # Decrease the count to avoid duplicates

    return result


# Example Usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 3]

print("Intersection:", intersection(nums1, nums2))

if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = [1, 9, 11, 15, 18, 5]

    # print(intersection(l1, l2))
    print(intersection_hash(l1, l2))