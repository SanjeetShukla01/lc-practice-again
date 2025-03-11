
def find_min_max(l: list) -> list:
    min, max = l[0], l[0]
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
        elif l[i] < min:
            min = l[i]
    return [min, max]


def find_largest_smallest_2nd_too(l:list) -> list:
    l1 = max(l)
    l2 = min(l)

    l.remove(l1)
    l.remove(l2)
    lx = find_min_max(l)
    return [l1, l2, lx]



if __name__ == '__main__':
    l = [1, 4, 5, 7, 9, 6]
    # print(find_min_max(l))
    print(find_largest_smallest_2nd_too(l))