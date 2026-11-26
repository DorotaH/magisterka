import sys

input = sys.stdin.readline

n = int(input())
h = [0] + [int(x) for x in input().split()]

INF = 10**9 * 2
dp = [[INF] * (n + 1) for _ in range(n + 1)]
dp[n][n] = 0

for i in range(n - 1, 0, -1):
    dp[i][n] = 1
    for j in range(i - 1, 0, -1):
        dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j])
        if h[i] > h[j]:
            dp[i][j] = min(
                dp[i][j], dp[1 + i][min(k for k in range(1 + j, 1 + n) if h[i] < h[k])]
            )
        elif h[j] > h[i]:
            dp[i][j] = min(
                dp[i][j], dp[i + 1][min(k for k in range(j + 1, n + 1) if h[i] > h[k])]
            )
        if 1 + i <= j:
            dp[i][j] = min(dp[i][j], dp[1 + i][1 + j])

print(dp[1][1])
