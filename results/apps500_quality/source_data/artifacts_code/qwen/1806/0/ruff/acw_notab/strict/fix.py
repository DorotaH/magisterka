def can_cover(intervals, x, y):
    return any(l <= x and y <= r for l, r in intervals)


def min_intervals_to_cover(intervals, x, y):
    # If there is no interval that covers [x, y], return -1
    if not can_cover(intervals, x, y):
        return -1

    # Sort intervals by their right endpoint
    intervals.sort(key=lambda x: x[1])

    # Use a greedy approach to select the minimum number of intervals
    selected_intervals = []
    for l, r in intervals:
        if not selected_intervals or l > selected_intervals[-1][1]:
            selected_intervals.append((l, r))

    return len(selected_intervals)


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    intervals = []
    for i in range(n):
        l = int(data[2 + i * 2])
        r = int(data[3 + i * 2])
        intervals.append((l, r))

    queries = []
    for i in range(m):
        x = int(data[2 + 2 * n + i * 2])
        y = int(data[3 + 2 * n + i * 2])
        queries.append((x, y))

    results = [min_intervals_to_cover(intervals, x, y) for x, y in queries]
    for result in results:
        print(result)


# Call the solve function to run the program
solve()
