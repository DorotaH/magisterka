from collections import deque
from sys import stdin


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
    names = []
    for _ in range(n):
        names.append(read_strings())
    p = read_ints()
    handles = [None] * (n + 1)
    for i in range(n):
        h = names[p[i] - 1][0] if p[i] != 1 else names[p[i] - 1][1]
        handles[p[i]] = h

    q = deque(sorted(p, key=lambda x: handles[x]))

    for i in range(n):
        if handles[q[i]] != names[q[i] - 1][0] and handles[q[i]] != names[q[i] - 1][1]:
            return "NO"

    return "YES"

print(solve())
