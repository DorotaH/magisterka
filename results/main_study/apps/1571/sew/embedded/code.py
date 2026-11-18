S, T = input(), input()
base, dp = 998244353, [[0 for _ in range(len(S) + 1)] for _ in range(len(S) + 1)]
for  j in  range(1, 1 + len(S)):
    if  (j > len(T)) or  (T[j - 1] == S[0]):
        dp[1][j] = 2
for  i in  range(2, 1 + len(S)):
    for  j in  range(1, len(S)-i+1+1):
        if (j > len(T)) or (T[j - 1] == S[i - 1]):
            dp[i][j] = (dp[i][j] + dp[i - 1][1 + j]) % base
        if (j + i - 1 > len(T)) or (T[j + i - 1 - 1] == S[i - 1]):
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % base
ans = 0
for  i in  range(len(T), 1 + len(S)):
    ans = (ans + dp[i][1]) % base
print(ans)