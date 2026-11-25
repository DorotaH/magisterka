import sys

input = sys.stdin.readline


def distance(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2))


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solve():
    n, m, k = map(int, input().split())
    points = []
    for _ in range(k):
        x, y = map(int, input().split())
        points.append((x, y))

    def dist(p1, p2):
        return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

    def all_burned(points, time):
        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if not any(dist((x, y), p) <= time for p in points):
                    return False
        return True

    lo, hi = 1, n * m
    while lo < hi:
        mid = (lo + hi) // 2
        if all_burned(points, mid):
            hi = mid
        else:
            lo = mid + 1

    print(lo)


solve()
