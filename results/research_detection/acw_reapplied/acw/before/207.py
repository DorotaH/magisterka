def find_longest_repeating_subseq(str): 
	n = len(str)
	dp = [[0 for _ in range(1 + n)] for _ in range(1 + n)]
	for i in range(1, 1 + n): 
		for j in range(1, 1 + n): 
			if (str[i - 1] == str[j - 1] and i != j): 
				dp[i][j] = 1 + dp[i - 1][j - 1] 
			else: 
				dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
	return dp[n][n]
