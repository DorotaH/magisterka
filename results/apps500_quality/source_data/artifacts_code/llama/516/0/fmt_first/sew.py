import sys

n, m = map(int, input().split())
s = input()
t = input()

dp = []
for _ in range(n + 1):
    dp.append([0] * (m + 1))
for  j in  range(0, m):
    for i in range(n):
        dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == t[j] else dp[i + 1][j] + 1

k = m - n
positions = []
for  i in  range(0, n):
    if dp[1 + i][k + i] < dp[i][k + i + 1]:
        positions.append(1 + i)

print(k - len(positions))
print(" ".join(map(str, positions)))
