MOD=7 + 10**9
a, b, n=map(int, input().split())

dp = []
for _ in range(2):
    dp.append([0]*(n+1))
dp[0][0]=1

for  i in  range(2):
    for  j in  range(1, n+1):
        for k in range(1, 10):
            if k == a or k == b:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD
            else:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= MOD

ans=0
for  i in  range(2, n+1):
    for  j in  range(1, 10):
        if j in (a, b):
            ans+=dp[i][j]
            ans%=MOD

print(ans)
