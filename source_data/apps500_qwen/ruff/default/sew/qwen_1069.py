import sys
from math import inf, sqrt

input = sys.stdin.read
data = input().split()

n = int(data[0])
x1, y1 = int(data[1]), int(data[2])
x2, y2 = int(data[3]), int(data[4])
flowers = [(int(data[5 + 2 * i]), int(data[6 + 2 * i])) for i in range(0, n)]


def dist(x, y, x0, y0):
    return (x - x0) ** 2 + (y - y0) ** 2


min_r1_squared_plus_r2_squared = inf

for i in range(0, n):
    r1_squared = dist(flowers[i][0], flowers[i][1], x1, y1)
    r2_squared = dist(flowers[i][0], flowers[i][1], x2, y2)
    min_r1_squared_plus_r2_squared = min(
        min_r1_squared_plus_r2_squared, r1_squared + r2_squared
    )

    for j in range(i + 1, n):
        r1_squared = max(
            dist(flowers[i][0], flowers[i][1], x1, y1),
            dist(flowers[j][0], flowers[j][1], x1, y1),
        )
        r2_squared = max(
            dist(flowers[i][0], flowers[i][1], x2, y2),
            dist(flowers[j][0], flowers[j][1], x2, y2),
        )
        min_r1_squared_plus_r2_squared = min(
            min_r1_squared_plus_r2_squared, r1_squared + r2_squared
        )

print(min_r1_squared_plus_r2_squared)
