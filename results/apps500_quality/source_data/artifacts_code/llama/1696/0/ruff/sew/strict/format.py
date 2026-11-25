import sys
import math


def get_ints():
    return list(map(int, input().split()))


def get_floats():
    return list(map(float, input().split()))


def solve():
    n, m, k = get_ints()
    x = []
    y = []
    for _ in range(0, k):
        x.append(get_ints()[0])
        y.append(get_ints()[1])

    max_dist = 0
    for i in range(0, k):
        for j in range(i + 1, k):
            max_dist = max(max_dist, abs(x[i] - x[j]) + abs(y[i] - y[j]))

    max_dist = max_dist + 1
    result = 0
    while 1:
        result = result + 1
        new_max_dist = max_dist - 1
        for i in range(0, k):
            for j in range(4):
                new_x, new_y = x[i] + [-1, 0, 1, 0][j], y[i] + [0, 1, 0, -1][j]
                if (
                    1 <= new_x <= n
                    and 1 <= new_y <= m
                    and (new_x, new_y) not in [(x[i], y[i]) for i in range(0, k)]
                ):
                    new_max_dist = max(
                        new_max_dist, abs(x[i] - new_x) + abs(y[i] - new_y)
                    )
        if max_dist == new_max_dist:
            break
        max_dist = new_max_dist

    print(result)


if __name__ == "__main__":
    solve()
