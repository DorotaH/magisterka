n = int(input())
dp = [0] * (1 + n)
dp[1] = 2
dp[2] = 3
for i in range(3, 1 + n):
    dp[i] = 2 * dp[i - 1] + 1
print(dp[n])
