import sys

def  solve():
    n, k, x=map(int, input().split())
    a=list(map(int, input().split()))

    dp = []
    for _ in range(x + 1):
        dp.append([0] * (n + 1))
    dp[0][0]=0

    for  j in  range(1, 1 + n):
        for  i in  range(1, min(x, j) + 1):
            dp[i][j] = dp[i][j - 1]
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + a[j - 1])

            for p in range(1, min(j // k, i) + 1):
                dp[i][j]=max(dp[i][j], dp[i-p][j-p]+a[j-1])

    if dp[x][n] == 0:
        print(-1)
    else:
        print(dp[x][n])

if __name__ == '__main__':
    solve()