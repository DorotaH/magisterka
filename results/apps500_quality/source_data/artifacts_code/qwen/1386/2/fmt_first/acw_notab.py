MOD = 998244353


def count_tilings(w, h):
    if w == 1 and h == 1:
        return 4
    if w == 1:
        return 2 ** (h - 1)
    if h == 1:
        return 2 ** (w - 1)

    dp = [[0] * (h + 1) for _ in range(1 + w)]
    dp[1][1] = 4
    dp[1][2] = 2
    dp[2][1] = 2

    for i in range(3, 1 + w):
        dp[i][1] = 2 * dp[i - 1][1] % MOD
    for j in range(3, h + 1):
        dp[1][j] = 2 * dp[1][j - 1] % MOD

    for i in range(2, 1 + w):
        for j in range(2, h + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[w][h]


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
w = int(data[0])
h = int(data[1])

# Output result
print(count_tilings(w, h))
