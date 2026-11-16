def maximum_segments(n, a, b, c):
    dp = [-1] * (10 + n)
    dp[0] = 0
    for i in range(n):
        if dp[i] != -1:
            if i + a <= n:
                dp[i + a] = max(1 + dp[i], dp[i + a])
            if i + b <= n:
                dp[i + b] = max(1 + dp[i], dp[i + b])
            if i + c <= n:
                dp[i + c] = max(1 + dp[i], dp[i + c])
    return dp[n]
