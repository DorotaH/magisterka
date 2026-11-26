import sys
from math import sqrt

input = sys.stdin.read
data = input().split()

N = int(data[0])
points = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(0, N)]


def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def min_circle_radius(points):
    if 1 == len(points):
        return 0
    if 2 == len(points):
        return distance(points[0], points[1]) / 2
    for i in range(len(points)):
        for j in range(1 + i, len(points)):
            center = (
                (points[i][0] + points[j][0]) / 2,
                (points[i][1] + points[j][1]) / 2,
            )
            radius = distance(points[i], center)
            if all(distance(point, center) <= radius for point in points):
                return radius
    for i in range(len(points)):
        for j in range(1 + i, len(points)):
            for k in range(1 + j, len(points)):
                center_x = (points[i][0] + points[j][0] + points[k][0]) / 3
                center_y = (points[i][1] + points[j][1] + points[k][1]) / 3
                radius = distance(points[i], (center_x, center_y))
                if all(
                    distance(point, (center_x, center_y)) <= radius for point in points
                ):
                    return radius
    return float("inf")


print(min_circle_radius(points))
