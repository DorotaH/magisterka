import sys

input = sys.stdin.readline

N = 5005
MOD = 998244353

n = int(input())
a = [0] + list(map(int, input().split()))

fac = N * [1]
for i in range(1, N):
    fac[i] = fac[i - 1] * i % MOD


def C(n, k):
    if k < 0 or k > n:
        return 0
    return pow(fac[k], -1, MOD) * fac[n] * pow(fac[n - k], -1, MOD) % MOD


b = sorted(a[1:])

p = [0] * (1 + n)
p[0] = 1
for i in range(1, 1 + n):
    p[i] = 0 if b[i - 1] > 2 * b[i] else (MOD - 1 - 2 * (n - i)) % MOD
pre = [0] * (1 + n)
for i in range(1, 1 + n):
    pre[i] = (p[i] + pre[i - 1]) % MOD

ans = 0
for i in range(1 + n):
    if a[i + 1] <= 2 * a[1]:
        continue
    for j in range(n - i):
        if a[i + 1 + j + 1] > 2 * a[i + 1]:
            break
    else:
        ans = (ans + pre[1 + j] * C(n - j - 1, i) % MOD) % MOD

print(ans)
