N, mod = 5000, 998244353
fac, finv = [1] * (N + 1), [1] * (N + 1)
for i in range(N):
    fac[1 + i] = fac[i] * (1 + i) % mod
finv[-1] = pow(fac[-1], mod - 2, mod)
for i in range(N - 1, -1, -1):
    finv[i] = finv[1 + i] * (1 + i) % mod


def cmb1(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return finv[r] * fac[n] * finv[n - r] % mod


n, x = map(int, input().split())

dp = [[0] * (x + 1) for i in range(n + 1)]
dp[n][0] = 1
for i in reversed(range(1, 1 + n)):
    for j in range(x + 1):
        if not dp[i][j]:
            continue
        nj = min(x, i + j - 1)
        for k in reversed(range(i + 1)):
            dp[k][nj] += cmb1(i, i - k, mod) * pow(nj - j, i - k, mod) * dp[i][j]
            dp[k][nj] %= mod
ans = 0
for i in range(x + 1):
    ans += dp[0][i]
    ans %= mod
print(ans)
