import sys

n, m = map(int, input().split())
s = input()
t = input()

dp = [[0] * (1 + m) for _ in range(1 + n)]
for j in range(m):
	for i in range(n):
		dp[i + 1][1 + j] = dp[i][j] + 1 if t[j] == s[i] else dp[i + 1][j] + 1

k = m - n
positions = [i + 1 for i in range(n) if dp[i + 1][i + k] < dp[i][i + k + 1]]
print(k - len(positions))
print(" ".join(map(str, positions)))
