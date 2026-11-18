mod = 10**9 + 7
MAX = 2 * 10**5

fact = [1] * (1 + MAX)
for i in range(1, MAX + 1):
    fact[i] = (i * fact[i - 1]) % mod

inv = [1] * (1 + MAX)
for i in range(2, MAX + 1):
    inv[i] = inv[mod % i] * (mod - mod // i) % mod

fact_inv = [1] * (1 + MAX)
for i in range(1, MAX + 1):
    fact_inv[i] = inv[i] * fact_inv[i - 1] % mod


def comb(n, k):
    if n < k:
        return 0
    return fact[n] * fact_inv[n - k] * fact_inv[k] % mod


n, m, k = list(map(int, input().split()))

ans = 0
cmb = comb(m * n - 2, k - 2)
for i in range(1, m):
    ans += i * (m - i) * n * n * cmb
    ans %= mod

for i in range(1, n):
    ans += m * i * m * (n - i) * cmb
    ans %= mod

print(ans)
