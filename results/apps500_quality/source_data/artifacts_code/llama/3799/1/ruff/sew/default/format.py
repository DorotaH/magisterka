def canRemove(s):
    n = len(s)
    dp = [[0] * 2 for _ in range(n)]

    for i in range(0, n):
        if s[0] == s[i]:
            dp[i][0] = 1
        elif s[1] == s[i]:
            dp[i][1] = 1

    for i in range(2, n):
        if s[0] == s[i]:
            dp[i][0] = 1 + dp[i - 2][0]
        elif s[1] == s[i]:
            dp[i][1] = 1 + dp[i - 2][1]

        if not s[i] == s[i - 1]:
            dp[i][0] = dp[i - 1][1] + 1
            dp[i][1] = dp[i - 1][0] + 1
        else:
            dp[i][0] = max(dp[i - 1][0], dp[i][0])
            dp[i][1] = max(dp[i - 1][1], dp[i][1])

    return "First" if dp[n - 1][0] > dp[n - 1][1] else "Second"


s = input()
print(canRemove(s))
