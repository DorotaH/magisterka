M = 10**9 + 7

def odd_permutations(n, k):
    # Create a 2D array to store the number of permutations of oddness i modulo n
    dp = [[0] * (n * n + 1) for _ in range(n + 1)]

    # Initialize the base case
    dp[0][0] = 1

    # For each number of elements
    for i in range(1, n + 1):
        # For each possible oddness
        for j in range(i, min(i * (i + 1) // 2 + 1, n * n + 1)):
            # If this is the first element, there are two ways to place it
            if i == 1:
                dp[i][j] = 1
            else:
                # Otherwise, the number of permutations is the sum of the number of permutations
                # with the current element in the first position and the number of permutations
                # with the current element in the last position
                dp[i][j] = (dp[i - 1][j - i] + dp[i - 1][j + 1]) % M

    # Return the result
    return dp[n][k]

# Read the input
n, k = map(int, input().split())

# Print the result
print(odd_permutations(n, k))
