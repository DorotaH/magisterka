def min_replacements(s, t):
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(0, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1] or s[i - 1] == "?" or t[j - 1] == "?":
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    k = dp[n][m]
    positions = []
    i = n
    j = m
    while i > 0 and j > 0:
        if not (s[i - 1] == t[j - 1] or s[i - 1] == "?" or t[j - 1] == "?"):
            if dp[i - 1][j] == dp[i][j - 1]:
                positions.append(i)
                j -= 1
            elif dp[i - 1][j] == dp[i][j - 1]:
                i -= 1
            else:
                i -= 1
                j -= 1
        else:
            i -= 1
            j -= 1
    return (str(k), " ".join(map(str, reversed(positions))))


n, m = map(int, input().split())
s = input()
t = input()
print(min_replacements(s, t))
