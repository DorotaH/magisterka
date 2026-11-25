def min_time_to_reach_floors(n, c, a, b):
    # Initialize the dp array where dp[i] will store the minimum time to reach the i-th floor
    dp = [float("inf")] * n
    dp[0] = 0  # Starting from the 1st floor, the time is 0

    # Calculate the minimum time to reach each floor
    for i in range(1, n):
        # Time to reach the i-th floor using stairs
        dp[i] = min(dp[i], dp[i - 1] + sum(a[:i]))
        # Time to reach the i-th floor using elevator
        dp[i] = min(dp[i], dp[i - 1] + c + sum(b[:i]))

    return dp


# Read input
import sys

input = sys.stdin.read
data = input().split()

n, c = int(data[0]), int(data[1])
a, b = list(map(int, data[2 : n + 1])), list(map(int, data[n + 1 : 2 * n]))

# Calculate and print the result
result = min_time_to_reach_floors(n, c, a, b)
print(" ".join(map(str, result)))
