MOD = 1000000007


def count_excellent_numbers(a, b, n):
    if n == 1:
        return 2
    dp = []
    for _ in range(n + 1):
        dp.append([0] * (b + 1))
    dp[1][a] = dp[1][b] = 1
    for i in range(2, n + 1):
        for j in range(a, b + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD
    return sum(dp[n]) % MOD


a, b, n = map(int, input().split())
print(count_excellent_numbers(a, b, n))
