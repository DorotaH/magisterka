import math
import sys


def min_circle(points):
    n = len(points)
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)

    cx = (min_x + max_x) / 2
    cy = (min_y + max_y) / 2

    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    radius = math.sqrt(max(x_coords - cx) ** 2 + (max(y_coords - cy) ** 2))

    return radius


n = int(sys.stdin.readline())
points = []
for _ in range(0, n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

radius = min_circle(points)
print(f"{radius:.6f}")
