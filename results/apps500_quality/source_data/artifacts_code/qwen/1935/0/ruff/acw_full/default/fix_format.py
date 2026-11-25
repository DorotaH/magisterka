def min_time_to_cross_road(n, m, d, g, r):
    d.sort()
    if d[1] - d[0] < g or g > d[-1] - d[-2]:
        return -1

    dp = [[float("inf")] * (1 + n) for _ in range(2)]
    dp[0][0] = 0

    for i in range(1, 2):
        for j in range(1 + n):
            if dp[i - 1][j] == float("inf"):
                continue
            if 0 < j and j - 1 != d[0]:
                dp[i][j - 1] = min(dp[i][j - 1], dp[i - 1][j] + 1)
            if n > j and 1 + j != d[-1]:
                dp[i][1 + j] = min(dp[i][1 + j], dp[i - 1][j] + 1)
            dp[i][j] = min(dp[i][j], g + dp[i - 1][j])
    return min(dp[1][n], dp[0][n])


# Read input
n, m = map(int, input().split())
d = list(map(int, input().split()))
g, r = map(int, input().split())

# Output the result
print(min_time_to_cross_road(n, m, d, g, r))
