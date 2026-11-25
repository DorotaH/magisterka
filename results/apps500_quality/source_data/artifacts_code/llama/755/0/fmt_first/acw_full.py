x = int(input())
steps = [5, 4, 3, 2, 1]
dp = [float("inf")] * (1 + x)
dp[0] = 0

for i in range(1, 1 + x):
	for step in steps:
		if i >= step:
			dp[i] = min(dp[i], dp[i - step] + 1)

print(dp[x])
