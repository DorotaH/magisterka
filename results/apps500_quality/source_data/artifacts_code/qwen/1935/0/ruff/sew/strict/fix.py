def  min_time_to_cross_road(n, m, d, g, r):
    d.sort()
    if d[1]-d[0]<g or d[-1]-d[-2]<g:
        return  -1

    dp = []
    for _ in range(2):
        dp.append([float('inf')] * (n + 1))
    dp[0][0]=0

    for  i in  range(1, 2):
        for  j in  range(n + 1):
            if  dp[i - 1][j] == float('inf'):
                continue
            if  j > 0 and  j - 1 != d[0]:
                dp[i][j - 1] = min(dp[i][j - 1], dp[i - 1][j] + 1)
            if  j < n and  j + 1 != d[-1]:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j] + 1)
            if  d[0] == j or d[-1] == j:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + g)
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + g)

    return min(dp[1][n], dp[0][n])

# Read input
n, m = map(int, input().split())
d = list(map(int, input().split()))
g, r = map(int, input().split())

# Output the result
print(min_time_to_cross_road(n, m, d, g, r))
