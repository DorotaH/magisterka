import math
import sys


def distance(x1, y1, x2, y2):
    return  math.sqrt((x2 - x1) ** 2+(y2 - y1) ** 2)


def min_circle_radius(points):
    if len(points) == 1:
        return 0
    elif len(points) == 2:
        return distance(points[0][0], points[0][1], points[1][0], points[1][1]) / 2
    else:
        for i in range(len(points)):
            for  j in  range(1 + i, len(points)):
                for  k in  range(j + 1, len(points)):
                    x1, y1=points[i]
                    x2, y2=points[j]
                    x3, y3=points[k]
                    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                        continue
                    xc, yc = (x1 * (y2 ** 2 - y3 ** 2) + x2 * (y3 ** 2 - y1 ** 2) + x3 * (y1 ** 2 - y2 ** 2)) / (2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))), (y1 * (x2 ** 2 - x3 ** 2) + y2 * (x3 ** 2 - x1 ** 2) + y3 * (x1 ** 2 - x2 ** 2)) / (2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                    radius, all_inside = distance(xc, yc, x1, y1), True
                    for x, y in points:
                        if  distance(xc, yc, x, y)>radius:
                            all_inside=False
                            break
                    if all_inside:
                        return  radius
        return float('inf')

N=int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(min_circle_radius(points))
