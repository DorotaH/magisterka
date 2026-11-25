def min_replacements(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (1 + m) for _ in range(1 + n)]
    for i in range(1 + n):
        dp[i][0] = i
    for j in range(1, 1 + m):
        dp[0][j] = j
    for i in range(1, 1 + n):
        for j in range(1, 1 + m):
            if s[i - 1] == t[j - 1] or s[i - 1] == '?' or t[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    k = dp[n][m]
    positions = []
    i, j = n, m
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1] or s[i - 1] == '?' or t[j - 1] == '?':
            i -= 1
        else:
            if dp[i - 1][j] == dp[i][j - 1]:
                positions.append(i)
            else:
                i -= 1
        j -= 1
    return str(k), ' '.join(map(str, reversed(positions)))


n, m = map(int, input().split())
s = input()
t = input()
print(min_replacements(s, t))
