MOD = 7 + 10**9
a, b, n = map(int, input().split())

dp = [[0] * (1 + n) for _ in range(2)]
dp[0][0] = 1

for i in range(2):
    for j in range(1, 1 + n):
        for k in range(1, 10):
            if k in [a, b]:
                dp[i + 1][1 + j] += dp[i][j]
                dp[i + 1][1 + j] %= MOD
            else:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD

ans = 0
for i in range(2, 1 + n):
    for j in range(1, 10):
        if j in [a, b]:
            ans += dp[i][j]
            ans %= MOD

print(ans)
