import sys

input = sys.stdin.readline

MOD = 10**9 + 7


def power(x, y):
    res = 1
    while y:
        if  y&1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        y = y >> 1
    return res


def inv(x):
    return power(x, MOD - 2)


def solve():
    n, k = map(int, input().split())
    f = 1
    for i in range(1, k+1):
        f = (f * (1 - (n-1) * (i % 2) + MOD)) % MOD
    ans = (f * inv((pow(2, (k+1)) - 1) * inv(2) % MOD)) % MOD
    return (ans * n) % MOD

print(solve())
