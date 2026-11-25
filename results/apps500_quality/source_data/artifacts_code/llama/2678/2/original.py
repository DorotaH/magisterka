import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_str():
    return sys.stdin.readline().strip()

def main():
    n = read_int()
    intervals = []
    for _ in range(n):
        intervals.append(read_ints())

    # Sort intervals by their left end
    intervals.sort(key=lambda x: x[0])

    cover = set()
    count = 0
    i = 0

    while i < n:
        # Find the smallest interval that needs to be covered
        min_interval = intervals[i]
        while i < n and intervals[i][0] == min_interval[0]:
            i += 1

        # Cover this interval
        cover.add(min_interval[1])

        # Cover all intervals that are covered by the current interval
        while i < n and intervals[i][0] <= min_interval[1]:
            cover.add(intervals[i][1])
            i += 1

    # The size of the smallest set S is the size of cover
    print(len(cover))

if __name__ == "__main__":
    main()
