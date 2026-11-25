MOD = 998244353


def count_tilings(w, h):
    if w == 0 or h == 0:
        return 1
    if w == 1:
        return 2 ** h
    if h == 1:
        return 2 ** w

    dp = [[0] * (h + 1) for _ in range(1 + w)]
    dp[1][1] = 2
    dp[2][1] = 4
    dp[1][2] = 4
    dp[2][2] = 8

    for i in range(3, 1 + w):
        dp[i][1] = (2 * dp[i - 1][1] + 2 * dp[i - 2][1]) % MOD
    for j in range(3, h + 1):
        dp[1][j] = (2 * dp[1][j - 1] + 2 * dp[1][j - 2]) % MOD

    for i in range(3, 1 + w):
        for j in range(3, h + 1):
            dp[i][j] = (2 * dp[i - 1][j] + 2 * dp[i][j - 1]) % MOD

    return dp[w][h]


# Read input
w, h = map(int, input().split())

# Print output
print(count_tilings(w, h))
