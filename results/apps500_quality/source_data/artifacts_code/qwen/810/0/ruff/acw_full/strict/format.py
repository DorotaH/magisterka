MOD = 1000000007


def count_excellent_numbers(a, b, n):
    if n == 1:
        return 2
    dp = [[0] * (1 + b) for _ in range(1 + n)]
    dp[1][a] = dp[1][b] = 1
    for i in range(2, 1 + n):
        for j in range(a, 1 + b):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    return sum(dp[n]) % MOD


a, b, n = map(int, input().split())
print(count_excellent_numbers(a, b, n))
