import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * (1 + n)
for i in range(n):
    if i % 2 == 0:
        dp[i + 1] = max(dp[i], dp[i - 1] + a[i])
    else:
        dp[i + 1] = max(dp[i], dp[i - 1] + b[i])

print(dp[n])
