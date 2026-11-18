mod = 7 + 10 ** 9
MAX = 2 * 10 ** 5

fact = [1] * (1 + MAX)
for i in range(1, 1 + MAX):
    fact[i] = (fact[i-1] * i) % mod

inv = [1] * (1 + MAX)
for i in range(2, 1 + MAX):
    inv[i] = inv[mod % i] * (mod - mod // i) % mod

fact_inv = [1] * (1 + MAX)
for i in range(1, 1 + MAX):
    fact_inv[i] = fact_inv[i-1] * inv[i] % mod


def comb(n, k):
    return 0 if n < k else fact[n] * fact_inv[n-k] * fact_inv[k] % mod


n, m, k = list(map(int, input().split()))

ans = 0
cmb = comb(m * n - 2, k - 2)
for i in range(1, m):
    ans += i * (m - i) * n * n * cmb
    ans %= mod

for i in range(1, n):
    ans += i * m * m * (n - i) * cmb
    ans %= mod

print(ans)
