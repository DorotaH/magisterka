def  max_beauty_sum():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    if  k > x:
        return  -1

    if  1 == k:
        return  sum(a, 0)

    dp = []
    for _ in range(n + 1):
        dp.append([-1 for _ in range(x + 1)])

    dp[0][0] = 0

    for i in range(1, 1 + n):
        for j in range(min(i, x) + 1):
            if not j == 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1])
                if i >= k:
                    dp[i][j] = max(dp[i][j], dp[i - k][j] + a[i - k] * min(k, j))
            else:
                dp[i][j] = dp[i - 1][j]

    return  dp[n][x]

print(max_beauty_sum())
