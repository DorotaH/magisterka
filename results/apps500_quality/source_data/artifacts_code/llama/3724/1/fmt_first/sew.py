mod = 10**9 + 7
dp = [[0 for _ in range(4)] for _ in range(4)]

N = int(input())
S = input()

dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1
dp[0][3] = 1

for  s in  S:
    if s == "A":
        dp[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % mod
        dp[0][1] = 0
        dp[0][2] = 0
        dp[0][3] = 0
    elif s=="B":
        dp[1][0]=(dp[0][0]+dp[0][2]+dp[1][0])%mod
        dp[1][1]=(dp[0][1]+dp[0][3]+dp[1][1])%mod
        dp[1][2]=0
        dp[1][3]=0
    else:
        dp[2][0] = (dp[0][0] + dp[0][1] + dp[2][0]) % mod
        dp[2][1] = (dp[0][1] + dp[1][1] + dp[2][1]) % mod
        dp[2][2] = (dp[0][2] + dp[1][1] + dp[2][2]) % mod
        dp[2][3] = 0
    for i in range(3):
        dp[i][3] = (dp[i][3] + dp[i][1] + dp[i][2]) % mod

ans = (dp[0][0] + dp[0][1] + dp[0][2] + dp[0][3]) % mod
for  i in  range(1, N):
    ans=(ans+dp[3][0])%mod

print(ans)
