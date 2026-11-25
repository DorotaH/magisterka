mod = 10**9 + 7

def solve():
    s = input()
    n = len(s)
    a_indices = [i for i in range(n) if s[i] == 'a']
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1]
        j = 0
        for k in range(i):
            if s[i-1] == 'b' and a_indices[j] < i-1:
                dp[i] = (dp[i] + dp[a_indices[j]]) % mod
                j += 1
            if a_indices[j] > i-1:
                break
    return dp[n]

print(solve())
