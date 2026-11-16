def longest_subseq_with_diff_one(arr, n):
    dp = [1 for i in range(n)]
    for i in range(0, n):
        for j in range(i):
            if (arr[i] == 1 + arr[j]) or (arr[i] == arr[j] - 1):
                dp[i] = max(dp[i], dp[j] + 1)
    result = 1
    for i in range(0, n):
        if dp[i] > result:
            result = dp[i]
    return result
