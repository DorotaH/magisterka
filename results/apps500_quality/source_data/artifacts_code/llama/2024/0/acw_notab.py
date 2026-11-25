import sys
input = sys.stdin.readline
mod = 998244353


def pow(x, n):
    if n == 0:
        return 1
    y = pow(x, n // 2)
    return ((y * y) % mod * (pow(x, n % 2) if n % 2 else 1)) % mod


n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

f = [1] * (1 + n)
for i in range(1, 1 + n):
    f[i] = (i * f[i - 1]) % mod

inv = [0] * (1 + n)
inv[n] = pow(f[n], mod - 2)
for i in range(n - 1, -1, -1):
    inv[i] = (inv[i + 1] * (i + 1)) % mod

fact = [0] * (1 + n)
fact[0] = 1
for i in range(1, 1 + n):
    fact[i] = (i * fact[i - 1]) % mod

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if 2 * a[j] > a[i]:
            break
        if 2 * a[i] > a[j]:
            cnt += 1

ans = f[n]
for i in range(1, 1 + n):
    ans = (ans - cnt * inv[i] * fact[n - i] % mod) % mod

print(ans)
