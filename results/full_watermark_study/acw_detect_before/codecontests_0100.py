import sys
input = sys.stdin.readline

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	dp = [[2100] * 2100 for _ in range(n)]
	dp[0][a[0]] = a[0]
	
	for i in range(1, n):
		for j in range(2100):
			nj = max(j - a[i], 0)
			dp[i][nj] = min(dp[i][nj], max(a[i] - j, 0) + dp[i - 1][j])
			
			if a[i] + j < 2100:
				dp[i][a[i] + j] = min(dp[i][a[i] + j], max(a[i] - (dp[i - 1][j] - j), 0) + dp[i - 1][j])
	
	print(min(dp[-1]))
