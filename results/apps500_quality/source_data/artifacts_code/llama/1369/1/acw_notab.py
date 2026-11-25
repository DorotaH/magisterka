import math
import sys


def min_circle(points):
    n = len(points)
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)

    cx = (max_x + min_x) / 2
    cy = (max_y + min_y) / 2

    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    return math.sqrt((max(x_coords - cx)**2 + (max(y_coords - cy)**2)))


n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

radius = min_circle(points)
print('{:.6f}'.format(radius))
