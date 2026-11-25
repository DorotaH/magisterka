import sys
from builtins import print as builtin_print
import math
import heapq
from collections import deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import lru_cache, reduce
from itertools import accumulate, permutations, combinations, product
from heapq import heappushpop, heapify, heappop, heappush, heapreplace
from inspect import currentframe


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_list():
    return list(map(int, input().split()))


def input_str():
    return input().split()


def input_int_list():
    return list(map(int, input().split()))


def print(*args, **kwargs):
    kwargs["file"] = sys.stdout
    return builtin_print(*args, **kwargs)


def solve():
    a = input_int_list()
    n = input_int()
    b = input_int_list()
    ans = float("inf")
    for i in range(6):
        mx, mn = float("-inf"), float("inf")
        for j in range(n):
            mx = max(mx, b[j] + a[i])
            mn = min(mn, b[j] + a[i])
        ans = min(ans, mx - mn)
    print(ans)


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()
