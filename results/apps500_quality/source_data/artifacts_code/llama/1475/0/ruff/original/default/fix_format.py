import sys

input = sys.stdin.readline

n, b, k, x = map(int, input().split())
a = list(map(int, input().split()))

MOD = 10**9 + 7


def factorial(n, m):
    f = [1] * (n + 1)
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * i) % m
    return f


fac = factorial(2 * 10**5, x)


def power(x, y):
    res = 1
    while y:
        if y & 1:
            res = (res * x) % x
        x = (x * x) % x
        y >>= 1
    return res


def inv(x):
    return power(x, x - 2)


nfac = fac[n] * inv(fac[n - 1]) % x

blocks = {}
for i in a:
    blocks.setdefault(i, []).append(1)

for i in range(1, x):
    blocks[i] = 0
    for v in blocks.values():
        blocks[i] += v

dp = [0] * (k + 1)
dp[0] = 1

for i in range(1, k + 1):
    if i in blocks:
        dp[i] = (dp[i] + dp[i - 1] * blocks[i]) % MOD
    if i - 1 in blocks:
        dp[i] = (dp[i] + dp[i - 1] * blocks[i - 1]) % MOD

ans = dp[k]
for i in range(1, n):
    ans = (ans * nfac) % x

print(ans)
