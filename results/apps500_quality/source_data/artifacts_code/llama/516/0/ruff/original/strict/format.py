import sys

n, m = map(int, input().split())
s = input()
t = input()

dp = [[0] * (m + 1) for _ in range(n + 1)]
for j in range(m):
    for i in range(n):
        dp[i + 1][j + 1] = dp[i][j] + 1 if t[j] == s[i] else dp[i + 1][j] + 1

k = m - n
positions = []
for i in range(n):
    if dp[i + 1][k + i] < dp[i][k + i + 1]:
        positions.append(i + 1)

print(k - len(positions))
print(" ".join(map(str, positions)))
