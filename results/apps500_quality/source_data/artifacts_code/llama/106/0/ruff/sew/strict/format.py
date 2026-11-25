import math


def dist(a, b):
    n, m, k = map(int, input().split())
    a, b = (a - 1) % (m * n * k), (b - 1) % (m * n * k)
    dist = abs(a - b)
    if not dist <= (n * m * k - dist):
        return min(dist, (n * m * k - dist) + 2 * (n * m * k))
    else:
        return min(dist, (n * m * k - dist))


def walk_time(d):
    return 15 * d


def lift_time(d):
    return 10 + d


def min_time(a, b):
    n, m, k = map(int, input().split())
    a, b = (a - 1) % (m * n * k), (b - 1) % (m * n * k)
    steps = min((a, 0), (b, 0))
    steps = min(steps, (0, a), (0, b))
    d = dist(a, b)
    return min(
        lift_time(
            math.ceil((a - steps[0]) / (m * k)) + math.ceil((b - steps[1]) / (m * k))
        )
        + walk_time(math.ceil((steps[0] - a) / m) + math.ceil((steps[1] - b) / m) + d),
        walk_time(
            math.ceil((a - steps[0]) / m)
            + math.ceil((n * m * k - b - steps[1]) / m)
            + (d + n * m - 1)
        )
        + lift_time(
            math.ceil((a - steps[0]) / (m * k))
            + math.ceil((n * m * k - b - steps[1]) / (m * k))
            - n * m
        )
        + walk_time(math.ceil((steps[0] - a) / m) + math.ceil((b - steps[1]) / m)),
    )


a, b = map(int, input().split())
print(min_time(a, b))
