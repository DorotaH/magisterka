mod = 10**9 + 7
n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    dp[i][0] = 1
    for j in range(1, k + 1):
        for diff in range(1, min(i, j) + 1):
            dp[i][j] += dp[i - 1][j - diff] * (i - diff + 1)
            dp[i][j] %= mod

ans = dp[n][k]
for i in range(1, (n + 1) // 2 + 1):
    ans += dp[n - 2 * i][k - 2 * i * (n - i)] * comb(n - 2 * i, n - 2 * i)
    ans %= mod

print(ans)

def comb(n, r):
    res = 1
    for i in range(r):
        res *= (n - i)
        res //= (i + 1)
    return res
