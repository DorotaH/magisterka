import sys


def min_watering_time():
    n, k = map(int, input().split())
    buckets = list(map(int, input().split()))

    # Initialize dp array to store the minimum time required to water the garden for each segment length from 1 to k
    dp = [float("inf")] * (k + 1)

    # Base case: it takes 0 hours to water a segment of length 0
    dp[0] = 0

    # Iterate over each possible segment length
    for i in range(1, k + 1):
        # For each possible segment length, check all buckets
        for j, a in enumerate(buckets):
            # If the current bucket can water the current segment, update dp[i]
            if i >= a:
                dp[i] = min(dp[i], 1 + dp[i - a])

    # The minimum time required to water the garden is stored in dp[k]
    return dp[k]


print(min_watering_time())
