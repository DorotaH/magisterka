import sys

n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n
for i in range(1, n):
	dp[i] = a[i - 1] + dp[i - 1]

for i in range(1, n - 1):
	dp[i + 1] = min(dp[i] + c + b[i], dp[i] + a[i])

for i in range(2, n):
	for j in range(i - 1, 0, -1):
		dp[j] = min(dp[j], dp[i] + a[i - 1] + a[i - 2] + (b[i - 1] + c + b[i - 2] if 1 < j else 0))

print(' '.join(map(str, dp)))
