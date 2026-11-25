import sys

input=sys.stdin.readline

MOD=998_244_353

def  solve():
    n, k=map(int, input().split())
    a=list(map(int, input().split()))

    dp = []
    for _ in range(n + 1):
        dp.append([0 for _ in range(k + 1)])
    dp[0][0]=1

    for  i in  range(1, 1 + n):
        for  j in  range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i-1]!=-1:
                dp[i][j] += dp[i - 1][abs(a[i - 1] - j)]
            if i>=2 and a[i-1]==-1 and a[i-2]==-1:
                dp[i][j] += dp[i - 2][j]

    result=0
    for  i in  range(k + 1):
        result = result + dp[n][i]
        result = result % MOD

    print(result)

solve()
