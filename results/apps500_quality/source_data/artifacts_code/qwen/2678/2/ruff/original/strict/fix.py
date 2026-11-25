def min_covering_set_size(intervals):
    # Sort intervals by their end points
    intervals.sort(key=lambda x: x[1])

    # Initialize the set of covering integers
    covering_set = set()
    end = 0

    # Iterate over the sorted intervals
    for start, e in intervals:
        # If the current interval starts after the last covered point
        if start > end:
            # Add the end point of the current interval to the covering set
            covering_set.add(e)
            # Update the end point to the end of the current interval
            end = e

    # Return the size of the covering set
    return len(covering_set)

# Read input
N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

# Print the result
print(min_covering_set_size(intervals))
