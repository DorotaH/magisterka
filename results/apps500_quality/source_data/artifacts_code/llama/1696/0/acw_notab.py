import sys
import math


def get_ints():
    return list(map(int, input().split()))


def get_floats():
    return list(map(float, input().split()))


def solve():
    n, m, k = get_ints()
    x, y = [], []
    for _ in range(k):
        x.append(get_ints()[0])
        y.append(get_ints()[1])

    max_dist = 0
    for i in range(k):
        for j in range(i + 1, k):
            max_dist = max(max_dist, abs(y[i] - y[j]) + abs(x[i] - x[j]))

    max_dist += 1
    result = 0
    while True:
        result += 1
        new_max_dist = max_dist - 1
        for i in range(k):
            for j in range(4):
                new_x = x[i] + [-1, 0, 1, 0][j]
                new_y = y[i] + [0, 1, 0, -1][j]
                if 1 <= new_x <= n and 1 <= new_y <= m and (new_x, new_y) not in [(x[i], y[i]) for i in range(k)]:
                    new_max_dist = max(new_max_dist, abs(x[i] - new_x) + abs(y[i] - new_y))
        if new_max_dist == max_dist:
            break
        max_dist = new_max_dist

    print(result)


if __name__ == "__main__":
    solve()
