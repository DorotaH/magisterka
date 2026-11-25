import sys

input = sys.stdin.readline

n = int(input())
h = [0] + [int(x) for x in input().split()]

INF = 2 * 10**9
dp = [[INF] * (1 + n) for _ in range(1 + n)]
dp[n][n] = 0

for i in range(n - 1, 0, -1):
    dp[i][n] = 1
    for j in range(i - 1, 0, -1):
        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
        if h[j] < h[i]:
            dp[i][j] = min(
                dp[i][j], dp[i + 1][min(k for k in range(1 + j, 1 + n) if h[k] > h[i])]
            )
        elif h[j] > h[i]:
            dp[i][j] = min(
                dp[i][j], dp[i + 1][min(k for k in range(1 + j, 1 + n) if h[k] < h[i])]
            )
        if i + 1 <= j:
            dp[i][j] = min(dp[i][j], dp[i + 1][1 + j])

print(dp[1][1])
