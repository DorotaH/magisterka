import sys

input = sys.stdin.readline


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


def read_str():
    return input().strip()


def read_strs():
    return map(str, input().split())


def solve():
    n, k, len_ = read_ints()
    a = list(read_ints())
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        if not a[i - 1] == -1:
            if i - len_ < 0:
                ways[i] = ways[i - 1]
            else:
                ways[i] = (ways[i - 1] + ways[i - len_]) % mod
        else:
            if i - len_ < 0:
                ways[i] = ways[i]
            else:
                ways[i] = (ways[i - len_] * (k - 1) + ways[i - len_ + 1]) % mod
    return ways[n]

mod = 998_244_353
print(solve())
