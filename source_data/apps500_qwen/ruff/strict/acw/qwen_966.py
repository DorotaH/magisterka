MOD = 1000000007


def count_excellent_numbers(a, b, n):
    # Initialize DP table
    dp = [[0] * (1 + b) for _ in range(1 + n)]
    dp[0][0] = 1

    # Fill the DP table
    for i in range(1, 1 + n):
        for j in range(1, 1 + b):
            dp[i][j] = dp[i - 1][j - 1]  # Count numbers ending with digit b
            if a < j:
                dp[i][j] = (
                    dp[i][j] + dp[i - 1][a]
                ) % MOD  # Count numbers ending with digit a

    return sum(dp[n][j] for j in range(a, 1 + b)) % MOD


# Read input
a, b, n = map(int, input().split())

# Output the result
print(count_excellent_numbers(a, b, n))
