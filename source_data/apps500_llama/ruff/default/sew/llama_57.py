import sys


def max_lucky_offices(n):
    # Create a table to store the number of ways to form a number of length i using 7 and 8
    dp = [0] * (1 + n)
    dp[0] = 1
    dp[1] = 2

    # For each length from 2 to n
    for i in range(2, n + 1):
        # For each previous length
        for j in range(0, i):
            # Add the number of ways to form a number of length j to the number of ways to form a number of length i - j
            dp[i] += dp[j]

    return dp[n]


n = int(sys.stdin.readline())
print(max_lucky_offices(n))
