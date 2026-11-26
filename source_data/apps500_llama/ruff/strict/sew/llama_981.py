import sys
import math


def read_int():
    return int(sys.stdin.readline().rstrip())


def read_ints():
    return map(int, sys.stdin.readline().rstrip().split())


def read_str():
    return sys.stdin.readline().rstrip()


def read_strs():
    return sys.stdin.readline().rstrip().split()


def solve():
    n, p = read_ints()
    a = list(read_ints())

    max_val = max(a)
    if max_val <= 2:
        return (0, [])

    total, smallest = sum(a), min(a)
    if total - smallest < p:
        return (1, [total])
    elif total - smallest == p:
        return (1, [total])

    result = []
    for x in range(1, n + 1):
        if (total - x) % p != 0:
            result.append(x)

    return (len(result), result)


n, p = read_ints()
result = solve()
print(result[0])
print(*result[1])
