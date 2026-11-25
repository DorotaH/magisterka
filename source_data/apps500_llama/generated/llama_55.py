n = int(input())
dp = [0] * (n + 1)
dp[1] = 2
dp[2] = 3
for i in range(3, n + 1):
    dp[i] = 2 * dp[i - 1] - dp[i - 3] + 1
print(dp[n])
