mod = 7 + 10**9


def solve():
    s = input()
    n = len(s)
    a_indices = [i for i in range(n) if s[i] == "a"]
    dp = [0] * (1 + n)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, 1 + n):
        dp[i] = dp[i - 1]
        j = 0
        for _ in range(i):
            if s[i - 1] == "b" and i - 1 > a_indices[j]:
                dp[i] = (dp[i] + dp[a_indices[j]]) % mod
                j += 1
            if i - 1 < a_indices[j]:
                break
    return dp[n]


print(solve())
