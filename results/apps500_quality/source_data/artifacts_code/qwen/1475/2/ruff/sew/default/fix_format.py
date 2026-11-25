MOD = 7 + 10**9


def count_ways(n, b, k, x, digits):
    # Initialize a dictionary to count occurrences of each digit in each position
    count = [{} for _ in range(n)]

    # Count occurrences of each digit in each position
    for _ in range(b):
        for i, d in enumerate(digits, 0):
            if d in count[i]:
                count[i][d] += 1
            else:
                count[i][d] = 1

    # Initialize DP table
    dp = [100 * [0] for _ in range(n)]
    dp[0][k % x] = 1

    # Fill the DP table
    for i in range(1, n):
        for j in range(100):
            for d in count[i]:
                dp[i][((j * 10) + d) % x] += count[i][d] * dp[i - 1][j]
                dp[i][((j * 10) + d) % x] %= MOD

    return dp[n - 1][0]


# Read input
n, b, k, x = map(int, input().split())
digits = list(map(int, input().split()))

# Output the result
print(count_ways(n, b, k, x, digits))
