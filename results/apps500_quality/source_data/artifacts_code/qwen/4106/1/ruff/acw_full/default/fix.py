def max_beauty_pictures(n, k, x, a):
	if n < k * x:
		return -1
	
	dp = [[-1] * (1 + x) for _ in range(1 + n)]
	dp[0][0] = 0
	
	for i in range(1, 1 + n):
		for j in range(1, 1 + x):
			if i >= k:
				dp[i][j] = max(dp[i][j], sum(a[i - k:i]) + dp[i - k][j - 1])
			dp[i][j] = max(dp[i][j], dp[i - 1][j])
	
	return dp[n][x]


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
x = int(data[2])
a = list(map(int, data[3:]))

# Output result
print(max_beauty_pictures(n, k, x, a))
