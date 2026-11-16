def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    c += b if len(a) == 0 else a
    return c


def merge_sort(x):
    if len(x) in [0, 1]:
        return x
    middle = len(x) // 2
    a = merge_sort(x[:middle])
    b = merge_sort(x[middle:])
    return merge(a, b)
