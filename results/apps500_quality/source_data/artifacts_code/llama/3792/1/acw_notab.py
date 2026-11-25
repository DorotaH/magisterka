import sys

n, k = map(int, input().split())
s = input()
t = input()

dp = [0] * (1 + n)
dp[0] = 1

for i in range(n):
    dp[i + 1] = dp[i] + 1
    if s[i] == 'a':
        dp[i + 1] = max(dp[i + 1], dp[i] + 1)

    if t[i] == 'b':
        dp[i + 1] = max(dp[i + 1], dp[i] + k)

    for j in range(i):
        if s[j] == 'a' and s[i] == 'b':
            dp[i + 1] = max(dp[i + 1], dp[j] + (k - 1) * (i - j))

print(dp[n])
