import sys


def read_input():
    n, h = map(int, sys.stdin.readline().split())
    segments = list()
    for _ in range(n):
        x1, x2 = map(int, sys.stdin.readline().split())
        segments.append((x1, x2))
    return (n, h, segments)


def main():
    n, h, segments = read_input()

    # Initialize the maximum distance
    max_distance = 0

    # Process the segments
    segments.append((pow(10, 9), pow(10, 9)))
    i = 0
    for i in range(n):
        x1, x2 = segments[i]
        max_distance = max(max_distance, x1)
        i += 1
        x1, x2 = segments[i]
        max_distance = max(max_distance, x1)

    # Process the last segment
    x1, x2 = segments[-1]
    max_distance = max(max_distance, x2 - max_distance)

    # Process the plane's flight
    max_distance += pow(10, 9) - max_distance

    print(max_distance)


if __name__ == "__main__":
    main()
