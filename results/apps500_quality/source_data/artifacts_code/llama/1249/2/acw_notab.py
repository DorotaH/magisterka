from collections import defaultdict
import sys


def solve():
    m, k, n, s = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    a = [(val, i) for i, val in enumerate(a)]
    a.sort(key=lambda x: x[0])

    b = [(val, i) for i, val in enumerate(b)]
    b = sorted(b, key=lambda x: x[0])

    count = defaultdict(int)
    for val, i in b:
        count[val] += 1

    removed = []

    def can_remove():
        nonlocal removed
        for val, i in b:
            if count[val] > 0 and count[val] > (a[i][1] - a[i - 1][1]) // k if i > 0 else (a[i][1] // k):
                removed.append(a[i][1])
                count[val] -= 1
        return True

    for i in range(1, m):
        if a[i - 1][0] == a[i][0]:
            a[i - 1] = (a[i - 1][0], k + a[i - 1][1])
        else:
            a[i] = (a[i][0], a[i][1])

    if k > a[-1][1]:
        return -1

    if can_remove():
        return len(removed)

    for i in range(1, m):
        if a[i][0] == a[i - 1][0]:
            a[i - 1] = (a[i - 1][0], k + a[i - 1][1])
        else:
            a[i] = (a[i][0], a[i][1])
        while can_remove():
            pass

    return -1


print(solve())
