n, k = map(int, input().split())

dp = [0] * (1 + n)
dp[0] = 1
dp[1] = k

for i in range(2, 1 + n):
    dp[i] = k * dp[i - 1]

print(dp[n])
