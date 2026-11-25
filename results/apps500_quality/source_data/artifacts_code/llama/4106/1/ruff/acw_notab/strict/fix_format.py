def max_sum_reposted_pictures():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[0] * (1 + n) for _ in range(1 + x)]
    for i in range(1, 1 + x):
        max_sum = 0
        for j in range(k, 1 + n):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - k] + a[j - 1])
            max_sum = max(max_sum, dp[i][j])

    return -1 if max_sum == 0 else max_sum


print(max_sum_reposted_pictures())
