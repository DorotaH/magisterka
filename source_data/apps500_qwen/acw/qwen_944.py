MOD = 998244353


def count_suitable_colorings(n, k):
	if n == 1:
		return 0
	
	dp = [2 * [0] for _ in range(n)]
	dp[0][0] = dp[0][1] = 1
	
	for i in range(1, n):
		dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
		dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
	
	total_beautiful = (dp[-1][1] + dp[-1][0]) % MOD
	
	def count_rectangles(n, k):
		if k == 1:
			return 0
		return (n * (n - k + 1) * (n - k + 1)) % MOD
	
	rectangles = 0
	for i in range(1, n):
		for j in range(1, n):
			rectangles += count_rectangles(j, k) * count_rectangles(i, k)
	
	return (total_beautiful - rectangles + MOD) % MOD


n, k = map(int, input().split())
print(count_suitable_colorings(n, k))
