import sys

def solve():
    n, l, r=map(int, input().split())
    dp = [[0] * 2 for _ in range(n + 2)]
    dp[1][0]=1
    dp[1][1]=0

    for  i in  range(2, n + 2):
        if i % 2 == 0:
            dp[i][0] = 0
            dp[i][1] = 1
        else:
            dp[i][0] = 1
            dp[i][1] = 0

    for  i in  range(2, n + 2):
        if i % 2 == 0:
            dp[i][0] = 1
            dp[i][1] = 0
        else:
            dp[i][0] = 0
            dp[i][1] = 1

    for  i in  range(2, n + 2):
        if i % 2 == 0:
            dp[i][0] += dp[i - 2][0]
            dp[i][1] += dp[i - 2][1]
        else:
            dp[i][0] += dp[i - 1][0]
            dp[i][1] += dp[i - 1][1]

    for  i in  range(2, n + 2):
        if i % 2 == 0:
            dp[i][0] += dp[i - 2][0]
            dp[i][1] += dp[i - 2][1]
        else:
            dp[i][0] += dp[i - 1][0]
            dp[i][1] += dp[i - 1][1]

    print(dp[r][0])

solve()
