import math
import sys


def dist(x1, y1, x2, y2):
    return  math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def min_distance_to_fountain(points):
    x1, y1=points[0]
    x2, y2=points[1]
    distances=list()
    for  point in  points[2:]:
        x, y=point
        d1, d2 = dist(x1, y1, x, y), dist(x2, y2, x, y)
        distances.append((d1, d2))
    return  distances

def min_sum_of_squares(distances):
    max_d1 = max_d2 = 0
    for  d1, d2 in  distances:
        max_d1=max(max_d1, d1)
        max_d2=max(max_d2, d2)
    r1 = math.ceil(max_d1)
    r2 = math.ceil(max_d2)
    return  r1**2 + r2**2

def main():
    n, x1, y1, x2, y2=map(int, sys.stdin.readline().split())
    points=list(map(int, sys.stdin.readline().split()))
    points=[(-1, 0), (x1, y1), (x2, y2)]+[(point[0], point[1]) for point in points]
    distances=min_distance_to_fountain(points)
    print(min_sum_of_squares(distances))

if  __name__=="__main__":
    main()
