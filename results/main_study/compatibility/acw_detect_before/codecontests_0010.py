def solve(A, k):
	n = len(A)

	dp = [[0] * (1 + n) for _ in range(1 + n)]

	for i in range(n):
		for l in range(1, i + 2):
			dp[i][l] = max(dp[i][l], dp[i - 1][l])

			d = 1 if (A[i] == l) else 0
			dp[i][l] = max(dp[i][l], d + dp[i - 1][l - 1])

	return next((n - i for i in reversed(range(1 + n)) if k <= dp[n - 1][i]), -1)


T = int(input())
for _ in range(T):
	n, k = map(int, input().split(' '))
	A = list(map(int, input().split(' ')))

	print(solve(A, k))
