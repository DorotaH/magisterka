def max_beauty_sum():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    if k > x:
        return -1

    if k == 1:
        return sum(a)

    dp = [[-1 for _ in range(1 + x)] for _ in range(1 + n)]

    dp[0][0] = 0

    for i in range(1, 1 + n):
        for j in range(1 + min(i, x)):
            if j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], a[i - 1] + dp[i - 1][j - 1])
                if i >= k:
                    dp[i][j] = max(dp[i][j], dp[i - k][j] + a[i - k] * min(k, j))

    return dp[n][x]


print(max_beauty_sum())
