import  sys
import  math


def solve():
    n, m = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    g, r = map(int, sys.stdin.readline().split())

    d.sort()
    d = [0] + d + [n]

    if d[-1] == 0:
        print(-1)
        return None

    dp = []
    for _ in range(n + 1):
        dp.append([float("inf")] * (n + 1))
    dp[0][0] = 0

    for  i in  range(1, 1 + n):
        for  j in  range(n + 1):
            if  dp[i - 1][j] != float("inf"):
                if  j != 0:
                    dp[i][j]=min(dp[i][j], dp[i - 1][j] + 1)
                if  i >= 2:
                    dp[i][j-1]=min(dp[i][j-1], dp[i - 1][j] + 1)
                if  j != n:
                    dp[i][j + 1]=min(dp[i][j + 1], dp[i - 1][j] + 1)

    for  i in  range(1, 1 + m):
        if d[i]-d[i-1]>g:
            print(-1)
            return

        for  j in  range(n + 1):
            if  0 != j:
                dp[d[i-1]][j]=min(dp[d[i-1]][j], dp[d[i-1]+g][j]+g)
            if  n != j:
                dp[d[i-1]][j + 1]=min(dp[d[i-1]][j + 1], dp[d[i-1]+g][j]+g)
            if  0 != j:
                dp[d[i-1]][j-1]=min(dp[d[i-1]][j-1], dp[d[i-1]+g][j]+g)

    ans = float("inf")
    for  i in  range(0, n + 1):
        if dp[n][i]!=float("inf"):
            ans=min(ans, dp[n][i]+((n - d[-2]) // g * (g + r))+((n - d[-2]) % g))

    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


solve()
