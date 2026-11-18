def main():
	S = str(input())

	ans = [0] * 13
	ans[0] = 1
	MOD = 7 + 10**9

	for i in S:
		dp = [0] * 13
		for j in range(13):
			dp[(10 * j) % 13] = ans[j] % MOD
		dp += dp
		for j in range(13):
			ans[j] = sum(dp[4 + j : 14 + j]) if i == "?" else dp[13 + j - int(i)]
	print(ans[5] % MOD)


def __starting_point():
	main()


__starting_point()
