def max_sum_increasing_subseq(a, n, index, k):
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        dp[0][i] = a[i] + a[0] if a[i] > a[0] else a[i]
    for i in range(1, n):
        for j in range(n):
            if a[j] > a[i] and j > i:
                dp[i][j] = max(dp[i - 1][i] + a[j], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[index][k]
