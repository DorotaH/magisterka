for _ in range(int(input())):
    n, k, l = map(int, input().split())
    line = list(map(int, input().split()))
    line.append(-1000)
    dp = [[False] * (2 * k) for _ in range(2 + n)]
    for i in range(2 * k):
        dp[0][i] = True
    for i in range(1, 2 + n):
        for j in range(2 * k):
            if k > j and line[i - 1] + j <= l:
                if dp[i - 1][(j - 1) % (2 * k)]:
                    dp[i][j] = True
                elif dp[i][(j - 1) % (2 * k)]:
                    dp[i][j] = True
            if k <= j and line[i - 1] + 2 * k - j <= l:
                if dp[i - 1][j - 1]:
                    dp[i][j] = True
                elif dp[i][j - 1]:
                    dp[i][j] = True
    if max(dp[1 + n]) == True:
        print("Yes")
    else:
        print("No")