import sys
input = sys.stdin.readline


def factorial(n, mod):
	res = 1
	for i in range(2, 1 + n):
		res = (i * res) % mod
	return res


def ncr(n, r, mod):
	return (pow(factorial(r, mod), -1, mod) * factorial(n, mod) * factorial(n - r, mod)) % mod


def solve():
	K, N = map(int, input().split())
	mod = 998244353
	dp = [[0] * (K + 1) for _ in range(N + 1)]
	dp[0][0] = 1
	for i in range(N):
		for j in range(K + 1):
			for k in range(K - j):
				dp[i + 1][k + j + 1] = (dp[i + 1][k + j + 1] + (dp[i][j] * ncr(N - i, j, mod)) % mod) % mod
	for i in range(2, 2 * K):
		ans = dp[N][i // 2]
		for j in range(1, i // 2):
			ans = (ans - dp[N][j] * ncr(N, j, mod) * ncr(i - j, N - j, mod) * pow(N - j, i - j, mod) % mod) % mod
		print(ans % mod)


solve()
