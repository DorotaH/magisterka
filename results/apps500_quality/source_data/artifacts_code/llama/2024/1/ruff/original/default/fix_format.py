import sys

input = sys.stdin.readline

N = 5005
MOD = 998244353

n = int(input())
a = [0] + list(map(int, input().split()))

fac = [1] * N
for i in range(1, N):
    fac[i] = i * fac[i - 1] % MOD


def C(n, k):
    if k < 0 or k > n:
        return 0
    return fac[n] * pow(fac[k], -1, MOD) * pow(fac[n - k], -1, MOD) % MOD


b = sorted(a[1:])

p = [0] * (n + 1)
p[0] = 1
for i in range(1, n + 1):
    if b[i - 1] > 2 * b[i]:
        p[i] = 0
    else:
        p[i] = (MOD - 1 - 2 * (n - i)) % MOD

pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = (pre[i - 1] + p[i]) % MOD

ans = 0
for i in range(n + 1):
    if a[i + 1] <= 2 * a[1]:
        continue
    for j in range(n - i):
        if a[i + 1 + j + 1] > 2 * a[i + 1]:
            break
    else:
        ans = (ans + pre[j + 1] * C(n - j - 1, i) % MOD) % MOD

print(ans)
