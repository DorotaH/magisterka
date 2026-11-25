import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])

if N == 1:
	print(K)
else:
	dp = [0] * (N + 1)
	dp[1] = K
	dp[2] = (K - 1) * K
	for i in range(3, N + 1):
		dp[i] = (K - 1) * dp[i - 1]
	print(dp[N])
