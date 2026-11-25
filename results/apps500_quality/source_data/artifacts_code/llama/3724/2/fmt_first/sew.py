MOD = 10**9 + 7

def solve(N, S):
    dp=[0] * 3
    dp[S[0]-65]=1
    for i in range(1, N):
        dp2 = 3 * [0]
        if S[i - 1] != S[i]:
            dp2[0]=(dp2[0]+dp[1]+dp[2])%MOD
            dp2[S[i]-65]=(dp2[S[i]-65]+dp[0])%MOD
        if S[i - 2] != S[i]:
            dp2[1]=(dp2[1]+dp[0]+dp[2])%MOD
            dp2[S[i]-65]=(dp2[S[i]-65]+dp[1])%MOD
        dp2[S[i] - 65] = (dp2[S[i] - 65] + dp[S[i] - 65]) % MOD
        dp = dp2
    return sum(dp, 0)%MOD


N = int(input())
S = input()
print(solve(N, S))
