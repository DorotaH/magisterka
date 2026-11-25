def get_min_blocked(n):
    if n == 0:
        return 0
    if n == 1:
        return 4
    if n == 2:
        return 8
    if n == 3:
        return 16

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 4
    dp[2] = 8
    dp[3] = 16

    for i in range(4, n + 1):
        dp[i] = min(4 * (2 ** (i - 2)), 2 * (4 * (2 ** (i - 2)) - (i - 1) ** 2 + 1))

    return dp[n]


n = int(input())
print(get_min_blocked(n))
