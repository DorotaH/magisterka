import sys


def read_input():
    N = int(sys.stdin.readline())
    intervals = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        intervals.append((a, b))
    return intervals


def compute_minimum_cover(intervals):
    # Sort intervals by their start value
    intervals.sort(key=lambda x: x[0])

    # Initialize the minimum cover and the current cover
    min_cover = current_cover = 0

    # Iterate over the sorted intervals
    for i, (a, b) in enumerate(intervals, 0):
        # If the current cover is not enough to cover the current interval
        if a > current_cover:
            # Add the minimum required cover to the current cover
            current_cover = a - 1

        # If the current cover is still not enough to cover the current interval
        if b > current_cover:
            # Add the minimum required cover to the current cover
            current_cover = current_cover + 1

        # Update the minimum cover
        min_cover = max(min_cover, current_cover)

    return 1 + min_cover


def main():
    intervals = read_input()
    result = compute_minimum_cover(intervals)
    print(result)


if __name__ == "__main__":
    main()
