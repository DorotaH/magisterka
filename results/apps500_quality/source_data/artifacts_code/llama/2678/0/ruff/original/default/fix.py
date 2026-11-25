import sys


def solve(intervals):
    # Sort intervals by their start value
    intervals.sort(key=lambda x: x[0])

    # Initialize variables
    n = len(intervals)
    dp = [0] * n
    dp[0] = 1
    end = intervals[0][1]

    # Fill up dp table
    for i in range(1, n):
        if intervals[i][0] > end:
            dp[i] = dp[i-1] + 1
            end = intervals[i][1]
        elif intervals[i][0] <= end and intervals[i][1] >= end:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + 1
            end = intervals[i][1]

    # Return the minimum number of intervals
    return dp[-1]

def main():
    n = int(sys.stdin.readline())
    intervals = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        intervals.append((a, b))

    print(solve(intervals))

if __name__ == "__main__":
    main()
