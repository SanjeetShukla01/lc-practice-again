

def two_sum(l:list, target:int) -> list:
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == target:
                return [i, j]


def target_sum_better(nums:list, target:int) -> list:
    m = {}
    for i, x in enumerate(nums):
        m[x] = i
        y = target - x
        if y in m:
            return [m[y], i]



def median_two_sa(l1, l2):
    median_arr = l1 + l2
    median = 0
    length = len(median_arr)
    if length % 2 != 0:
        return median_arr[(length//2)+ 1]
    return (median_arr[length//2 -1] + median_arr[length//2])/2



def transpose_string(input_string):
    lines = input_string.strip().split('\n')
    matrix = [line.split() for line in lines]
    print(f"matrix: {matrix}")
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    transposed_matrix = [['' for _ in range(rows)] for _ in range(cols)]
    print(f"transposed_matrix: {transposed_matrix}")
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    transposed_lines = [' '.join(row) for row in transposed_matrix]
    return '\n'.join(transposed_lines)




if __name__ == '__main__':
    l = [1, 4, 5, 6, 7, 9, 2]
    # print(two_sum(l, 9))
    # print(target_sum_better(l, 9))

    nums1 = [1, 2]
    nums2 = [3, 4]
    # print(median_two_sa(nums1, nums2))

    # Example with a string.
    test_string = "name age\nalice 21\nryan 30"
    transposed_string_result = transpose_string(test_string)
    print(transposed_string_result)
