for _ in range(int(input())):
    n, k, l = map(int, input().split())
    line = list(map(int, input().split()))
    line.append(-1000)
    dp = [[False] * (2 * k) for _ in range(n + 2)]
    for i in range(2 * k):
        dp[0][i] = True
    for i in range(1, n + 2):
        for j in range(2 * k):
            if j < k and line[i - 1] + j <= l and (dp[i - 1][(j - 1) % (2 * k)] or dp[i][(j - 1) % (2 * k)]):
                dp[i][j] = True
            if j >= k and line[i - 1] + 2 * k - j <= l and (dp[i - 1][j - 1] or dp[i][j - 1]):
                dp[i][j] = True
    if max(dp[n + 1]) == True:
        print("Yes")
    else:
        print("No")
