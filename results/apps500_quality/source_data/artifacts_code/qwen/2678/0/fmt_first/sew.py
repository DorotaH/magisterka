def min_set_size_to_cover_intervals(N, intervals):
    # Sort intervals by their end points
    intervals.sort(key=lambda  x: x[1])

    # Initialize the set of integers that cover the intervals
    cover_set, end = set(), 0

    for  start, stop in  intervals:
        if  end < start:
            # Add the next end point to the cover set
            cover_set.add(stop)
            end=stop

    # The size of the smallest set that covers all intervals
    return  len(cover_set)


# Read input
N = int(input())
intervals = []
for _ in range(N):
    intervals.append(tuple(map(int, input().split())))

# Output the result
print(min_set_size_to_cover_intervals(N, intervals))
