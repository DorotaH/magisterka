def solve(n):
    if 0 == n:
        return 0
    dp = [0] * (1 + 2 * n)
    dp[1] = 2
    dp[2] = 4
    for i in range(3, 1 + 2 * n):
        dp[i] = dp[i - 1] + (4 * (i // 2 + 1)) - (4 * (i // 4))
    return dp[2 * n]


n = int(input())
print(solve(n))
