


def move_zeros_to_end(l):
    zeros = []
    non_zeros = []
    for i in range(len(l)):
        if l[i] == 0:
            zeros.append(l[i])
        else:
            non_zeros.append(l[i])
    return non_zeros + zeros


if __name__ == '__main__':
    l = [0, 89, 90, 0,  73, 63, 11, 35, 52]
    print(move_zeros_to_end(l))

