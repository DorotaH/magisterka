MOD = 1000000007


def count_excellent_numbers(a, b, n):
    # Calculate the sum of the two favourite digits
    sum_ab = a + b

    # Calculate the difference between the two favourite digits
    diff_ab = b - a

    # Create a 2D array to store the number of good numbers
    dp = [[0] * (1 + n) for _ in range(sum_ab + 1)]

    # There is 1 way to get a sum of 0 (no digits)
    dp[0][0] = 1

    # For each possible sum from 1 to sum_ab
    for s in range(1, sum_ab + 1):
        # If the current sum is equal to a, the number of good numbers is the same as the number of good numbers with sum a - b
        dp[s][1] = dp[s - a][1]

        # For each possible length from 2 to n
        for i in range(2, 1 + n):
            # If the current sum is equal to a, the number of good numbers is the same as the number of good numbers with sum a - b
            # If the current sum is equal to a + b, the number of good numbers is the same as the number of good numbers with sum a - b + a - b
            # If the current sum is between a and a + b, the number of good numbers is the sum of the number of good numbers with sum s - a and the number of good numbers with sum s - b
            dp[s][i] = (dp[s - b][i - 1] + dp[s - a][i - 1]) % MOD

    # The total number of excellent numbers is the sum of the number of good numbers with sum a and the number of good numbers with sum b
    total = (dp[b][n] + dp[a][n]) % MOD

    # The number of excellent numbers that contain both a and b is the number of good numbers with sum a + b
    contain_ab = dp[sum_ab][n]

    # The final answer is the total number of excellent numbers minus the number of excellent numbers that contain both a and b
    return (total - contain_ab + MOD) % MOD


# Read the input from standard input
a, b, n = map(int, input().split())

# Print the answer to standard output
print(count_excellent_numbers(a, b, n))
