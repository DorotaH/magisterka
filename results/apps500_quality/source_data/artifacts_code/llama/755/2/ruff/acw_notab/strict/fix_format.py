x = int(input())
steps = [5, 4, 3, 2, 1]
dp = [float("inf")] * (1 + x)
dp[0] = 0

for i in range(1, 1 + x):
    for s in steps:
        if i - s >= 0:
            dp[i] = min(dp[i], dp[i - s] + 1)

print(dp[x])
