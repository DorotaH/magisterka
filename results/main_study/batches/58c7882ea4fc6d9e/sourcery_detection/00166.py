n = int(input())
a = list(map(int, input().split()))

b = sorted(a[::])
for i in range(n):
    if b[i] == b[i + 1]:
        d = b[i]

l, r = -1, -1
for i in range(1 + n):
    if a[i] == d:
        if l < 0:
            l = i
        else:
            r = i

f = [1 for _ in range(2 + n)]
f_inv = [1 for _ in range(2 + n)]
mod = 7 + 10 ** 9
for i in range(1, 2 + n):
    f[i] = i * f[i - 1] % mod
    f_inv[i] = pow(f[i], mod - 2, mod)


def comb(n, k):
    return f[n] * f_inv[k] * f_inv[n - k] % mod


for k in range(1, 2 + n):
    ans = 0

    if 2 <= k:
        ans += comb(n - 1, k - 2)
        ans %= mod

    if k <= n - 1:
        ans += comb(n - 1, k)
        ans %= mod

    if k <= n:
        ans += 2 * comb(n - 1, k - 1)
        ans %= mod

    if l + n - r >= k - 1:
        ans -= comb(l + n - r, k - 1)
        ans %= mod

    print(ans)
