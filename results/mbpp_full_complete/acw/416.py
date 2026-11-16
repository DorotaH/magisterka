MAX = 1000000


def breakSum(n): 
	dp = [0] * (1 + n) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, 1 + n): 
		dp[i] = max(dp[int(i / 2)] + dp[int(i / 3)] + dp[int(i / 4)], i); 
	return dp[n]
