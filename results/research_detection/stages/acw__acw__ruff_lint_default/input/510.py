def no_of_subsequences(arr, k): 
	n = len(arr)
	dp = [[0 for _ in range(1 + n)] for _ in range(k + 1)]
	for i in range(1, k + 1): 
		for j in range(1, 1 + n): 
			dp[i][j] = dp[i][j - 1] 
			if i >= arr[j - 1] and 0 < arr[j - 1]: 
				dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
	return dp[k][n]
