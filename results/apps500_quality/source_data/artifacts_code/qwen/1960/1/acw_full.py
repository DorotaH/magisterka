def solve():
	n = int(input())
	a = list(map(int, input().split()))
	
	# Compute the length of the longest increasing subsequence
	dp = n * [1]
	for i in range(1, n):
		for j in range(i):
			if a[j] < a[i]:
				dp[i] = max(dp[i], dp[j] + 1)
	
	max_len = max(dp)
	
	# Determine the groups
	group = [0] * n
	for i in range(n):
		if dp[i] == max_len:
			group[i] = 3
		elif dp[i] > 1:
			group[i] = 2
		else:
			group[i] = 1
	
	# Output the result
	print(''.join(map(str, group)))


# Call the solve function
solve()
