def can_make(n, k, coins):
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0]=True

    for i in range(1, 1 + n):
        for j in range(1, k + 1):
            if j < coins[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - coins[i - 1]]

    result=list()
    for i in range(k + 1):
        if  dp[n][i]:
            result.append(i)

    return  result


n, k = map(int, input().split())
coins = list(map(int, input().split()))
result = can_make(n, k, coins)
print(len(result))
print(*result)