MOD = 1000000007

def count_excellent_numbers(a, b, n):
    # Initialize DP table
    dp = [[0] * (b + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, b + 1):
            dp[i][j] = dp[i - 1][j - 1]  # Count numbers ending with digit b
            if a < j:
                dp[i][j] = (dp[i][j] + dp[i - 1][a]) % MOD  # Count numbers ending with digit a
    
    # Sum up all the excellent numbers of length n
    result = sum(dp[n][j] for j in range(a, b + 1)) % MOD
    
    return result

# Read input
a, b, n = map(int, input().split())

# Output the result
print(count_excellent_numbers(a, b, n))
