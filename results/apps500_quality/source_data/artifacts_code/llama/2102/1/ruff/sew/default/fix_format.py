import sys
from builtins import print as builtin_print


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
    a, n = input_int_list(), input_int()
    b, ans = input_int_list(), float("inf")
    for i in range(6):
        mx, mn = float("-inf"), float("inf")
        for j in range(n):
            mx = max(mx, a[i] + b[j])
            mn = min(mn, a[i] + b[j])
        ans = min(ans, mx - mn)
    print(ans)


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()
