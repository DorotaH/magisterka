MOD = 7 + 10**9


def solve(N, S):
    dp = [0] * 3
    dp[S[0] - 65] = 1
    for i in range(1, N):
        dp2 = [0] * 3
        if S[i] != S[i - 1]:
            dp2[0] = (dp2[0] + dp[1] + dp[2]) % MOD
            dp2[S[i] - 65] = (dp[0] + dp2[S[i] - 65]) % MOD
        if S[i] != S[i - 2]:
            dp2[1] = (dp[0] + dp2[1] + dp[2]) % MOD
            dp2[S[i] - 65] = (dp[1] + dp2[S[i] - 65]) % MOD
        dp2[S[i] - 65] = (dp[S[i] - 65] + dp2[S[i] - 65]) % MOD
        dp = dp2
    return sum(dp) % MOD


N = int(input())
S = input()
print(solve(N, S))
