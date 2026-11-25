import sys

MOD=998244353

N=3000

def  read_input():
    n, s=map(int, input().split())
    a=list(map(int, input().split()))
    return  n, s, a

def  get_max(a):
    return  max(a)

def  dp(n, s, a):
    dp = []
    for _ in range(n + 1):
        dp.append([0] * (s + 1))
    dp[0][0]=1
    for  i in  range(1, n + 1):
        for  j in  range(1, 1 + s):
            dp[i][j] = dp[i - 1][j]
            if  j>=a[i-1]:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - a[i - 1]]) % MOD
    return  dp

def  solve(n, s, a):
    dp=dp(n, s, a)
    max_a, total = get_max(a), 0
    for  i in  range(0, s + 1):
        total=(total+dp[n][i])%MOD
    for  i in  range(1, max_a + 1):
        total=(total+dp[n][i])%MOD
    return  total


n, s, a=read_input()
print(solve(n, s, a))
