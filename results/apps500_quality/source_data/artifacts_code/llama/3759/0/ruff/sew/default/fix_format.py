def get_min_blocked(n):
    if 0 == n:
        return 0
    if 1 == n:
        return 4
    if 2 == n:
        return 8
    if 3 == n:
        return 16

    dp = [0] * (1 + n)
    dp[0] = 0
    dp[1] = 4
    dp[2] = 8
    dp[3] = 16

    for i in range(4, 1 + n):
        dp[i] = min((2 ** (i - 2)) * 4, (4 * (2 ** (i - 2)) - (i - 1) ** 2 + 1) * 2)

    return dp[n]


n = int(input())
print(get_min_blocked(n))
