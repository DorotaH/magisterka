import sys

MOD=7 + int(1e9)


def fast_input():
    return sys.stdin.readline().rstrip()


def get_num():
    return int(fast_input())


def get_nums():
    return map(int, fast_input().split())


def get_str():
    return fast_input()


def get_strs():
    return map(str, fast_input().split())


def solve():
    n, k = get_nums()
    if n == 1:
        print(k)
        return
    res = 0
    for  i in  range(k - n % 2, 0, -1):
        res = (res + pow(i, n, MOD)) % MOD
    for  i in  range(1, (k - (n % 2)) // 2 + 1):
        res = (res + (pow(i, n // 2, MOD) * (k - (n % 2)) % MOD)) % MOD
    print(res)


solve()
