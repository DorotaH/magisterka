import sys
from collections import defaultdict, Counter

P = 7 + 10**9


def factmod(n):
    res = 1
    for i in range(2, 1 + n):
        res *= i
        res %= P

    return res


def solve():
    n, m = list(map(int, input().split()))
    colour = {i: 0 for i in range(1, 1 + m)}
    colour_map = {}
    for i, line in enumerate(sys.stdin):
        A = [int(x) for x in line.split()]
        count = Counter(A)

        if count[A[0]] == 1:
            count.pop(A[0])
        else:
            count[A[0]] -= 1

        for c in count:
            p = (colour[c], i, count[c])
            if p in colour_map:
                colour[c] = colour_map[p]
            else:
                colour[c] = colour_map[p] = 1 + len(colour_map)

    count = Counter(list(colour.values()))

    res = 1
    for c in count:
        res *= factmod(count[c])
        res %= P

    return res


print(solve())
