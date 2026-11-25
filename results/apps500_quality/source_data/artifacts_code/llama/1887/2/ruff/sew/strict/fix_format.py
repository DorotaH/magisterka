import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(n):
    if not i % 2 == 0:
        dp[i + 1] = max(dp[i], dp[i - 1] + b[i])
    else:
        dp[i + 1] = max(dp[i], dp[i - 1] + a[i])

print(dp[n])
