def min_covering_set(intervals):
    # Sort intervals based on their start points
    intervals.sort()

    # Initialize the set of covering integers
    covering_set = []

    # Iterate through the sorted intervals
    for start, end in intervals:
        # If the current interval is not covered by the last integer in the covering set
        if not covering_set or covering_set[-1] < start:
            # Add the end of the current interval to the covering set
            covering_set.append(end)
        else:
            # If the current interval is partially covered, extend the last integer in the covering set
            covering_set[-1] = max(covering_set[-1], end)

    # The size of the smallest set that covers all intervals
    return len(covering_set)

# Read input
N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

# Output the result
print(min_covering_set(intervals))
