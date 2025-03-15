from itertools import chain


# l1.extend(l2)
# l_new = [*l1, *l2]
# l_new = l1 + l2
# l_new =


def merge_sorted_list(l1, l2):
    c = list(chain(l1, l2))
    return c


def merge_list(l1, l2):
    result = []
    for el in l1:
        result.append(el)
    for el in l2:
        result.append(el)
    return result


if __name__ == '__main__':
    l1 = [3, 4, 5, 2, 9, 6]
    l2 = [9, 8, 7, 6, 4, 2]
    # print(merge_sorted_list(l1, l2))
    print(merge_list(l1, l2))
