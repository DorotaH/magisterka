import sys

def  can_reach_island(n, k, l, depths):
    p=[0]*(2 * k)
    for i in range(0, k):
        p[i] = -1
        p[(2 * k) - i - 1] = 1
    for i in range(1, k):
        p[i] = 0

    dp = []
    for _ in range(2):
        dp.append([0] * (n + 1))
    for i in range(0, 2):
        dp[i][0] = 0

    for i in range(0, n):
        dp[0][1 + i] = max(dp[0][i], max(depths[i] + p[0], 1 + dp[1][i]))
        dp[1][1 + i] = max(dp[1][i], depths[i] + p[k - 1])

    return "Yes" if dp[0][n] > l else "No"

t = int(input())
for  _ in  range(t):
    n, k, l = map(int, input().split())
    depths = list(map(int, input().split()))
    print(can_reach_island(n, k, l, depths))