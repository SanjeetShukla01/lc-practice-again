
def revs(s):
    n = len(s)
    result = ""
    for i in range (n-1, -1, -1):
        result = result + s[i]
    return result

def min_max(l):
    n = len(l)
    result = ""
    for i in range (n-1, -1, -1):
        result = result + s[i]
    return result


if __name__ == '__main__':
    print(revs("slkf;al"))