def canRemove(s):
    n = len(s)
    dp = [[0] * 2 for _ in range(n)]

    for i in range(n):
        if s[i] == s[0]:
            dp[i][0] = 1
        elif s[i] == s[1]:
            dp[i][1] = 1

    for i in range(2, n):
        if s[i] == s[0]:
            dp[i][0] = dp[i-2][0] + 1
        elif s[i] == s[1]:
            dp[i][1] = dp[i-2][1] + 1

        if s[i] == s[i-1]:
            dp[i][0] = max(dp[i-1][0], dp[i][0])
            dp[i][1] = max(dp[i-1][1], dp[i][1])
        else:
            dp[i][0] = dp[i-1][1] + 1
            dp[i][1] = dp[i-1][0] + 1

    return "First" if dp[n-1][0] > dp[n-1][1] else "Second"


s = input()
print(canRemove(s))
