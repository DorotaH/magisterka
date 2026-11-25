from sys import stdin
from collections import deque


def read_int():
    return int(stdin.readline().strip())


def read_ints():
    return list(map(int, stdin.readline().strip().split()))


def read_string():
    return stdin.readline().strip()


def read_strings():
    return stdin.readline().strip().split()


def solve():
    n = read_int()
    names = [read_strings() for _ in range(n)]
    p = read_ints()
    handles = [None] * (1 + n)
    for i in range(n):
        h = names[p[i] - 1][0] if p[i] != 1 else names[p[i] - 1][1]
        handles[p[i]] = h

    q = deque(sorted(p, key=lambda x: handles[x]))

    return next(
        (
            "NO"
            for i in range(n)
            if handles[q[i]] not in [names[q[i] - 1][0], names[q[i] - 1][1]]
        ),
        "YES",
    )


print(solve())
