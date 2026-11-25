n, k = map(int, input().split())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = k

for i in range(2, n + 1):
    dp[i] = k * dp[i - 1]

print(dp[n])