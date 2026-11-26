import sys

MOD = 7 + 10**9


def factorial(n):
    f = [1] * (1 + n)
    for i in range(1, 1 + n):
        f[i] = (i * f[i - 1]) % MOD
    return f


def ncr(n, r):
    f = factorial(n)
    inv = [0] * (1 + n)
    inv[n] = pow(f[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD
    return (f[n] * inv[r] * inv[n - r]) % MOD


def solve():
    k, s = input().split()
    k, n = int(k), len(s)
    ans = 1
    for _ in s:
        ans = (ans * ncr(k + n, k)) % MOD
        n += 1
    return ans


print(solve())
