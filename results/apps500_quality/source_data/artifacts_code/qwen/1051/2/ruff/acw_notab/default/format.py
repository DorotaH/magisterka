def min_declines(K, ranks):
    # The minimum number of declines is the number of gaps between the known ranks
    # and the positions they would occupy if they were all accepted.
    # Since the highest rank is 10^6 and the highest known rank is the K-th highest,
    # the minimum number of declines is the number of integers between the highest
    # known rank and 10^6 that are not in the list of known ranks.
    # This is equivalent to 10^6 - the highest known rank + 1 minus K.
    return 10**6 - ranks[-1] + 1 - K


# Read input from standard input
K = int(input())
ranks = list(map(int, input().split()))

# Calculate and print the minimum number of declines
print(min_declines(K, ranks))
