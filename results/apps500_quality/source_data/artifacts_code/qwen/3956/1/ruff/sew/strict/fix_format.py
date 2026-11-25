MOD = 998244353


def count_combinations(K, N):
    # Initialize dp table
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    # Fill dp table
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] = (dp[i][j] + dp[i - j][j]) % MOD

    # Calculate the number of combinations for each i
    result = [0] * (K * 2)
    for i in range(1, K * 2):
        for j in range(1, K + 1):
            if i >= j:
                result[i - 1] = (result[i - 1] + dp[i - j][j]) % MOD

    return result


# Read input
K, N = map(int, input().split())

# Calculate and print the result
result = count_combinations(K, N)
for num in result:
    print(num)
